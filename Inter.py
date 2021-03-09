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





