num = int(input("Enter a natural number: "))

def natural_num(num):
    if num == 1:
        return 1 
    return num + natural_num(num - 1)

print(natural_num(num))