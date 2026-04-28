def digit_root(num):
    while num > 9:
        total = 0

        for digit in str(num):
            total += int(digit)

        num = total

    return num

print(digit_root(4851))   
print(digit_root(97569))  
print(digit_root(889987)) 