import os

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
            print(res)
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
            pass
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
            while n >= 3:
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
        
    def change_coins(self,cc,amount,kinds_of_coins):
        if amount == 0:
            return 1
        elif amount < 0 or kinds_of_coins == 0:
            return 0
        else:
           return self.change_coins(cc,amount,(kinds_of_coins -1)) + self.change_coins(cc,(amount - (self.first_denom_kind_coins(kinds_of_coins))),kinds_of_coins)

  
        

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
        ex_10_fn = self.exercise_10_fn(ex_10_3,1,2)
        ex_fib_ser = self.fib_series([2,3,4])
        fib_rec_ex1_11 =  self.exer_1_11(5)
        fib_rec_ex1_11_ite = self.exer_1_11_iterative(5)
        kind_of_coins = self.change_coins(2,100,3)
        
        print('fib_series', ex_fib_ser)
        print('change_coins', kind_of_coins)
        print('fib_number' , fib_rec_ex1_11)
        print('fib_number_ite' , fib_rec_ex1_11_ite)
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