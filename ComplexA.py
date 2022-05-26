class A:
    def __init__(self,a,b):
        
        self.a = a
        self.b = b

class Add(A):
    def add(self):
        resultx = self.a + self.b
        return resultx
class Subtract(A):
    def sub(self):
        resultx = self.a - self.b
        return resultx
class Multiplication(A):
    def mul(self):
        resultx = self.a * self.b
        return resultx
class Divison(A):
    def div(self):
        resultx = self.a / self.b
        return resultx