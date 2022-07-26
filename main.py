def main():
    nsequence = int(input("Enter how many Fibonacci sequences to calculate : "))
    x,y = 0,1
    count = 0
    if nsequence <=0:
        print("Enter a positive Interger!")
        main()
    else:
        while nsequence > count :
            print(x)
            f = x + y
            y = x
            x = f
            count += 1
        print("Goodbye!")
main()
