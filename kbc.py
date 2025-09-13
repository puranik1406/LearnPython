# ques={1:'What is the capital of Maharashtra?\n',2:'What is the name of the Shri Ram\'s mother?',3:'What is the name of Bali\'s brother in Ramayan?'}
# ans={1:'Mumbai',2:'Kaushalya',3:'Sugreev'}
def correct(amount):
    amount=amount+1000
    print("Correct Answer! You have won ₹",amount,"!\n")
    return amount

def wrng(wrong):
    print("Wrong Answer!Game over:(")
    wrong=True
    return wrong

qna=(('What is the capital of Maharashtra?','Mumbai'),('What is the name of the Shri Ram\'s mother?','Kaushalya'),('What is the name of Bali\'s brother in Ramayan?','Sugreev'))
choices=(['Ahmedabad','Mumbai','New Delhi','Pune'],['Kaikeyi','Sumitra','Kaushalya','Mandodari'],['Sugreev','Angad','Hanuman','Lakshman'])
print("Welcome to Kaun Banega Crorepati!\nQuestion 1 aapke screen par ye raha:")
amount=0
wrong=False
for i in range(3):
    if wrong==True:
        break
    print("Question",i+1,": ",qna[i][0])
    A=choices[i][0]
    B=choices[i][1]
    C=choices[i][2]
    D=choices[i][3]
    print("Option A:",A,"\t\t\t","Option B:",B)
    print("Option C:",C,"\t\t\t","Option D:",D)

    while True:
        ans=input(str("Enter choice(A/B/C/D): "))
        lock=input(str("Lock karein?(Y/N): "))
        if lock=='y' or lock=='Y':
            match(ans):
                case 'A'|'a':
                    if A==qna[i][1]:
                        amount=correct(amount)
                        break
                    else:
                        wrong=wrng(wrong)
                        break
                case 'B'|'b':
                    if B==qna[i][1]:
                        amount=correct(amount)
                        break
                    else:
                        wrong=wrng(wrong)
                        break
                case 'C'|'c':
                    if C==qna[i][1]:
                        amount=correct(amount)
                        break
                    else:
                        wrong=wrng(wrong)
                        break
                case 'D'|'d':
                    if D==qna[i][1]:
                        amount=correct(amount)
                        break
                    else:
                        wrong=wrng(wrong)
                        break
                case _:
                    print("Enter Valid Choice!")
                    continue
        elif lock=='n' or lock=='N':
            continue
        else:
            print("You've pressed an invalid key!")

print("You've won ₹",amount,"!")