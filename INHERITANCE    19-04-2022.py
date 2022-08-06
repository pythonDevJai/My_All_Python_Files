##                                   **************** INHERITANCE  ****************
##
##
##SINGLE INHERITANCE:-
##
##
##PARENT CLASS:-
"""
class mahesh:
    qualification = "B.E"
    vehicle = "TVS Champ"



class mahesh_son(mahesh):
    name = "charvik"
    born = "14-02-2020"

maheshFamily_obj = mahesh_son()

print("mahesh son name is {}".format(maheshFamily_obj.name))
print("mahesh son born in {}".format(maheshFamily_obj.born))
print("mahesh qualification is {}".format(maheshFamily_obj.qualification))
print("mahesh vehicle is {}".format(maheshFamily_obj.vehicle))


#   MULTIPLE INHERITANCE:-

class adding:
    def add_fun(self , a , b):
        return "After adding my result is {}".format(a + b)

class sub:
    def sub_fun(self , a ,b):
        return "After sub my result is {}".format(a - b)

class multiples(sub , adding):
    def multiples_fun(self , a , b):
        return "After multiplied my result is {}".format(a * b)

multiples_obj = multiples()

print(multiples_obj.multiples_fun(10 ,2))
print(multiples_obj.sub_fun(10 , 5))
print(multiples_obj.add_fun(5 , 5))


#   MULTILEVEL INHERITANCE:-
class mahesh_dad:
    name = "john"
    qualification = "b.sc"
    vehicle = "Enfield"

class mahesh(mahesh_dad):
    name = "mahesh"
    qualification = "B.E"
    vehicle = "TVS Champ"



class mahesh_son(mahesh):
    name = "charvik"
    born = "14-02-2020"

maheshFamily_obj = mahesh_son()

print("mahesh son name is {}".format(maheshFamily_obj.name))
print("mahesh son born in {}".format(maheshFamily_obj.born))
print("mahesh qualification is {}".format(maheshFamily_obj.qualification))
print("mahesh vehicle is {}".format(maheshFamily_obj.vehicle))



"""



class parent:
    name = "rocky"
    age = 25

class son(parent):
    name = "sharma"
    

parent_obj = parent()
son_obj = son()

##print(parent_obj.name)
##print(parent_obj.age)
print(son_obj.name)
print(son_obj.age)

