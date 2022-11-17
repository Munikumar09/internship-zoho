# class Test:
#     class __NormalTest:
#        def __init__(self):
#         print("nomal test")
#     def get_inner(self):
#         return Test.__NormalTest
class Test:
    a = 10
    def __init__(self):
        print("Constructor Execution...")
    def __del__(self):
        print("Destructor Execution...")
test1=Test()
test2=test1
print(test1, test2)
del test1
print(test2.a)
del test2

