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

    def big_number(self,num1,num2):
        return max(num1,num2)
        
    def exercise1_3(self,num1,num2,num3):
        big_num = self.big_number(num1,num2)
        if num3 > big_num:
            return (num3 ** 2) + (big_num ** 2)
        else:
            if max(num2,num3) == num2 and max(num1 , num3) == num1:
                return (num1 ** 2) + (num2 ** 2)
            
  
            
       

    def exercise1_4(self,a,b):
        if (b > 0):
            return a + b
        else:
            return a + (-(b))
        
    def check_guess_accuracy(self,guess,radicand):
        diff = radicand - (guess ** 2)
        return True if abs(diff) <= 0.001 else False
    
    def check_better_aprox(self,x,y):
        return (x / (y ** 2) + 2 * y) / 3
    
    def check_guess_accuracy_cube_root(self,guess,value):
        diff = value - (guess ** 3)
        print('diff_cube',diff)
        print('abs diff cube', abs(diff))
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
        main_guess = 1
        if self.check_guess_accuracy_cube_root(guess,radicand):
        #and abs(guess - self.check_better_aprox(radicand,guess) <= 0.001):
            return guess
        
        else:
            quotient = radicand / guess
            main_guess  = (quotient + guess) / 2
            if self.check_guess_accuracy_cube_root(main_guess,radicand): 
            #and abs(guess - self.check_better_aprox(radicand,main_guess) <= 0.001):
                return main_guess
            else:
                quotient2 = radicand / main_guess
                print('quotient2', quotient2)
                new_guess = (quotient2 + main_guess) / 2
                return self.exercise_1_8(radicand,new_guess)
                #print('new guess cube', new_guess)
                #return new_guess
        
            
        
         


    def get_answer(self):
        answer =  self.exercise1_3(4,6,3)
        answer2 = self.exercise1_4(2,21)
        guess = self.sqrt_guess_ex1_7(9,2)
        cube_guess = self.exercise_1_8(125,2)
        print(cube_guess)
        print(guess)
        print(answer2)
        print(answer)
    

                                                                                                                                                                                                            
element_instance = element()
element_instance.exp_square(5)
element_instance.get_answer()
#element_instance.sqrt_guess_ex1_7(300,4)