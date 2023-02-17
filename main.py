def main():
    x=int(input("How many fibonacci sequences you want me to write?: "))
    a, b, c = 1,0,0
    if x <=0:
        print("Enter a positive Interger!")
        main()
    for d in range(0,x):
        print(c, end=" ")
        c = a + b
        a = b
        b = c
main()
