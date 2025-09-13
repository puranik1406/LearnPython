import os

# os.rename("OOPs/clutter/file.txt","OOPs/clutter/ishita.txt")

files=os.listdir("OOPs/clutter")

i=1
for file in files:
    if ".png" in file:
        os.rename(f"OOPs/clutter/{file}",f"OOPs/clutter/{i}.png")
        i=i+1