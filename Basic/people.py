import json


class peolpe:
    name = ''
    age = 0

    def __init__(self,n,a):
        self.name = n
        self.age = a
    
    def speak(self):
        print(f'我是{self.name}，今年{self.age}岁!')

p = peolpe('bowen',25)
p.speak()

class singer(peolpe):
    work = ''

    # def __init__(self,n,a,w):
    #     self.name = n
    #     self.age = a
    #     self.work = w

    def __init__(self,n,a,w):
        peolpe.__init__(self,n,a)
        self.work = w
    
    def speak(self):
        print(f'我是{self.work}:{self.name}，今年{self.age}岁!')

p = singer('katy',33,'歌手')
p.speak()

class star():
    name = ''
    work = ''
    def __init__(self,n,w):
        self.name = n
        self.work = w
    
    def speak(self):
        print(f'我是明星:{self.name}，我的职业是{self.work}')

class superStar(star,singer):#在多继承时,如果子类没有重写父类的方法,子类在使用父类的方法时,哪个父类在前,就调用哪个父类的方法
    __name = ''
    def __init__(self,n,a,w):
        star.__init__(self,n,w)
        singer.__init__(self,n,a,w)
        self.__name = n

    def speak(self):
        print(f'我是明星:{self.__name}，我的职业是{self.work},今年{self.age}岁')

    def jsonformat(self):
        return {
            'name':self.__name,
            'age':self.age,
            'work':self.work
        }

p = superStar('katy',33,'歌手')
p.speak()
print(p.jsonformat())
print(json.dumps(p,ensure_ascii=False,default=p.jsonformat()))