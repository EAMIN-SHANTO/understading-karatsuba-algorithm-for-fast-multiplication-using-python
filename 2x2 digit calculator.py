
inp1=input("enter first row: ")
w= int(inp1[0])
x= int(inp1[1])

inp2=input("enter second row: ")
y= int(inp2[0])
z= int(inp2[1])

# firstln= ((w*y)+(w*z)+(x*y)+(x*z))

a=(w*y)
b=(w*z)
c=(x*y)
d=(x*z)

midlle = b+c


aa_result= d%10
reminder=d//10


midlle+=reminder
reminder=midlle//10
bb_result=midlle%10


a+=reminder
print(a,end="")

print(bb_result,end="")

print(aa_result,end="")
