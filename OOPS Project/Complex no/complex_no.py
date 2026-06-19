# Complex No proto type
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def __str__(self):
        return f"{self.real} + {self.img}i"

    def __add__(self, num):
        NewReal = self.real + num.real
        NewImg = self.img + num.img
        return Complex(NewReal, NewImg)
    
    def __sub__(self, num):
        NewReal = self.real - num.real
        NewImg = self.img - num.img
        return Complex(NewReal, NewImg)
    
    def __mul__(self, num): #(a+bi)(c+di) = (ac-bd) + (ad+bc)i
        NewReal = (self.real * num.real) - (self.img * num.img)
        NewImg = (self.real * num.img) + (self.img * num.real)
        return Complex(NewReal, NewImg)
    
    
num_1 = Complex(3, 4)
num_2 = Complex(6, 3)
print(num_1)
print(num_2)

cn_1 = num_1 + num_2
cn_2 = num_1 - num_2
cn_3 = num_1 * num_2
print(f"Addition: {cn_1}")
print(f"Substraction: {cn_2}")
print(f"Multiplication: {cn_3}")