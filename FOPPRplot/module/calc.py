class calc():
    def __init__(self):
        pass

    def normalize(self,meanlist):
        I0 = meanlist[0]
        I = meanlist[-1]
        result = (I - I0) / I0
        return result
