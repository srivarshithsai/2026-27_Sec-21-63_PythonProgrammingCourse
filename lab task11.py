#AND operator
a=int(input("enter the number1:"))
result=a>10 and a<4
print("result of",a,">10 and ",a,"<4 is",result)
#OR operator
a=int(input("enter the number2:"))
result=a>2 or a<6
print("result of",a,">2 or ",a,"<6 is",result)
#NOT operator
a=int(input("enter the number3:"))
result=not(a>9 and a<10)
print("result of ",a,">9 not ",a,"<10 is",result)