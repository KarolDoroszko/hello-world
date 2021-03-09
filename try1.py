import Inter
class Duck:
    def __init__(self, Dtype, Dname,Dflying):
        self.Dtype = Dtype
        self.Dname = Dname
        self.Dflying = Dflying
    def Dflying_meth(self):
        if self.Dtype == 'NoFlying':
            self.Dflying.INoflying()
        if self.Dtype == 'NormalFlying':
            self.Dflying.IFlying()
        if self.Dtype == 'ExtraFlying':
            self.Dflying.IExtraFlying(100)

if __name__ == '__main__':
    print('Hello world!')
    print('Hello, I have just extended thr script')
    InterFLY = Inter.IFlying(50,50,50)
    InterNOF = Inter.IFlying()
    InterEXF = Inter.IFlying(100,100,100)

    DuckNormal = Duck('NormalFlying','Flying Duck',InterFLY)
    DuckExtra = Duck('ExtraFlying','Extra Flying Duck',InterEXF)
    DuckNoFly = Duck('NoFlying','No Flying Duck',InterNOF)

    DuckNoFly.Dflying_meth()
    DuckExtra.Dflying_meth()
    DuckNormal.Dflying_meth()


