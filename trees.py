from hierachy import hierachy
import operator

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
        if tree_val is None or len(tree_val) == 0:
            return []
        def sc_tr(tr_ls,fact):
            for i in tr_ls:
                if not isinstance(tr_ls,list) or len(tr_ls) == 1:
                    new_scaled_tree.append(i * fact)
                else:
                    new_scaled_tree.append(sc_tr(tr_ls[0:1],fact) + sc_tr(tr_ls[1:],fact))
            return new_scaled_tree
        return sc_tr(tree_val,factor)

                
    def scale_tree_map(self,tree_list,factor):
        map_scaled_tree = []
        if tree_list is None or len(tree_list) == 0:
            return []
        def map_scale_tree_list(tr_list,factor):
            for i in tr_list:
                if not isinstance(i,list):
                    map_scaled_tree.append(i * factor)
                else:
                    map_scaled_tree.append(map_scale_tree_list(tr_list[0:1],factor) + map_scale_tree_list(tr_list[1:]))
            return map_scaled_tree
        return map_scale_tree_list(tree_list,factor)
     
    def square_tree(self,tree_list):
        if tree_list is None or len(tree_list) == 0:
            return []
        else:
            return [i ** 2 for i in tree_list[0:1]] + [j ** 2 for j in tree_list[1:]]
        
    def square_tree_rec(self,tree_list):
        squared_list = []
        if tree_list is None or len(tree_list) == 0 or len(tree_list) == 1:
            return tree_list
        def sq_tr_ls_rec(tree_lis):
            for i in tree_lis:
                if not isinstance(i,list):
                    squared_list.append(i ** 2)
                else:
                    squared_list.append(sq_tr_ls_rec(tree_lis[0:1]) + sq_tr_ls_rec(tree_lis[1:]))
            return squared_list
        return sq_tr_ls_rec(tree_list)

        
    def sum_odd_squares(self,tree_list):
        new_tree_list = []
        if tree_list is None or len(tree_list) < 1:
            return []
        for i in tree_list:
            if i % 2 != 0  and not isinstance(i,list):
                 new_tree_list.append(i ** 2)
                 #return [i ** 2]
        new_tree_list.append(tree_list[0:1] + self.sum_odd_squares(tree_list[1:]))
        return new_tree_list
    

    def predicate(self,list_val):
        odd_val = []
        if list_val is None or len(list_val) < 1:
            return odd_val
        else:
            for i in list_val:
                if i % 2 != 0:
                    odd_val.append(i)
            return odd_val

    def filter_pred(self,seq_list):
        predicate = self.predicate(seq_list)
        new_list = []
        if seq_list is None or len(seq_list) < 1:
            new_list.append(seq_list)
        else:
             [new_list.append(i) for i in predicate if i in seq_list[0:1]]
             
        def fil_pred_inner(predic,list2):
            predic = predicate
            for i in predic:
                if i in list2[1:]:
                   new_list.append(i)
            return new_list
        return fil_pred_inner(predicate,seq_list)
    
    def decide_opp(self,opp):
        opps = {"+":operator.add, "-":operator.sub,"*":operator.mul, "/":operator.truediv}
        if opp is None:
            return None
        match  opp:
            case "add":
                return opps["+"]
            case "subtract":
                return opps["-"]
            case "multiply":
                return opps["*"]
            case "divide":
                return opps["/"]
        
    def accumulate(self,op,initial,sequence):
        resp = []
        if len(sequence) == 0:
                return initial
        elif len(sequence) == 1 and [isinstance(i,list) is False for i in sequence]:
            return sequence[0] 
        val = self.decide_opp(op)
        for i in sequence[0:1]:
            resp.append(i * initial)
        fin_val = self.accumulate(op,initial,sequence[1:])
        return fin_val
    
    def enumerate_interval(self,low,high):
        new_enum = []
        if low > high:
            return []
        else:
            new_enum.append(low) 
            new_enum.extend(self.enumerate_interval(low + 1, high))
        return new_enum
    
    def enumerate_tree(self,tree_list):
        new_list = []
        if tree_list is None and len(tree_list) < 1:
            return tree_list
        def enum_tree_int(tree_list_int):
            if len(tree_list_int) == 0 or len(tree_list_int) == 1 and (isinstance(i,list) is False for i in tree_list_int):
                return tree_list_int
            for i in tree_list_int:
                if not isinstance(i,list):
                    new_list.append(i)
                else:
                   enum_tree_int(i)
            return new_list
        return enum_tree_int(tree_list)
    
    def sum_odd_sq_enc(self,tree_list):
        operator_val = self.decide_opp("add")
        enum_tree_list = self.enumerate_tree(tree_list)
        print('enum_tree_list',enum_tree_list)
        filtered_seq = self.filter_pred(enum_tree_list)
        print('filtered_sequence',filtered_seq)
        mapped_square = self.sum_odd_squares(filtered_seq)
        print('mapped square', mapped_square)
        val  = self.accumulate(operator_val,1,mapped_square)
        
        return val
    
    def filt_even(self,list_num):
        even_list = []
        if list_num is None or len(list_num) < 1:
            return []
        else:
            for i in list_num:
                if i % 2 == 0:
                    even_list.append(i)
            print('even_list',even_list)
            return even_list  
          
    def even_fibs(self,n):
        accum_list = []
        fib_list = []
        if n is None or n < 1:
            return []
        def even_inter_fibs(n):
            for i in range(0,n):
                accum_list.append(i)
            for i  in accum_list:
                if i == 0 or i == 1:
                    fib_list.append(i)
                else:
                    fib_list.append(accum_list[i-1] + accum_list[i - 2])
            return self.filt_even(fib_list)
        return even_inter_fibs(n)
    

    def list_fib_squares(self,n):
        if n is None or n < 1:
            return []
        map_sq = [self.sum_odd_squares(self.even_fibs(i)) for i in range(0,n)]
        print('map_even_fib',map_sq)
        #val =  self.accumulate("add",None,self.even_fibs(n))
        return map_sq
                
    
    def prod_squ_odd_elements(self,sequence):
        init = 1
        filterd_odd = self.filter_pred(sequence)
        mapped_sqq = self.square_tree_rec(filterd_odd)
        for i in mapped_sqq:
            init *= i
        return init
        
        