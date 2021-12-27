class calculator:
    def zarb(self, a, b):
        return a*b
    def taghsim(self, a, b):
        return a/b
    def jam(self, a, b):
        return a+b
    def tafrigh(self, a, b):
        return a-b


class calculatorfix:
    def __init__(self):
     self.a = 4
     self.b = 5
    def zarb(self):

        return self.a*self.b
    def taghsim(self):
        return self.a/self.b
    def jam(self):
        return self.a+self.b
    def tafrigh(self):
        return self.a-self.b



class calc_input:
    def __init__(self , a , b):
     self.a = a
     self.b = b

    def zarb(self):
        return self.a*self.b

    def taghsim(self):
        return self.a/self.b

    def jam(self):
        return (self.a+self.b)

    def tafrigh(self):
        return self.a-self.b

