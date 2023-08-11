class list_parity:
    def __init__(self):
        self.list_val = None
        self.val = lambda list1,list2 : None if list1 is None and list2 is None else [list1 + [(2 * i)] for i in list2]
        self.mapped_items =  lambda items,factor : [j * factor for j in items]
        self.square_list_items_map = lambda items : [j ** 2 for j in items[0:1]] + [k ** 2 for k in items[1:]]
        

    def get_list_value(self):
        return self.list_val
    
    def even_odd_parity(self,*args):
        even_val = [i for i in args if i % 2 == 0]
        odd_val = [j for j in args if j % 2 != 0]
        return even_val,odd_val
    
    def scale_list_items(self,items,factor):
        return [] if items is None or len(items) < 1 else ([i * factor for i in items[0:1]]) + self.scale_list_items(items[1:],factor) 
        
    def scaled_list_mapped(self,items,factor):
        return self.mapped_items(items,factor)
        
            
    
    def get_mapped(self,lis,lis2):
         return self.val(lis,lis2)
    
    def square_list_items(self,items):
        return [] if items is None and len(items) < 1 else [i ** 2 for i in items[0:1]] + [i ** 2 for i in items[1:]]
    
    def get_mapped_square_items(self,items):
        return self.square_list_items_map(items)
    
    def square_list_iter(self,items):
        pass

    def iter_items(self,things,answer):
        return answer if things is None or len(things) < 1 else self.iter_items(things[1:],([i ** 2 for i in things[0:1]] + answer))

    def iter_items_corr(self,things,answer):
        return answer if things is None or len(things) < 1 else self.iter_items_corr(things[1:],(answer + ([i ** 2 for i in things[0:1]])))

    def display_proc(self,list_val):
        if list_val is None and len(list_val) < 1:
            return False
        for i in list_val:
            print(i)
        return True
        
        
            
    def display_res(self, items):
        proc = self.display_proc(items)
        return proc