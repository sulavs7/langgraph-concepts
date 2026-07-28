class Complex:
    def __init__(self,real,img):
        self.real = real 
        self.img = img

    def show_num(self):
        print(self.real,"i +",self.img,"j")
    def __add__(num1,num2):
        newReal = num1.real + num2.real
        newImg = num1.img + num2.img
        return Complex(newReal,newImg)

    def __sub__(num1,num2):
        newReal = num1.real - num2.real
        newImg = num1.img - num2.img
        return Complex(newReal,newImg)
        
c1 = Complex(3,4)
c1.show_num()
c2 = Complex(5,6)
c2.show_num()

c4 = c1-c2
c4.show_num()