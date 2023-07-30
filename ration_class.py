class rational:
    
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom
    

    def display_ration(self,num,denom):
        if num > 0 and denom > 0:
            return str(num) + '/' + str(denom)
        elif num < 0 or denom < 0:
            return str(-(abs(num))) + '/' + str(abs(denom))
        else:
            return 'invalid rational number'

    def create_ration(self):
        if self.num > 0 and self.denom > 0:
            return self.num / self.denom
        elif self.num < 0 or self.denom < 0:
            return -self.num / self.denom
        else:
            print('invalid')

    
    def gcd(self,num1,num2):
       if num2 == 0:
           return num1
       return self.gcd(num2,(num1 % num2))

    def create_ration_red(self):
        rem =  self.gcd(self.num,self.denom)
        red_num = self.num / rem
        red_den = self.denom / rem
        return self.display_ration(red_num, red_den)
        


    def get_num(self):
        return self.num
    
    def get_den(self):
        return self.denom
        

  

    
        
    