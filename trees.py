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
    
    def deep_rev_list(self,deep_list):
        rev_list = []
        if len(deep_list) == 0 or len(deep_list) == 1:
            return rev_list
        else:
            for i in deep_list:
                if isinstance(i,list):
                    rev_list.append(i[-1:] + self.deep_rev_list(i[:-1]))
                else:
                    rev_list.append(i)
                return rev_list
            val = deep_list[-1:] + self.deep_rev_list(deep_list[:-1])
            rev_list.append(val)
            return rev_list
         


    def fringe(self,deep_lis):
        final_list = []
        if isinstance(deep_lis,list) and len(deep_lis) == 0 or len(deep_lis) == 1:
            return deep_lis
        def extr_deep_lis(deep_lis):
            for i in deep_lis:
                if isinstance(i,list):
                    extr_deep_lis(i)
                else:
                    final_list.append(i)
            return final_list
        return extr_deep_lis(deep_lis)
    
    def make_mobile(self,left,right):
        branch_list = []
        branch_list.append(left)
        branch_list.append(right)
        return branch_list
    
    def make_branch(self,lenght,structure):
        branch_list = []
        if lenght != None or structure != None or len(structure) < 1:
            branch_list.append(lenght,structure)
        return branch_list

    def get_left_branch(self,branch_list):
        return branch_list[0] if isinstance(branch_list,list) and len(branch_list) > 0 else 0

    def get_right_branch(self,branch_list):
        return branch_list[1] if isinstance(branch_list,list) and len(branch_list) > 1 else 0 
    
    def get_branch_length(self,branch_list):
        return branch_list[0] if isinstance(branch_list,list) and len(branch_list) >= 0 else 0
    
    def get_branch_struct(self,branch_list):
        return branch_list[1:] if isinstance(branch_list,list) and len(branch_list) > 1 else []
    
    def test_mobile_branch(self,list_val):
        list_struct = list_val[1:][0] if isinstance(list_val,list) and len(list_val) >= 1 else []
        left_branch = self.get_left_branch(list_struct)
        right_branch = self.get_right_branch(list_struct)
        branch_lenght = list_val[0] if isinstance(list_val,list) and len(list_val) >= 0 else 0
        branch_structure = list_val[1:] if isinstance(list_val,list) and len(list_val) >= 0 else []
        return left_branch, right_branch , branch_lenght, branch_structure
    
    def total_weight(self,mobile_br):
        return sum(mobile_br) if isinstance(mobile_br,list) and len(mobile_br) > 0 else mobile_br
    
    def test_binary_mobile(self,list_mobile):
        if list_mobile is None or len(list_mobile) <= 1:
            return False
        else:
            mobile_struct = list_mobile[1:][0]
            return True if list_mobile[0] * mobile_struct[0] == list_mobile[0] * mobile_struct[1] else False
        
    def scale_tree(self,tree_val,factor):
        new_scaled_tree = []
        if tree_val is None or len(tree_val) == 1 or len(tree_val) == 0:
            return tree_val
        def sc_tr(tr_ls,fact):
            for i in tr_ls:
                if isinstance(i,list):
                    new_scaled_tree.append(i * fact)
                else:
                    new_scaled_tree.append(sc_tr(tr_ls[0:1],fact) + sc_tr(tr_ls[1:],fact))
            return new_scaled_tree
        return sc_tr(tree_val,factor)

                
    
