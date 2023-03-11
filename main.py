#i'm still learning about python from time to time (newbie hoobiest) so i just came up with a different approach to calculate the sequences using lists
n = int(input("how many sequences: "))
fibonacci = [0 , 1]
while n > len(fibonacci):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci)
