import sys

T = int(sys.stdin.readline())

def GCD(A, B):
    while True:
        C = A % B
        if C == 0:
            return B
        A = B
        B = C
        
def LCM(A, B, gcd):
    return (A * B) // gcd 


for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(LCM(A, B, GCD(max(A, B), min(A, B))))