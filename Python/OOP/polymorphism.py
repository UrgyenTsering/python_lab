class Nepali:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"नमस्कार म {self.name} ho |"


class English:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello. I am {self.name}."


def talk(object_name):
    return object_name.greet()


n1 = Nepali("Rabindra")
e1 = English("Ram")

print(talk(n1))
print(talk(e1))
