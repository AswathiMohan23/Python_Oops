class Science(object):
    def subjects(self):
        print("physics ,chemistry,biology")


class physics(Science):
    def subject1(self):
        print("Subject1 is physics")


class chemistry(Science):
    def subject2(self):
        print("Subject2 is chemistry")


obj1 = physics()
obj2 = chemistry()
obj1.subjects()
obj1.subject1()
obj2.subjects()
obj2.subject2()