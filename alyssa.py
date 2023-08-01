class alyssa:
    def __init__(self):
        self.resist1 = None
        self.resist2 = None
        self.para_equiv_res = None
        self.lower_bound_x = None
        self.upper_bound_x = None
        self.lower_bound_y = None
        self.upper_bound_y = None
        self.x = None
        self.y = None

    def compute_par_res(self):
        return 1 / ((1 / self.resist1) + (1/self.resist2))
    
    def create_bound(x,y):
        pass
    
    def make_interval(self,x,y):
        min_bound = self.lower_bound_x + self.lower_bound_y
        max_bound = self.upper_bound_x + self.upper_bound_y
        return min_bound, max_bound
    
    def mult_interval(self):
        p1 = self.lower_bound_x * self.lower_bound_y
        p2 = self.lower_bound_x * self.upper_bound_y
        p3 = self.upper_bound_x * self.lower_bound_y
        p4 = self.upper_bound_x * self.upper_bound_y

        return self.make_interval(min(p1,p2,p3,p4), max(p1,p2,p3,p4))

    def div_interv(self,x,y):
        return self.mult_interval(x,self.make_interval((self.upper_bound_y / 1.0), (self.lower_bound_y) / 1.0))


    

    def interv_arith(self):
        pass




