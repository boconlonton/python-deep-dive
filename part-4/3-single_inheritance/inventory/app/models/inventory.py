"""Inventory models"""


from app.utils.validators import validate_integer


class Resource:
    """Base class for resource"""
    __slots__ = '_name', '_manufacturer', '_total', '_allocated', '__dict__'

    def __init__(self, name, manufacturer, total, *, allocated=0):
        """

        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resource
            allocated (int): current count of in-use resource
        Note:
            `allocated` cannot exceed `total`
        """
        self._name = name
        self._manufacturer = manufacturer

        validate_integer('total', total, min_value=0)
        self._total = total

        validate_integer(
            'allocated', allocated, 0, total,
            custom_max_message='Allocated inventory cannot exceed total inventory'
        )
        self._allocated = allocated

    @property
    def name(self):
        """

        Returns:
            str: the resource name
        """
        return self._name

    @property
    def manufacturer(self):
        """

        Returns:
            str: the resource manufacturer
        """
        return self._manufacturer

    @property
    def total(self):
        """

        Returns:
            int: the total inventory count
        """
        return self._total

    @property
    def allocated(self):
        """

        Returns:
            int: number of resources in use
        """
        return self._allocated

    @property
    def category(self):
        """

        Returns:
            str: the resource category
        """
        return self.__class__.__name__.lower()

    @property
    def available(self):
        """

        Returns:
            int: number of resources available for uses
        """
        return self.total - self.allocated

    def check_availability(self, *, died=False):
        if died:
            return self._allocated in range(1, self._total + 1)
        else:
            return self._allocated < self._total

    def claim(self, value):
        """
        Claim `value` inventory items (if available)

        Args:
            value (int): Number of inventory items to claim

        Returns:

        """
        validate_integer(
            'value', value, 1, self.available,
            custom_max_message='Cannot claim more than available'
        )
        self._allocated += value

    def freeup(self, value: int):
        """
        Return an inventory item to the available pool

        Args:
            value (int): NUmber of items to return (cannot exceed number in use)

        Returns:

        """
        validate_integer(
            'value', value, 1, self.allocated,
            custom_max_message='Cannot claim more than allocated'
        )
        self._allocated -= value

    def died(self, value: int):
        """
        Number of items to deallocate and remove from the inventory pool
        altogether

        Args:
            value (int): Number of items that have died

        Returns:

        """
        validate_integer(
            'value', value, 1, self.allocated,
            custom_max_message='Cannot retire more than allocated'
        )
        self._allocated -= value
        self._total -= value

    def purchased(self, value: int):
        """
        Add new inventory to the pool

        Args:
            value (int): Number of items to add to the pool

        Returns:

        """
        validate_integer('value', value, 1)
        self._total += value

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, ' \
               f'manufacturer={self.manufacturer}, ' \
               f'total={self.total}, ' \
               f'allocated={self.allocated})'


class CPU(Resource):
    """Resource subclass used to track specific CPU inventory pools"""

    def __init__(self, name, total, manufacturer,
                 cores, socket, power_watts, *, allocated=0):
        """

        Args:
            name (str): display name of resource
            total (int): current total amount of resources
            manufacturer (str): resource manufacturer
            cores (int): number of cores
            socket (str): CPU socket type
            power_watts (int): CPU rated wattage
            allocated (int): current count of in-use resources
        """
        super().__init__(name, manufacturer, total, allocated=allocated)

        validate_integer('cores', cores, 1)
        validate_integer('power_watts', power_watts, 1)

        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts

    @property
    def cores(self):
        """
        Number of cores

        Returns:
            int
        """
        return self._cores

    @property
    def socket(self):
        """
        The socket type for this CPU

        Returns:
            str
        """
        return self._socket

    @property
    def power_watts(self):
        """
        The rated wattage of this CPU

        Returns:
            int
        """
        return self._power_watts

    def __repr__(self):
        return f'{self.category}: {self.name} ({self.socket} - x{self.cores}'


class Storage(Resource):
    """
    A base class for storage devices - probably not used directly
    """

    def __init__(self, name, manufacturer, total, capacity_gb, *, allocated=0):
        """

        Args:
            name (str): display name of resources
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            capacity_gb (int): storage capacity (in GB)
            allocated (int): current count of in-use resources
        """
        super().__init__(name, manufacturer, total, allocated=allocated)
        validate_integer('capacity_gb', capacity_gb, 1)
        self._capacity_gb = capacity_gb

    @property
    def capacity_gb(self):
        """
        Indicates the capacity (in GB) of the storage device

        Returns:
            int
        """
        return self._capacity_gb

    def __repr__(self):
        return f'{self.category}: {self.capacity_gb} GB'


class SSD(Storage):
    """
    Class used for SSD type resources
    """

    def __init__(self, name, manufacturer, total,
                 capacity_gb, interface, *, allocated=0):
        """

        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            capacity_gb (int): storage capacity (in GB)
            interface (str): indicates the device interface (e.g PCIe NVMe 3.0 x4)
            allocated (int): current count of in-use resource
        """
        super().__init__(name, manufacturer, total, capacity_gb, allocated=allocated)

        self._interface = interface

    @property
    def interface(self):
        """
        Interface used by SSD (e.g PCIe NVMe 3.0 x4)

        Returns:
            str
        """
        return self._interface

    def __repr__(self):
        s = super().__repr__()
        return f'{s} ({self.interface})'


class HDD(Storage):
    """
    Class used for HDD type resources
    """

    def __init__(self, name, manufacturer, total,
                 size, rpm, capacity_gb, *, allocated=0):
        """

        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            size (str): indicates the device size (must be either 2.5" or 3.5")
            rpm (int): disk rotation speed (in rpm)
            capacity_gb (int): storage capacity (in GB)
            allocated (int): current count of in-use resources
        """
        super().__init__(name, manufacturer, total, capacity_gb, allocated=allocated)

        allowed_sizes = ['2.5"', '3.5"']
        if size not in allowed_sizes:
            raise ValueError(
                f'Invalid HDD size. '
                f'Must be one of {", ".join(allowed_sizes)}'
            )

        validate_integer('rpm', rpm, min_value=1_000, max_value=50_000)
        self._size = size
        self._rpm = rpm

    @property
    def size(self):
        """
        The HDD size (2.5" / 3.5")

        Returns:
            str
        """
        return self._size

    @property
    def rpm(self):
        """
        The HDD spin speed (rpm)

        Returns:
            int
        """
        return self._rpm

    def __repr__(self):
        s = super().__repr__()
        return f'{s} ({self.size}, {self.rpm} rpm)'
