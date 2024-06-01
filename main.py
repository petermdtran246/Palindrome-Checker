def Reverse(n):
    rev = 0
    m = n
    while n > 0:
        r = n % 10
        n = n // 10
        rev = rev*10+r
    if rev == m:
        print('palindrome')
    else:
        print('not a palindrome')

n = int(input('Enter n: '))
Reverse(n)