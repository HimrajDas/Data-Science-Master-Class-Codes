class Pwskills:

    def __init__(self, name, email):
        self.name = name
        self.email = email


    def student_details(self):
        print(self.name, self.email)


# student = Pwskills("himraj", "himraj@gmail.com")
# print(student.name)
# student.student_details()


class Pwskills1:

    def __init__(self.name, self.email):
        self.name = name
        self.email = email


    @classmethod
    def details(cls, name, email):
        return cls(name, email)