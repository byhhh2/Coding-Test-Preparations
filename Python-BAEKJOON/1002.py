import sys

T = int(sys.stdin.readline())

for i in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, sys.stdin.readline().split())
    r_12 = (abs(x_1 - x_2) ** 2) + (abs(y_1 - y_2) ** 2)

    if r_12 > ((r_1 + r_2) ** 2) or (r_12 == 0 and r_1 != r_2) or (r_12 < (max(r_1, r_2) - min(r_1, r_2)) ** 2): # 둘이 안만남 
        print(0)
    elif r_12 == 0 and r_1 == r_2: # 무한대
        print(-1)
    elif r_12 == (r_1 + r_2) ** 2 or (r_12 == (max(r_1, r_2) - min(r_1, r_2)) ** 2): # 한 점 
        print(1)
    else: # 두 점 
        print(2)
    
    