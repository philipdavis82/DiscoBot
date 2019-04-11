import numpy as np

class dice_commander():
    def __init__(self):
        self.commands = {
            "all":self.combine_dice,
            "sep":self.seperate_dice,
            "last":self.return_last
        }
    def combine_dice(self,dice,amount,*args,**kwargs):
        self.args = [dice,amount]
        self.last = self.combine_dice
        self.roll = np.random.randint(1,dice,amount)
        return str(self.roll.sum())

    def seperate_dice(self,dice,amount,*args,**kwargs):
        self.args = [dice,amount]
        self.last = self.seperate_dice
        self.roll = np.random.randint(1,dice,amount)
        return str(list(self.roll))

    def return_last(self,*args,**kwargs):
        return self.last(*self.args)