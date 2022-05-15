#Q1
char=str("python is a case sensitive language")
print(len(char))
print(char[::-1])
charac=str()
charac=char[10:26]
print(charac)
newchar=char[:12]+'object oriented language'+char[26:]
print(newchar)
index=char.find('a')
print(index)
space=char.replace(" ","")
print(space)
#Q2
student=['Aditya Chhibber','21102041','Civil','9.9']
print("Hey,",student[0],"Here!")
print("My SID is",student[1])
print("I am from",student[2],"department and my CGPA is",student[3])
#Q3
a=int(56)
b=int(10)
print("a&b=",a&b)
print("a|b",a|b)
print("a^b",a^b)
print("left shift a(2 bit)=",a<<2)
print("left shift b(2 bit)=",b<<2)
print("right shift a(2 bit)=",a>>2)
print("right shift b(4 bit)=",b>>4)
#Q4
print("Please Enter a string :")
char = str(input())
x = char.find('name')
if x == -1 :
    print("No")
else :
    print("Yes")
#Q5
    
a=int(input("Please enter the length of side 1:"))
b=int(input("Please enter the length of side 2:"))
c=int(input("Please enter the length of side 3:"))
while((a+b)>c) and ((a+c)>b) and ((b+c)<a):
    print("Yes")
    break
while((a+b)<c) or ((a+c)<c) or ((b+c)<a):
    print("No")
    break
#Q6
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
num=a^b
count=0
while (num!=0):
  num=num&(num-1)
  count+1
print("Number of bits needed to be flipped to convert a to b is:",count)