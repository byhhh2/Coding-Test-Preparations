import sys

X = sys.stdin.readline().rstrip()
cnt = 0

def XtoY(X):
    global cnt

    cnt += 1
    Y = 0

    for x in X:
        Y += int(x)
    
    if len(str(Y)) > 1:
            XtoY(str(Y))
    else:
        print(cnt)
        print("YES") if Y % 3 == 0 else print("NO")

if len(X) == 1:
    print(0)
    if int(X) % 3 == 0:
        print("YES")
    else:
        print("NO")
    exit(0)
    
XtoY(X)