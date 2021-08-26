a=3
def digit_sum(n):
    if n<=9:
        return n
    else:
        return digit_sum(n//10)+digit_sum(n%10)
print(digit_sum(a))


print("======\n")
print('n+(n-2)+(n-4)+....\n')
def pattern(n):
    if n<=0:
        return 0
    else:
        return pattern(n-2)+n
print(pattern(3))
