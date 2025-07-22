class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
num = Number(2)

print(n + num)

# n.__add__(num) it returns
# self.n + num.n
