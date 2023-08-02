class alyssa:
    def __init__(self):
        self.max_bound = None
        self.min_bound = None
        self.resist1 = None
        self.resist2 = None
        self.x = None
        self.y = None

    def compute_par_res(self,x,y):
        self.resist1 = x
        self.resist2 = y
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
        p5 = self.create_upper_bound(x) * self.create_upper_bound(y)
        first_min   = min(p1,p2)
        sec_min = min(p3,p4)
        third_min = min(first_min,sec_min)
        final_min = min(third_min,p5)
        first_max = max(p1,p2)
        sec_max = max(p3,p4)
        th_max = max(first_max,sec_max)
        four_max = max(th_max,p5)
        val =  self.make_interval(final_min,four_max)
        print('broken down',val)
        return self.make_interval(min(p1,p2,p3,p4), max(p1,p2,p3,p4))

    def div_interv(self,x,y):
        val =  self.mult_interval(x,self.make_interval((self.create_upper_bound(y) / 1.0), (self.create_lower_bound(y)) / 1.0))
        return val if val is not 0 else -1
    
    def check_div(self,x,y):
        return "Error in division" if self.div_interv(x,y) == 0  else "Correct"

    def width_interv(self,x,y):
        if self.sub_interval(x,y) > 0:
            return sum(self.sub_interval(x,y)) / 2
        
    
    def center(self,i):
        return (self.create_lower_bound(i) + self.create_upper_bound(i)) / 2
    
    def width(self,i):
        return (self.create_upper_bound(i) - self.create_lower_bound(i)) / 2

    def make_center_width(self,c,w):
        return self.make_interval((c-w),(c + w))
    

    def make_center_percent(self):
        pass