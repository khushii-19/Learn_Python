# . Write a program to print multiplication table of n using for loops in reversed
# order.

n = int(input("Enter a number : "))
for i in range(10,0,-1):
    print(f"{n}X{i}= {n*i}")

    # here 10 is start value , 0 is end value because we want to print till 1, -1 because in reverse order decrease
