class list_parity:
    def __init__(self):
        self.list_val = None
        self.val = lambda list1,list2 : None if list1 is None and list2 is None else [list1 + [(2 * i)] for i in list2]

    def get_list_value(self):
        return self.list_val
    
    def even_odd_parity(self,*args):
        even_val = [i for i in args if i % 2 == 0]
        odd_val = [j for j in args if j % 2 != 0]
        return even_val,odd_val
    
    def scale_list_items(self,items,factor):
        return [] if items is None or len(items) < 1 else ([i * factor for i in items[0:1]]) + self.scale_list_items(items[1:],factor) 
        
    def map_list(self):
            val = lambda list1,list2 : None if list1 is None and list2 is None else [list1 + [(2 * i)] for i in list2]
            return val
            
    
    def get_mapped(self,lis,lis2):
         return self.val(lis,lis2)