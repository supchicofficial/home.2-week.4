#1
# with open("hello.txt","w") as file:
#     file.write("Salom jahon")

#2
# with open("notes.txt","r") as file:
#     print(file.read())

#3
# with open("notes.txt","r") as file:
#     for i in file:
#         print(i.strip())

#4
# cnt=0
# with open("notes.txt","r") as file:
#     a=file.readlines()
#     for i in a:
#         cnt+=1
#     print(cnt)

#5
# with open("notes.txt","a") as file:
#     file.write("\norange")

#6
# with open("name.txt","w") as file:
#     name=["Ali","Vali","Guli"]
#     for i in name:
#         file.write(f"{i}\n")

#7
# with open("text.txt","r") as file:
#     text=file.read()
#     a=text.split()
#     print(len(a))

#8
# cnt=0
# with open("text.txt","r") as file:
#     for i in file.read().replace(" ", ""):
#         cnt+=1
#     print(cnt)

#9
# with open("number.txt","r") as file:
#     a=file.read().split()
#     for i in range(len(a)):
#         a[i]=int(a[i])
#     print(sum(a))

#10
# with open("number.txt","r") as file:
#     a=file.read().split()
#     for i in range(len(a)):
#         a[i]=int(a[i])
#     print(max(a))

#11
# with open("source.txt","r") as file:
#     a=file.read()
# with open("copy.txt","w") as f:
#     f.write(a)

#12
# sum = 0
# with open("notes.txt","r") as file:
#     a = file.readlines()
#     for i in a:
#         i = i.split()
#         sum+=1
#         print(f'{sum}:',*i)

#13
# with open("text.txt","r") as file:
#     a=file.read()
# print(a.count("python"))

#14
# with open("text.txt","r") as file:
#     a=file.read()
#     lines=[lines.rstrip("\n") for i in file]
# print(max(lines, key=len))