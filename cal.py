def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1//num2


val=int((input("Enter which operation do you want to do\n\t\t\t 1.adding \n\t\t\t2. substract \n\t\t\t3. Multiply \n\t\t\t4.  division \n enter operation ")))
num1=int((input("Enter num1 value \t\t")))
num2=int((input("Enter num1 value \t\t")))
match val:
    case 1:
        print("sum of two num",add(num1,num2))
    case 2:
        print("sub of two num",sub(num1,num2))
    case 3:
        print("mul of two num", mul(num1, num2))
    case 4:
        print("div of two num", div(num1, num2))
    case 5:
        print("Exit")


