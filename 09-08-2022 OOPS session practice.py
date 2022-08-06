"""
class student:
    name = "jai"
    age = 24
    dept = "ECE"

    def student_details(self):
        return {"name" : "jai" , "From" : "Tiruttani"}

student_obj = student()

print(student_obj.name)
print(student_obj.age)
print(student_obj.dept)
print()
print(student_obj.student_details())


------------------------------------------------------------------------------

class Arithmatic:
    a = 10
    b = 10
    def calculator(self):
        a = 20
        b = 30
        
        return a + b


arth_obj = Arithmatic()
print(arth_obj.a)
print(arth_obj.b)
print()
print(arth_obj.calculator())


-------------------------------------------------------------------------------
"""
a = 100
b = 50
def add():
    a =10
    print("global a is-------->",a)
    def sub():
        global a
        print(a)
        print(b)

    sub()

add()





