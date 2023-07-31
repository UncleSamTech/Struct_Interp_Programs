class line_point:

    def __init__(self):
        self.start_segment = None
        self.end_segment = None
        self.x_point = None
        self.y_point = None

    def get_start_segment(self):
        return self.start_segment
    
    def get_end_segment(self):
        return self.end_segment
    
    def midpoint_segment(self):
        return (self.start_segment + self.end_segment) / 2
    
    def make_point(self,x_point, y_point):
        self.x_point = x_point
        self.y_point = y_point
        return self.x_point,self.y_point

    
    def get_x_point(self):
        return self.x_point
    
    def get_y_point(self):
        return self.y_point
    
    def create_segment(self,xpoint_start,ypoint_start,xpoint_end,ypoint_end):
        segments = []
        self.start_segment =  self.make_point(xpoint_start,ypoint_start)
        self.end_segment = self.make_point(xpoint_end,ypoint_end)
        segments.append(self.start_segment)
        segments.append(self.end_segment)
        return segments
    
    def mid_point_seg(self,xpoint_start,ypoint_start,xpoint_end,ypoint_end):
        segment = self.create_segment(xpoint_start,ypoint_start,xpoint_end,ypoint_end)
        sum_val = 0
        if len(segment) > 0:
            for i in segment:
                sum_val += sum(i)
            return sum_val / 2 if sum_val > 0 or sum_val < 0 else  0


    