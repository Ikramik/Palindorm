x= input ("your word is ")
x= str(x)
a= len(x)
b= True
for i in range (0, a):
    if (x[i]== x[a-i-1]):
        b= True
    else:
        b= False
if b == True :
    print('your word is a palindrom')
else :
    print('your word is not a palindrom')



