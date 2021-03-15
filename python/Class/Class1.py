# class mit:
#     def cs:
#         print("aa")
# m1=mit

# class mit:
#     def cs(self):
#         print("aaaaaaaaaa")
# #   x = 5

# p1 = mit()
# print(p1.cs())

# print("HIIIIIIIIIIIIIIIIIIIIIIIIII")
# init funtion
# A Sample class with init method   

# class Person:   
      
#     # init method or constructor    
#     def __init__(self, name):   
#         self.name = name   
      
#     # Sample Method    
#     def say_hi(self):   
#         print('Hello, my name is', self.name)   
      
# p = Person('Nikhil')   
# p.say_hi() 

# in class     Con
# class mit:   
      
#     # init method or constructor    
#     def __init__(self, a,b):   
#         self.a=10 
#         self.b=10 

      
#     # Sample Method    
#     def cs(self):   
#         print('value of a b', self.a,self.b)   
      
# p = mit(10,20)   
# p.cs() 

                    # Print mob and name by user
# class mit:   
      
    # init method or constructor    
    # def __init__(self, a,b):   
    #     self.a=10 
    #     self.b=20
#     def __init__(self,name,mob):
#         self.name=name
#         self.mob=mob
#         self.cname="AseemG"
          
#     # Sample Method    
#     # def cs(self):   
#     #     print('value of a b', self.a,self.b)   
#     def cs2(self):
#         print("the name and mob",self.name,self.mob,self.cname)
        
# name=input("enter the name ")
# mob=int(input("enter the mobil no. "))
# p = mit(name,mob)   
# p.cs2() 

# using dos

#  def __init__(self,name,mob):
#         self.name=name
#         self.mob=mob
#         self.cname="AseemG"
          
#     # Sample Method    
#     # def cs(self):   
#     #     print('value of a b', self.a,self.b)   
#     def cs2(self):
#         print("the name and mob",self.name,self.mob,self.cname)
        
# name=input("enter the name ")
# mob=int(input("enter the mobil no. "))
# p = mit(name,mob)   
# p.cs2() 

# using the dict   
# class mit:   
#     def __init__(self,name,mob):
#         self.name=name
#         self.mob=mob
#         self.cname="AseemG"
          
#     # Sample Method    
#     # def cs(self):   
#     #     print('value of a b', self.a,self.b)   
#     def cs2(self):
#         print("the name and mob",mit.__dict__)
        
# name=input("enter the name ")
# mob=int(input("enter the mobil no. "))
# p = mit(name,mob)   
# p.cs2() 

# using decorater 
class mit:   
    col="mit"
    def __init__(self):
        print(col)
          
@classmethod
def show():
    print(col)
    
        

p = mit  
p.show()

