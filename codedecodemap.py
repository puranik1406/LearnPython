import random
import string

def code(i):
    # takeinput=str(input("Type your message: "))
    # message=takeinput.split(" ")
    # result=[]
    # for i in message:
    if len(i)<3:
        return (i[::-1])
    else:
        lettersbeg = ''.join(random.choices(string.ascii_lowercase, k=3))
        lettersend = ''.join(random.choices(string.ascii_lowercase, k=3))
        return (lettersbeg+i[1:]+i[0]+lettersend)

    # for i in result:
    #     print(i,end=" ")

def decode(i):
    # takeinput=str(input("Type your message: "))
    # message=takeinput.split(" ")
    # result=[]
    if len(i)<3:
        return (i[::-1])
    else:
        return(i[-4]+i[3:-4])

def main():
    print("Welcome to Secret Message writer and translator!")
    choice=int(input("Do you want to code(1) or decode(2)?: "))

    if choice==1:
        takeinput=str(input("Type your message: "))
        message=takeinput.split(" ")
        result=list(map(code,message))
        for i in result:
            print(i,end=" ")
    elif choice==2:
        takeinput=str(input("Type your message: "))
        message=takeinput.split(" ")
        result=list(map(decode,message))
        for i in result:
            print(i,end=" ")
    else:
        print("Enter Valid Choice!")
        return 0
    
main()