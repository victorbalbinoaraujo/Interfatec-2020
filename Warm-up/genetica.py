x = int(input())
string = str(input())
check = 0
for i in range(len(string)-x+1):
    p = string[i:x + i]
    r = p[::-1]
    if p == r:
        check = 1

if check == 1:
    print("S")
else:
    print("N")
