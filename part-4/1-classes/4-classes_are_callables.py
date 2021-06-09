class Program:
    language = 'Python'

    def say_hello():
        print(f'Hello from {Program.language}')


p = Program()
print(type(p))

print(p.__dict__)
print(Program.__dict__)

print(p.__class__)

# BEST PRACTICES
print(isinstance(p, Program))
