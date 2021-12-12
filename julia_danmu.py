c=-0.8+0.156j
for y in range(10):
    for x in range(20):
        n=(x+0.5)/5-2+((y+0.5)/2.5-2)*1j
        for z in range(26):
            if abs(n)<=2:
                n=n**2+c
                if abs(n)>2:
                    print(chr(z+65),end='')
                    break
            if z==25:
                print('A',end='')
    print()
