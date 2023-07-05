import os

class element:

    def __init__(self):
        pass

    def exp_square(self,n):
        f = ((n+1) ** 2) + ((n * 2) ** 2)
        print(f)
    
element_instance = element()
element_instance.exp_square(5)