from hierachy import hierachy
class trees:

    def __init__(self):
        self.count = 0


    def count_leaves(self, list_val):
        if list_val is None or len(list_val) < 1:
            return 0
        elif len(list_val) == 1 or any(isinstance(i,list) for i in list_val) is False or any(isinstance(k,dict) for k in list_val):
            return 1
        elif any(isinstance(m,list) for m in list_val):
            return (len(i) for i in list_val)

        else:
            return self.count_leaves(list_val[0:1]) + self.count_leaves(list_val[1:])
        
    def drill_tree_1(self,list_val):
        if list_val is None and len(list_val) < 1:
            return 0
        return list_val[1:][1:][0][1]
    
    def drill_tree_2(self,list_val):
        if list_val is None and len(list_val) < 1:
            return 0
        return list_val[0][0]
    
    def drill_tree_3(self,list_val):
        if list_val is None and len(list_val) < 1:
            return []
        lev1_cdr = list_val[1:]
        print('level1',lev1_cdr)
        print('length_level1',len(lev1_cdr))
        lev2_cdr = lev1_cdr[1:]
        print('level2_cdr',lev2_cdr)
        lev3_cdr = lev2_cdr[1:]
        print('level_3',lev3_cdr)
        return list_val[1:][1:][1:][1:][1:]
    
    def cons_list(self,list1,list2):
        return list1 + list2
        
    def appen_list(self,list1,list2):
        app_list = []
        app_list.append(list1)
        app_list.append(list2)
        return app_list
    
    def list_both(self,list1,list2):
        list1.extend(list2)
        return list1
    


