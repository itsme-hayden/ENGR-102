num = int(input('Enter a four digit integer:'))

digit1 = num // 1000
digit2 = (num % 1000) // 100
digit3 = (num % 100) // 10
digit4 = num % 10

divisor = digit1 + digit2 + digit3 + digit4

remainder = num % divisor

if remainder == 0:
    print(f"{num} is a Harshad number")
else:
    print(f"{num} is not a Harshat number")