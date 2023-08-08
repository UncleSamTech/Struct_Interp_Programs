class list_parity:
    def __init__(self):
        self.list_val = None

    def get_list_value(self):
        return self.list_val
    
    def even_odd_parity(self,*args):
        list1 = []
        list2 = []
        for i in args:
            if i % 2 == 0:
                list1.append(i)
            else:
                list2.append(i)
        return list1,list2
    
    def scale_list_items(self,items,factor):
        return [] if items is None or len(items) < 1 else ([i * factor for i in items[0:1]]) + self.scale_list_items(items[1:],factor) 
        