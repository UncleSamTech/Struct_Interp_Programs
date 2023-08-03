class hierachy:
    def __init__(self):
        self.squares = [1,4,9,16,25]
        pass

    def list_ref(self,items,n):
        return items[n] if n == 0 else self.list_ref(items[1:],n-1)
    
    def get_squares(self):
        return self.squares
        
    
    def view_square_val(self,posit):
        return self.list_ref(self.get_squares(),posit)