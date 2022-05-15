class IFlying:
    def __init__(self,Ihigh=0, Ivel=0, Itime=0):
        self.Ihigh = Ihigh
        self.Ivel = Ivel
        self.Itime = Itime
    def IFlying(self):
        print('Hi, the height of the flight is {height}.'
              'The velocity of flight is {vel}. And the '
              'duration of the flight is {time}'.format(height=self.Ihigh,
              vel=self.Ivel, time=self.Itime))
    def IExtraFlying(self,acc):
        self.Iacc = acc
        self.IFlying()
        print('And beacause the flight is extraordinary, '
              'get to know of the acceleration {acc}'.format(acc=self.Iacc))
    def INoflying(self):
        print('There is no flight at all')
        print('Test')


import time


def wrepSOmething(func):
    def wrappingFunction(*args,**kwargs):
        print('I am wrapping the simple function here!')
        return func(*args,**kwargs)

    return wrappingFunction

@wrepSOmething
def doSomething(arg:str):
    print('THis is a simple displaying function',arg)

@wrepSOmething
def doSomethingElse(param1:float,param2:float,param3:float):
    print(f'The sum of parametr 1 {param1}, parametr 2 {param2}, parametr 3 {param3} is {param1+param2+param3}')


def measureTime(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        end = time.time()
        print(f'Function {func.__name__} lasted for {end-start} s')
        return res
    return wrapper

@measureTime
def runF1():
    time.sleep(1)
    return 0

@measureTime
def runF2():
    time.sleep(2)
    return 0

class decorator:
    def __init__(self,f):
        self.f = f
    def __call__(self, *args, **kwargs):
        print('This is a monit before function call')
        self.f(*args,**kwargs)
        print('This is a monit after function call')




class decoratorWithargs:
    def __init__(self, dec_arg):
        self.dec_arg = dec_arg
    def __call__(self, func):
        def inner(*args, **kwargs):
            print(f'I am a decorator ({decorator.__name__}) of the function {func.__name__}'
                 f'My parameter is set to {self.dec_arg}')
            func(*args,**kwargs)
        return inner

@decoratorWithargs(5)
def testingClassDec(*args,**kwargs):
    print('I am aware of the stuff!')
    print('Positional arguments are as folows:')
    # print(kwargs)
    for item in args:
        print(item)
    print('Key arguments are as follows')
    for k,v in kwargs.items():
        print(k, ' ==> ', v)


def A(f):
    def inner():
        print('Dec A - start')
        f()
        print('Dec A - end')
    return inner

def B(f):
    def inner():
        print('Dec B - start')
        f()
        print('Dec B - end')
    return inner

@A
@B
def funkcja():
    print('Base function')


if __name__ == '__main__':
    doSomething('Karol')
    print()
    doSomethingElse(1,2,3)
    print()
    runF1()
    runF2()
    testingClassDec(1, 2, 3, 4, a = 5, b = 6 ,c = 7)

    print()
    funkcja()



