"""
Name:Thomas Scola
mean.py
Problem: computes the different means of imputs
Certification of Authenticity: I certify that this is entirely my own work.

"""
import math
def main():
    def mean():
        #This is the loop for the values and terms
        n_terms = eval(input("enter the values to be entered: "))#user inputs number of terms
        total = 0
        denominator = 0
        product = 1

        #inputs
        for num in range(n_terms):
            num = eval(input("enter value: "))
            total = total + num**2
            denominator = denominator + 1/num
            product = product * num

        #calculations for all the different kinds of means
        rms_average = math.sqrt(total / n_terms)#RMS calculation
        harmony = (n_terms / denominator)#harmonic interval calculation
        geo = (product) ** (1/n_terms)#geoemtric interval calculation

        #outputs
        print(round(rms_average, 3))
        print(round (harmony, 3))
        print(round(geo, 3))
    mean()

if __name__ == '__main__':
    main()
