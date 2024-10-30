class Student:
    # def __init__(self,f_name,l_name,age):
    #     self.f_name = f_name
    #     self.l_name = l_name
    #     self.age = age
    
    def print_student(self):
        print(f"The name of student is : {self.f_name, self.l_name} and his age is : {self.age}")
        
    def set_f_name(self,name):
        self.f_name = name
        
    def set_l_name(self,lname):
        self.l_name = lname
        
    def set_age(self,age):
        self.age = age
        
    def get_f_name(self):
        return self.f_name
    
    def get_lname(self):
        return self.l_name
    
    def get_age(self):
        return self.age
        
# s1 = Student('Abhi','Wagh',28)
# s1.print_student()

s1 = Student()
s1.set_f_name('Abhi')
s1.get_f_name
