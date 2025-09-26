import time
a=input("enter the time(in HH:MM:SS) ")
s=list(a.split(':'))
print(s)
sec=0
if len(s)==3:
    sec=(3600*int(s[0]))+(60*int(s[1]))+(int(s[2]))
else:
    print("invalid input")
print(sec)
time.sleep(sec)
print("time is up!!!!")