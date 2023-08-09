import os
import json
from pathlib import Path
import uuid
from fractions import Fraction
from treelib import Tree
from points import line_point
from ration_class import rational
from rectangle import rectangle
from alyssa import alyssa
from hierachy import hierachy
from list_parity import list_parity

class element:

    def __init__(self):
        pass

    def exp_square(self,n):
        return ((n+1) ** 2) + ((n * 2) ** 2)
        
    def exercise1_1(self):
        sum_vals = 5 + 3 + 4
        compound_sum = ((2 * 4) + 6 - 4)  #(+ (* 2 4) (- 4 6))
        a  = 3 # (define a 3)
        b = a + 1 #(define b (+ a 1))
        comp_proc = ((a + b) + (a * b))
        if (b < a) and ((a * b) < b):
            print(b)
        else:
            print(a)

        if a == 4:
            print(6)
        elif b == 4:
            print(6 + 7 + a) 
        else:
            print(25)

        if b > a:
            res = (b * a) + 2  #(+ 2 (if (> b a) b a))
            print(res)
        
        if a > b:
            print(a) * (a + 1) # (* (cond ((> a b) a)((< a b) b)(else -1))(+ a 1))
        elif a < b:
            print(b) * (a + 1)
        else:
            print(-1) * (a + 1)
        
    def exercise1_2(self):
        numerator = (5 + 4 + (2 - (3 - (6 + (4/5)))))
        denominator = 3 * (6 -2) * (2 -7)
        quot = numerator / denominator
        print(quot)  #find predicate in the wiki  

    def square_sum_num_larger(self,num1,num2):
        return (num1 ** 2) + (num2 ** 2)

    def exercise_1_3(self,num1,num2,num3):
        if min(num1,num2,num3) is num1:
            return self.square_sum_num_larger(num2,num3)
        elif min(num1,num2,num3) is num2:
            return self.square_sum_num_larger(num1,num3)
        else:
            return self.square_sum_num_larger(num1,num2)
            

    def exercise1_4(self,a,b):
        if (b > 0):
            return a + b
        else:
            return a + (-(b))
        
    def check_guess_accuracy(self,guess,radicand):
        diff = radicand - (guess ** 2)
        return True if abs(diff) <= 0.001 else False
    
    
    def check_guess_accuracy_cube_root(self,guess,value):
        diff = value - (guess ** 3)
        return True if abs(diff) <= 0.001 else False

        
    def sqrt_guess_ex1_7(self,radicand,guess):
        main_guess = 1
        if (self.check_guess_accuracy(guess,radicand)):
            return guess
        else:
            quotient = radicand  / guess
            main_guess = (quotient + guess) / 2
            if self.check_guess_accuracy(main_guess,radicand):
                return main_guess
            else:
                quotient_2 = radicand / main_guess
                new_guess = (quotient_2 + main_guess) / 2
                return self.sqrt_guess_ex1_7(radicand,new_guess)
    
    def exercise_1_8(self,radicand,guess):
        res = 1
        if self.check_guess_accuracy_cube_root(guess,radicand):
            return guess
        
        else:
            res  = (radicand / (guess ** 2) + 2 * guess) / 3
            if self.check_guess_accuracy_cube_root(res,radicand): 
                return res
            else:
                return self.exercise_1_8(radicand,res)
        
    
    def fact_recurs(self,n):
        while n > 1:
            return n * self.fact_recurs(n - 1)
        return n

    def fact_iter(self,n):
        counter  = 1
        res = 1
        while counter < n:
            res = counter * res
            counter += 1
        return res
    
    def exercise_1_9(self,a,b):
        if a == 0:
            return b
        a -= 1 
        res = (a + b)
        res += 1
        print(res)
        return res
    
    def exercise_1_9_2(self,a,b):
        if a == 0:
            return b
        a -= 1
        b += 1
        return a + b
        
    def exercise_1_10(self,A,x,y):
        if y == 0:
           return 0 
        elif x == 0:
            return 2 * y
        elif y == 1:
            return 2
        else:
            return self.exercise_1_10(A,x-1,(self.exercise_1_10(A,x,y-1)))

    def exercise_10_fn(self,A,num,n):
        return num * n * A
    
    def fib_series(self,series_number):
        if isinstance(series_number,list) and len(series_number) > 0:
            next_val = series_number[-1] + series_number[-2]
            print(next_val)
            return next_val

        else:
            if series_number == 0 or series_number == 1:
                return series_number

    def fib_rec_next_number(self,a,b,count):
        if count == 0:
            return a
        return self.fib_rec((a+b),a,(count -  1))
        
    def fib_rec_prev_number(self,a,b,count):
        if count == 0:
            return b
        return self.fib_rec_prev_number((a+b),a,count - 1)
    
    def exer_1_11(self,n):
        if n < 3:
            return n
        else:
            return (self.exer_1_11(n-1)) + (2 * self.exer_1_11(n-2)) + (3 * self.exer_1_11(n - 3))
    
    def exer_1_11_iterative(self,n):
        if n < 3:
            return  n
        else:
            return (n -1) + (2 * (n - 2)) + (3 * (n -3))
        
    def first_denom_kind_coins(self,kind_of_coins):
        if kind_of_coins == 1:
            return 1
        elif kind_of_coins == 2:
            return 5
        elif kind_of_coins == 3:
            return 10
        elif kind_of_coins == 4:
            return 25
        elif kind_of_coins == 5:
            return 50
        
    def change_coins(self,amount,kinds_of_coins):
        if amount == 0:
            return 1
        elif amount < 0 or kinds_of_coins == 0:
            return 0
        else:
           val =  self.change_coins(amount,(kinds_of_coins -1)) + self.change_coins((amount - (self.first_denom_kind_coins(kinds_of_coins))),kinds_of_coins)
           return val

    def firs_denom(self,list_coins):
        return list_coins[0] if self.no_more(list_coins) is False else 0

    def no_more(self,list_coins):
        return True if list_coins is None or len(list_coins) < 1 else False
    
    def except_first(self,list_coins):
        return list_coins[1:] if self.no_more(list_coins) is False else list_coins
    

    def change_coins_upd(self,amount,list_of_coins):
        if amount == 0:
            return 1
        elif amount < 0 or self.no_more(list_of_coins):
            return 0
        else:
            return self.change_coins_upd(amount,self.except_first(list_of_coins)) + self.change_coins_upd((amount-self.firs_denom(list_of_coins)),list_of_coins)
            



    def pascal_recurs(self,arr_num):
        main_row = [1]
        if arr_num == 1:
            return [[1]]
        elif arr_num == 0:
            return [] 
        else:
            result = self.pascal_recurs(arr_num - 1)
            last_row = result[-1]
            for i in range(len(last_row) - 1):
                main_row.append(last_row[i]+ last_row[i +1])
            main_row += [1]
            result.append(main_row)
            return result


    def exer_1_13(self):
        pass

    def cube_x(self,x):
        return x ** 3
    
    def px(self,x):
        return (3 * x) - (4 * self.cube_x(x))
    
    def eval_sin_angle_ex_1_15(self,angle):
        if not abs(angle > 0.1):
            return angle
        val = self.px(self.eval_sin_angle_ex_1_15(angle / 3))
        return val
    
    def exp_fxn(self,b,n):
        if n == 0:
            return 1
        else:
            return b * self.exp_fxn(b,n -1)

    def exp_iter(self,b,counter,product):
        if counter == 0:
            return product
        return self.exp_iter(b,(counter - 1),(product * b))
    
    def exp_fxn_iter(self,b,n):
        return self.exp_iter(b,n,1)

    def is_even(self,n):
        return True if n % 2 == 0 else False
    
    def fast_exp(self,b,n):
        val = 1
        if n == 0:
            val = 1
            return val
        if self.is_even(n):
            val =  (self.fast_exp(b,(n / 2))) ** 2
            return val
        else:
            val = b * (self.fast_exp(b,(n-1)))
            return val
        
    def gcd(self,num1,num2):
       if num2 == 0:
           return num1
       else:
           rem = num1 % num2
           print('rem',rem)
           val = self.gcd(num2, (rem))
           print('val',val)
       return val
       
    
    def divides(self,a,b):
        return True if b % a == 0 else False

    def find_divisor(self,n,test_divisor):
        if test_divisor % 2 > n:
            return n
        elif self.divides(test_divisor,n):
            return test_divisor
        else:
            return self.find_divisor(n,(test_divisor + 1))
        
    def smallest_divisor(self,n):
        return True if self.find_divisor(n) == n else False
    

    def recursive_json(self,json_data):
       if isinstance(json_data,dict) and bool(json_data):
           for key, values in json_data.items():
               if isinstance(values,dict) and bool(values):
                   self.recursive_json(values)
               elif isinstance(values,list) and len(values) > 0:
                   for each_value in  values:
                        self.recursive_json(each_value)
               elif isinstance(values,str) or isinstance(values,int) or isinstance(values,bool):
                   print(key,'->',values)
               else:
                   print(key,'->', values)
       elif isinstance(json_data,list) and len(json_data) > 0:
           for json_value in json_data:
               self.recursive_json(json_value)
       elif isinstance(json_data,str) or isinstance(json_data,int) or isinstance(json_data,bool):
           print(json_data)
       else:
           print(json_data)
           
       
           

           
                   
                   
       
    def add_values(self,args):
        sum = 0
        sum += args
        return sum
        pass

    def mult_values(self,args):
        prod = 1
        prod *= args
        return prod
        pass

    def linear_comb(self,a,b,x,y):
        self.add_values(self.mult_values(a,x),self.mult_values(b,y))
        #pass
      
    
    def add_rational(self,num,denom):
        ration1 = rational(num,denom)
        ration2 = rational(denom,num)
        return  (ration1.get_num() * ration2.get_den()) + (ration2.get_num() * ration1.get_den()) / (ration1.get_den() * ration2.get_den())
    
    def sub_ration(self,num,denom):
        ration1 = rational(num,denom)
        ration2 = rational(denom,num)
        return  (ration1.get_num() * ration2.get_den()) - (ration2.get_num() * ration1.get_den()) / (ration1.get_den() * ration2.get_den())
        
    def mult_ration(self,num,denom):
        ration1 = rational(num,denom)
        ration2 = rational(denom,num)
        return (ration1.get_num() * ration2.get_num()) / (ration1.get_den() * ration2.get_den())

    def div_ration(self,num,denom):
        ration1 = rational(num,denom)
        ration2 = rational(denom,num)
        return (ration1.get_num() * ration2.get_den()) / (ration1.get_den() * ration2.get_num())

    def check_ration_eq(self,num,denom):
        ration1 = rational(num,denom)
        ration2 = rational(denom,num)

        val = True if (ration1.get_num() * ration2.get_den()) == (ration2.get_num() * ration1.get_den()) else False
        print('rational1', ration1.display_ration(num,denom))
        print('rational2', ration2.display_ration(denom,num))
        print('rational3_red',ration1.create_ration_red())
        return ration1.create_ration() == ration2.create_ration() if val else False
    
    def midpoint_segment(self,xpoint_start,ypoint_start,xpoint_end,ypoint_end):
        lin_po = line_point()
        val = lin_po.create_segment(xpoint_start,ypoint_start,xpoint_end,ypoint_end)
        print('midpoint',lin_po.mid_point_seg(5,5,-5,5))
        return val
        
    def rect_check(self):
        rect_check = rectangle(2,8,6,-6)
        area =  rect_check.area_rec()
        print('area',area)
        return rect_check.per_rec()

    
    
    def alysa_check(self):
        aly = alyssa()
        x = [5,6,7,2,8,9]
        y = [-1,-3,-5,-2,6,12,2]
        z = [5,1,2,-3,4,-2]
        h = [3,-2,-1,4,6,8,11]
        width1 = aly.width_interv(x,y)
        width2 = aly.width_interv(z,h)
        print('width1',width1)
        print('width2',width2)
        perc_check = aly.get_percent(20,30)
        print('perecent',perc_check)
        aprox = aly.approx_perc(20,30)
        print('aprox_check',aprox)
        val2 =  aly.width_interv(width1,width2)
        print('width_funct',val2)
        return aly.width_interv(x,y)
    
    def hierach_check(self,val):
        hier = hierachy()
        list_val = [2,3,4,7,9,10,23]
        list_two = [5,6,7,3,5,7]
        print('list lenght', hier.list_length(list_val))
        print('iter_list_lenght',hier.iter_list_length(list_val,0))
        print('add list',hier.add_list(list_val,list_two))
        print('last_pair', hier.last_pair(list_val))
        print('revers_list', hier.reverse_list(list_val))
        return hier.view_square_val(val)
    
    def check_list_par(self):
        list_values = [1,2,3,4,5]
        ls_par = list_parity()
        print('scaled_items', ls_par.scale_list_items(list_values,10))
        print('scaled_items_mapped', ls_par.scaled_list_mapped(list_values,10))
        print('mapped list', ls_par.get_mapped(list_values,list_values))
        print('square list', ls_par.square_list_items(list_values))
        print('square list map', ls_par.square_list_items_map(list_values))
        print('iter_items' , ls_par.iter_items(list_values,[]))
        print('iter_items_corr' , ls_par.iter_items_corr(list_values,[]))
        print('lambda display',ls_par.lambda_display(list_values,2))
        return ls_par.even_odd_parity(1,3,5,4,6,7,8,9,10)
    


    def get_answer(self):
        
        answer2 = self.exercise1_4(2,21)
        guess = self.sqrt_guess_ex1_7(9,2)
        cube_guess = self.exercise_1_8(216,2)
        value_num = self.exercise_1_3(2,4,5)
        fact_res = self.fact_recurs(7)
        fact_iter = self.fact_iter(6)
        inc_ex =  self.exercise_1_9(4,5)
        inc_ex2 =  self.exercise_1_9_2(4,5)
        ex_10 = self.exercise_1_10('A',1,10)
        ex_10_2 = self.exercise_1_10('A',2,4)
        ex_10_3 = self.exercise_1_10('A',3,3)
        gcd_sim = self.gcd(206,40)
        ls_par = self.check_list_par()
        print('list_par',ls_par)
        aly_chk = self.alysa_check()
        hier_chk =  self.hierach_check(3)
        coins = [50,25,10,5,1]
        print('coins_update', self.change_coins_upd(100,coins))
        print('hiera_chk',hier_chk)
        print('alyssa_check' , aly_chk)
        print('gcd',gcd_sim)
        print('rect_chk',self.rect_check())
        ex_10_fn = self.exercise_10_fn(ex_10_3,1,2)
        ex_fib_ser = self.fib_series([2,3,4])
        fib_rec_ex1_11 =  self.exer_1_11(5)
        fib_rec_ex1_11_ite = self.exer_1_11_iterative(5)
        kind_of_coins = self.change_coins(11,3)
        pasc_rec = self.pascal_recurs(3)
        fast_exp =  self.fast_exp(2,1000)
        add_rat = self.add_rational(2,3)
        seg_cls = self.midpoint_segment(5,-5,-5,5)
        print('points_mid',seg_cls)
        print('add rational',add_rat)
        sub_rat = self.sub_ration(2,3)
        print('subtract rational', sub_rat)
        mult_ration = self.mult_ration(3,2)
        print('multiply rational', mult_ration)
        div_ratio = self.div_ration(2,3)
        print('divide rational',div_ratio)
        eq_ration = self.check_ration_eq(8,12)
        print('equality rational', eq_ration)
        print('fast_exp', fast_exp)
        data =  Path("actual_response.json").read_text()
        json_val = json.loads(data)
        sin_ang = self.eval_sin_angle_ex_1_15(12.15)
        exp_rec = self.exp_fxn(2,4)
        print('exp_rec',exp_rec)
        ration = rational(2,78)
        print('rat_red',ration.create_ration_red())
        exp_iter = self.exp_fxn_iter(2,4)
        print('exp_iter',exp_iter)
        print(sin_ang)
        #rec_json =  self.recursive_json(json_val)
        print('fib_series', ex_fib_ser)
        print('change_coins', kind_of_coins)
        #print(rec_json)
        print('fib_number' , fib_rec_ex1_11)
        print('fib_number_ite' , fib_rec_ex1_11_ite)
        print('pasc_rec',pasc_rec)
        print('cube',cube_guess)
        print('ex_10',ex_10)
        print('ex_10_2',ex_10_2)
        print('ex_10_3',ex_10_3)
        print('ex_10_fn',ex_10_fn)
        print(guess)
        print(answer2)
        print('factorial',fact_res)
        print('fact_iter',fact_iter)
        print('sum_inc',inc_ex)
        print('sum_inc2',inc_ex2)
        print('res',value_num)



    

                                                                                                                                                                                                            
element_instance = element()
element_instance.exp_square(5)
element_instance.get_answer()
#element_instance.sqrt_guess_ex1_7(300,4)