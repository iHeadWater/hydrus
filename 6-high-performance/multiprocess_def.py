def countdown(n):
    while n>0:
        n -= 1
        
def cpu_bound(number):
    return sum(i * i for i in range(number))