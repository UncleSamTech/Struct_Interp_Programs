from points import line_point
class rectangle():

    def __init__(self):
        #super.__init__()
        self.perimeter = None
        self.area = None
        self.length = None
        self.width = None

    def per(self,xpoint_start1,ypoint_start1,xpoint_end1,ypoint_start2):
        self.width = abs(xpoint_end1 - xpoint_start1)
        self.length = abs(ypoint_start1 - ypoint_start2)
        self.perimeter =  2 * (self.length + self.width)
        return self.perimeter


    def area(self):
        self.area =  self.width * self.length
        return self.area