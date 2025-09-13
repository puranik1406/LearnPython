import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

passed=list()
print("Enter the names of the students who passed")

i=1
while(stu:=input(f"Student {i}: "))!="quit":
    passed.append(stu)
    i=i+1

for i in passed:
    speaker.Speak(f"{i} passed")

#print(dir(speaker))
