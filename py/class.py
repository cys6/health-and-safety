class Ba:  # 父类
    i = 12345
    b = ''
    _w = 0

    def __init__(self, ina, bna, wight):
        self.ina = ina
        self.bna = bna
        self.wight = wight
        Ba._w += 1

    def say(self):
        print(self.i, self.b)
        # return 'hollo word'


class A(Ba):  # 继承父类
    k = ''

    def __init__(self, ina, bna, wight, koko):
        Ba.__init__(self, ina, bna, wight)
        self.k = koko

    def speak(self):
        print(self.i, self.b, self.k)
        super(A, self).say()
        

class B:  # 定义一个类，父类
    def __init__(self, ti, ha):
        self.ti = ti
        self.ha = ha

    def sting(self):
        print(self.ti, self.ha)
        


class BA(B, A):  # 继承上面所有类
    def __init__(self, ina, bna, wight, koko, ti, ha, baq):
        B.__init__(self, ti, ha)
        A.__init__(self, ina, bna, wight, koko)
        self.bs = baq
        super(BA, self).sting()


b = BA(1, 2, 3, 4, 5, 6, 7)

b.say()
b.sting()
b.speak()
print(Ba.i)
print(b._w)
print(b.__dict__)
