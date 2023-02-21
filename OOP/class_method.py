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

    def __init__(self, name, email):
        self.name = name
        self.email = email


    @classmethod
    def details(cls, name, email):
        return cls(name, email)

    
    def student_details(self):
        print(self.name, self.email)
        

pw = Pwskills1.details("himraj", "himraj@gmail.com")
# print(pw.name, pw.email)
# pw.student_details()



class Pwskills2:

    mobile_number = 9188845467

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email


    @classmethod
    def change_number(cls, mobile):
        Pwskills2.mobile_number = mobile

    
    @classmethod
    def details(cls, name, email):
        return cls(name, email)

    
    def student_details(self):
        print(self.name, self.email, Pwskills2.mobile_number)


# Pwskills2.mobile_number


class Pwskills3:

    mobile_number = 9188845467

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email


    @classmethod
    def change_number(cls, mobile):
        Pwskills2.mobile_number = mobile

    
    @classmethod
    def details(cls, name, email):
        return cls(name, email)

    
    def student_details(self):
        print(self.name, self.email, Pwskills2.mobile_number)


def course_details(cls, course_name):
    print("Course details: ", course_name)

Pwskills3.course_details = classmethod(course_details)
# Pwskills3.course_details("Data Science Masters")

class Pwskills4:

    mobile_number = 9188845467

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email


    @classmethod
    def change_number(cls, mobile):
        Pwskills2.mobile_number = mobile

    
    @classmethod
    def details(cls, name, email):
        return cls(name, email)

    
    def student_details(self):
        print(self.name, self.email, Pwskills2.mobile_number)

# To delete a method from a class
del Pwskills4.change_number
delattr(Pwskills4, "details")
