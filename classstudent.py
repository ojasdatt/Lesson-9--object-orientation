class student:
    grade = 7
    name = "Aaryan"

    def introduction(self):
        print("I am a student")

    def details(self):
        print("My name is:", self.name)
        print("I am in grade:",self.grade)

ob = student()
ob.introduction()
ob.details()