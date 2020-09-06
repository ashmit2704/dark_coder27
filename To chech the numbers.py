try:
    num = float(input("Enter a number : "))
    def real_nums(x):
        if x > 0:
            return "The number is POSITIVE"
        elif x == 0:
            return "The number is ZERO"
        elif x < 0:
            return "The number is NEGATIVE"
        else:
            return "Enter a valid number!"
    def even_or_odd(x):
        if x%2 == 0:
            if x == 0:
                return "Zero cannot be either positive or negative."
            else:
                return "The number is EVEN."
        elif x%2 != 0:
            return "The number is ODD."
        else:
            return "Enter a valid number!"
    x,y = real_nums(num), even_or_odd(num)
    print(x,y,sep=' & ')
except:
    print("Enter a valid number!")



