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