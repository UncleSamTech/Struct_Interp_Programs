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


    def get_answer(self):
        
        answer2 = self.exercise1_4(2,21)
        guess = self.sqrt_guess_ex1_7(9,2)
        cube_guess = self.exercise_1_8(216,2)
        value_num = self.exercise_1_3(2,4,5)
        fact_res = self.fact_recurs(6)
        print('cube',cube_guess)
        print(guess)
        print(answer2)
        print('factorial',fact_res)
        print('res',value_num)


    

                                                                                                                                                                                                            
element_instance = element()
element_instance.exp_square(5)
element_instance.get_answer()
#element_instance.sqrt_guess_ex1_7(300,4)