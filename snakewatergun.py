import random

def swg():
    matrix=[['tie','user','comp'],['comp','tie','user'],['user','comp','tie']]
    user=int(input("Enter 1 for Snake\n2 for Water\n3 for Gun:\n"))
    computer=random.randint(1,3)
    print(f"Computer chose {computer}")
    if matrix[user-1][computer-1]=='user':
        print("Point goes to you!")
        return 1
    elif matrix[user-1][computer-1]=='comp':
        print("Point goes to computer!")
        return 0
    else:
        return -1



def main():
    print("Let's play Snake Water Gun!\nRules: Snake drinks Water,Gun drowns in Water and Snake is killed by Gun")
    points=int(input("Enter number of points u wanna play for: "))
    pts1=0
    pts2=0
    while True:
        if pts1==points or pts2==points:
            break
        res=swg()
        if res==1:
            pts1=pts1+1
        elif res==0:
            pts2=pts2+1
        else:
            print("TIE!")
        
        print(f"Player={pts1}\nComputer={pts2}")

    if pts1>pts2:
        print("YOU WON!")
    elif pts2>pts1:
        print("YOU LOST:(")
    else:
        print("TIE!!")

main()