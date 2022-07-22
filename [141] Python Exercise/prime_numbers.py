minimum = int(input(" Please Enter the Minimum Value: "))
maximum = int(input(" Please Enter the Maximum Value: "))

with open('prime_numbers.txt', 'w+') as f:
    for Number in range (minimum, maximum + 1):
        count = 0
        for i in range(2, (Number//2 + 1)):
            if(Number % i == 0):
                count = count + 1
                break

        if (count == 0 and Number != 1):
            f.write(''.join(" %d" %Number))
