# # Method order resolution 

# class A(object):
#     def method(self):
#         print('A class method is called')  # 3
#         super().method()

# class B(object):
#     def method(self):
#         print("B class method called")  # 5
#         super().method()

# class C(object):
#     def  method(self):
#         print("C class method called")  #6

# class X(A,B):
#     def method(self):
#         print("X class method called")  # 2
#         super().method()

# class Y(B,C):
#     def method(self):
#         print("Y class method is called")  #4
#         super().method()

# class P(X,Y,C):
#     def method(self):
#         print("P class method called") #1
#         super().method()
# p = P()
# p.method()


