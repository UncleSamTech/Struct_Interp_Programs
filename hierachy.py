class hierachy:
    def __init__(self):
        self.squares = [1,4,9,16,25]

    def list_ref(self,items,n):
        return items[n] if n == 0 else self.list_ref(items[1:],n-1)
    
    def get_squares(self):
        return self.squares
        
    
    def view_square_val(self,posit):
        return self.list_ref(self.get_squares(),posit)
    
    def list_length(self,items):
        return 0 if items is None or len(items) == 0 else self.list_length(items[1:]) + 1
    
    def iter_list_length(self,items,count):
        return count if items is None or len(items) == 0 else self.iter_list_length(items[1:],count + 1)
    
    def add_list(self,list1,list2):
        fin_list = []
        if list1 is None or len(list1) == 0:
            return list2
        else:
            fin_list.append(list1[0])
            fin_list.append(self.add_list(list1[1:],list2))
        return fin_list
        