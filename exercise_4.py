x = int(input())
n = ""
 
while x > 0:
    y = str(x % 2)
    n = y + n
    x = int(x / 2)
 
print (n)