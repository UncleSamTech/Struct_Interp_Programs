from points import line_point
class rectangle():

    def __init__(self,xpoint_end1,xpoint_start1,ypoint_start1,ypoint_start2):
        #super.__init__()
        self.perimeter = None
        self.area = None
        self.width = abs(xpoint_end1 - xpoint_start1)
        self.length = abs(ypoint_start1 - ypoint_start2)

    def per_rec(self):        
        print('per_leng_wid',self.length, 'width', self.width)
        return  2 * (self.length + self.width)

    def area_rec(self):
        print('area_leng_wid',self.length, 'width', self.width)
        return self.width * self.length