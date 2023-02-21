class Pwskills:

    def student_details(self, name, mail_id, number):
        print(name, mail_id, number)

    
    @staticmethod
    def mentor_mail_id(mail_id):
        print(mail_id)


    @staticmethod
    def mentor_names(mentor_list):
        print(mentor_list)
        # Pwskills.mentor_mail_id(["sudh@gmail.com", "krish@gmail.com"])

    
    @classmethod
    def course_name(cls, course_name):
        print(course_name)
        cls.mentor_names(["sudhansu", "krish"])



# Pwskills.mentor_names(["Sudhansu", "Krish"])
pw = Pwskills()

pw.course_name("Data Science Masters")
