class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


admin: User = User('Magesh', 38)

print(admin.name)
