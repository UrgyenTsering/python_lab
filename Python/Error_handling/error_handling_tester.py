# from datetime import datetime, date


# def get_age(dob):
#     try:
#         birth_date = datetime.strptime(dob, "%Y-%m-%d").date()

#     except ValueError:
#         raise ValueError("The format of DOB is not valid")

#     today = date.today()

#     if birth_date > today:
#         raise ("The Date of Birth can't be in future or greater than today's date")

#     age = today.year - birth_date.year

#     if (today.month, today.day) < (birth_date.month, birth_date.day):
#         age = age - 1

#     return age


# print(get_age("1996-04-11"))


class People:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @property
    def get_age(self):
        age = 2026 - self.birth_year
        return age

    def __repr__(self):
        return f"{self.name} is of age {self.get_age}"

    def is_adult(self):
        user_age = self.get_age
        if user_age > 18:
            return True
        else:
            return False


p1 = People("Rabindra", 1990)
p2 = People("Ram", 1995)

print(p1)
print(p2)

print(p1.is_adult())
print(p2.is_adult())
