num = int(input("Enter a number:"))
for i in range(1,11):
    print(num,"X" ,i,"=",num*i)
#using concatenation
num = int(input("Enter a number:"))
for i in range(1,11):
    print(str(num)+"X" +str(i)+"="+str(num*i))
    print(f"{num}X{i}={num*i}") #using fstring