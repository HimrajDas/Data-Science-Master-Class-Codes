class Parent:

    def test_parent(self):
        print("this is my parent class.")


class Child(Parent):
    pass


# child_obj = Child()
# child_obj.test_parent()


class Class1:
    
    def class1(self):
        print("This is my class 1")


class Class2(Class1):

    def class2(self):
        print("This is my class 2")


class Class3(Class2):

    def class3(self):
        print("this is my class 3")


# class_obj = Class3()
# class_obj.class1()


class Class4:

    def class4(self):
        print("this is class 4")


class Class5:

    def class5(self):
        print("This is class 5")


class Class6(Class4, Class5):

    def class6(self):
        # print("this is class 6")
        pass


class_obj = Class6()
class_obj.class5()
