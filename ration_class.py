class rational:
    
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom
    
    def create_ration(self):
        if self.num > 0 and self.denom > 0:
            return self.num / self.denom
        elif self.num < 0 or self.denom < 0:
            return -self.num / self.denom
        else:
            print('invalid')
            

    def get_num(self):
        return self.num
    
    def get_den(self):
        return self.denom
        
    def display_ration(self):
        if self.get_num() > 0 and self.get_den() > 0:
            return str(self.get_num()) + '/' + str(self.get_den())
        elif self.get_num() < 0 or self.get_den() < 0:
            return str(-self.get_num()) + '/' + str(abs(self.get_den()))

   
        
    