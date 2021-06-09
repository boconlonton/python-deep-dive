class Program:
    language = 'Python'

    def say_hello():
        print(f'Hello from {Program.language}')


print(Program.say_hello)
print(getattr(Program, 'say_hello'))


Program.say_hello()
getattr(Program, 'say_hello')()
