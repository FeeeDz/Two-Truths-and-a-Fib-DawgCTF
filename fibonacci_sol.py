from pwn import *

def controllo(n):
    c=0
    a=1
    b=1
    if n==0 or n==1:
        print("Yes")
    else:
        while c<n:
            c=a+b
            b=a
            a=c
        if c==n:
            return True
        else:
            return False

r = remote("umbccd.io", 6000)

for i in range(0,100):
    r.recvuntil("[")
    numeri = []
    numeri = r.recvline().split()
    numeri[0] = numeri[0][:-1]
    numeri[1] = numeri[1][:-1]
    numeri[2] = numeri[2][:-1]
    for i in range(0,3):
        if controllo(int(numeri[i])) == True:
            r.sendline(bytes(numeri[i]))
        else:
            continue

r.interactive()

# flag ---> DawgCTF{jU$T_l1k3_w3lc0me_w33k}