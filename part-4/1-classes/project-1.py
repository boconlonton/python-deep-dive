"""
Description: Design & Implement a class that will be used to represent bank accounts
Attributes:
    - account_number
    - first_name
    - last_name
    - preferred_timezone
    - balances (default=0)
Methods:
    - deposits (generate a confirmation number)
    - withdrawals (generate a confirmation number)
    - deposit_interest
    - parse_confirmation_number
"""
from datetime import datetime
from my_datetime import TimeZone, DateTime
from decimal import Decimal, ConversionSyntax, getcontext
from collections import namedtuple
from numbers import Number


TRANSACTION_TYPE = {
    'D': 'Deposit',
    'W': 'Withdrawal',
    'I': 'Interest Deposit',
    'X': 'Denied'
}


class Balance:

    def __init__(self, balance):
        self.data = balance

    @property
    def data(self):
        return round(self._balance, 5)

    @data.setter
    def data(self, value):
        try:
            if value >= 0:
                self._balance = Decimal(value)
            else:
                raise ValueError('Account balance must be greater than or equal 0')
        except ConversionSyntax:
            raise TypeError('Value must be a number')

    def __sub__(self, value):
        if value > self.data:
            raise ValueError('Value must be smaller than or equal balance data')
        self.data -= value


class Transaction:

    global_trans_id = 0
    ConfirmNumber = namedtuple('ConferenceNumber', 'ts_code accnt created_at ts_id')
    transaction_list = []

    def __init__(self, account, transaction_code, amount, created_at=None, transaction_id=None):
        self.account = account
        self.transaction_code = transaction_code
        self.amount = amount
        self.created_at = created_at
        self._confirmation_number = None
        self.transaction_id = transaction_id
        Transaction.transaction_list.append(self)

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        if isinstance(value, BankAccount):
            self._account = value
        else:
            raise ValueError('Invalid bank account')

    @property
    def transaction_code(self):
        return self._transaction_code

    @transaction_code.setter
    def transaction_code(self, value):
        value = value.upper()
        if value in TRANSACTION_TYPE:
            self._transaction_code = value
            self._transaction_type = TRANSACTION_TYPE.get(value)
        else:
            raise ValueError(f"Invalid transaction type: must be "
                             f"{','.join(k for k in TRANSACTION_TYPE)}")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError('Amount must be greater than 0')
        self._amount = value

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        if value is None:
            self._created_at = datetime.now()
        else:
            if isinstance(value, datetime):
                self._created_at = value
            else:
                raise TypeError('Value must be datetime object')

    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        if value and value >= 0:
            self._transaction_id = value
        else:
            self._transaction_id = Transaction.global_trans_id
            Transaction.global_trans_id += 1

    @property
    def confirmation_number(self):
        if self._confirmation_number is None:
            dt = DateTime(self.created_at, self.account.timezone)
            self._confirmation_number = f'{self.transaction_code}-' \
                                        f'{self.account.account_number}-' \
                                        f'{dt.utc_as_string}-' \
                                        f'{self.transaction_id}'
        return self._confirmation_number

    @classmethod
    def parse_confirmation_number(cls, conf_num, timezone):
        transaction = next(filter(
            lambda x: x.confirmation_number == conf_num and x.account.timezone == timezone,
            Transaction.transaction_list
        ))
        return transaction


class BankAccount:
    transaction_id = 0
    account_list = []

    def __init__(self,
                 account_number,
                 first_name,
                 last_name,
                 preferred_timezone=None,
                 balances=0,
                 interest=None,
                 *args,
                 **kwargs):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.timezone = preferred_timezone
        self._balances = Balance(balances)
        self.interest = None

        BankAccount.account_list.append(self)

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        if isinstance(value, str) and value:
            self._account_number = value
        else:
            raise TypeError('Account number must be a non-empty string')

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str) and value:
            self._first_name = value
        else:
            raise TypeError('First name must be a non-empty string')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str) and value:
            self._last_name = value
        else:
            raise TypeError('Last name must be a non-empty string')

    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        if isinstance(value, TimeZone):
            self._timezone = value
        else:
            raise TypeError('Timezone must be a TimeZone instance')

    @property
    def balance(self):
        return self._balances

    @balance.setter
    def balance(self, value):
        if isinstance(value, Balance):
            self._balances = value
        else:
            raise TypeError('Value must be of Balance type')

    def deposit(self, amount):
        transaction_code = 'd'
        self.balance.data += amount
        return Transaction(self, transaction_code, amount)

    def withdraw(self, amount):
        transaction_code = 'w'
        try:
            self.balance = self.balance - amount
        except ValueError:
            transaction_code = 'x'
            print('Not allowed')
        finally:
            return Transaction(self, transaction_code, amount)

    def deposit_interest(self):
        if self.interest:
            if self.balance.data > 0:
                deposit_interest = (Decimal(self.interest) * self.balance.data) / 100
                return self.deposit(deposit_interest)
        else:
            raise ValueError('Please interest value')


# Usage
tz1 = TimeZone('Asia/Ho_Chi_Minh')
acc = BankAccount(
    account_number='123123214',
    first_name='Tommy',
    last_name='Truong',
    preferred_timezone=tz1,
    balances=0
)
