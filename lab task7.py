P=float(input("The principal amount:"))
R=float(input("the rate of interest:"))
T=float(input("The time in years:"))
A=P*(1+R/100)**T
compoundinterest=A-P
print(compoundinterest)