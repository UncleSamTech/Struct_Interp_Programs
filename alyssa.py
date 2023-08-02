class alyssa:
    def __init__(self):
        self.max_bound = None
        self.min_bound = None
        self.x = None
        self.y = None

    def compute_par_res(self):
        return 1 / ((1 / self.resist1) + (1/self.resist2))
    
    def create_lower_bound(self,val):
        return min(val) if isinstance(val,list) else val
        
    def create_upper_bound(self,val):
        return max(val) if isinstance(val,list) or isinstance(val,tuple) or isinstance(val,dict) else val
    
    def make_interval(self,x,y):
        self.min_bound = self.create_lower_bound(x) + self.create_upper_bound(y)
        self.max_bound = self.create_upper_bound(x) + self.create_lower_bound(y)
        return self.min_bound, self.max_bound
    
    def get_upper_bound(self,a,b):
        return max(a,b)
    
    def get_lower_bound(self,a,b):
        return min(a,b)
    
    def sub_interval(self,x,y):
        min_inter = self.create_upper_bound(y) -  self.create_lower_bound(x)
        max_inter = self.create_upper_bound(x) - self.create_lower_bound(y)
        return min_inter,max_inter
    
    def mult_interval(self,x,y):
        p1 = self.create_lower_bound(x) * self.create_lower_bound(y)
        p2 = self.create_lower_bound(x) * self.create_upper_bound(y)
        p3 = self.create_upper_bound(x) * self.create_lower_bound(y)
        p4 = self.create_upper_bound(x) * self.create_lower_bound(y)

        return self.make_interval(min(p1,p2,p3,p4), max(p1,p2,p3,p4))

    def div_interv(self,x,y):
        return self.mult_interval(x,self.make_interval((self.create_upper_bound(y) / 1.0), (self.create_lower_bound(y)) / 1.0))

    def width_interv(self,x,y):
        return sum(self.sub_interval(x,y)) / 2
        




