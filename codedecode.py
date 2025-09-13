import random
import string

def code():
    takeinput=str(input("Type your message: "))
    message=takeinput.split(" ")
    result=[]
    for i in message:
        if len(i)<3:
            result.append(i[::-1])
        else:
            lettersbeg = ''.join(random.choices(string.ascii_lowercase, k=3))
            lettersend = ''.join(random.choices(string.ascii_lowercase, k=3))
            result.append(lettersbeg+i[1:]+i[0]+lettersend)

    for i in result:
        print(i,end=" ")

def decode():
    takeinput=str(input("Type your message: "))
    message=takeinput.split(" ")
    result=[]
    for i in message:
        if len(i)<3:
            result.append(i[::-1])
        else:
            dec=i[-4]+i[3:-4]
            result.append(dec)
    for i in result:
        print(i,end=" ")

def main():
    print("Welcome to Secret Message writer and translator!")
    choice=int(input("Do you want to code(1) or decode(2)?: "))

    if choice==1:
        code()
    elif choice==2:
        decode()
    else:
        print("Enter Valid Choice!")
        return 0
    
main()