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
        if num1 > num2:
            return num1
        else:
            return num2
        
    def exercise1_3(self,num1,num2,num3):
        big_num = self.big_number(num1,num2)
        if num3 > big_num:
            return (num3 ** 2) + (big_num ** 2)
        else:
            if num2 > num3 and num1 > num3:
                return (num1 ** 2) + (num2 ** 2)
            
  
            
       

    def exercise1_4(self,a,b):
        if (b > 0):
            return a + b
        else:
            return a + (-(b))
        
    def check_guess_accuracy(self,guess,radicand):
        return True if guess < radicand and abs(radicand - (guess ** 2) <= 0.01) else False

        
    def sqrt_guess(self,radicand,guess):

        if (self.check_guess_accuracy(guess,radicand)):
            return guess
        else:
            quotient = radicand  / guess
            main_guess = (quotient + guess) / 2
            return self.sqrt_guess(radicand,main_guess)
         


    def get_answer(self):
        answer =  self.exercise1_3(4,6,3)
        answer2 = self.exercise1_4(2,21)
        print(answer2)
        print(answer)
    

                                                                                                                                                                                                            
element_instance = element()
element_instance.exp_square(5)
element_instance.get_answer()
element_instance.sqrt_guess(30,4)