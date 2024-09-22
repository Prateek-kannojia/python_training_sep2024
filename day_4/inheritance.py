class A:
    pass

class B(A):
    pass

class C(B):
    pass

obj1 = A()
obj2 = B()
obj3 = C()
print(type(obj1)) #o/p = <class '__main__.A'>
print(isinstance(obj1,B)) # o/p:False
print(isinstance(obj2,B)) # i/p:True
print(isinstance(obj3,B)) # i/p:True