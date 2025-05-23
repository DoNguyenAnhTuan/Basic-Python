n=int(input("nhap n"))
a=[ ]
for i in range(n):
                print('a[', i, ']')
                x=int(input("nhap x"))
                a.append(x)
print(a)
for i in range(len(a)):
                for j in range(i+1,len(a)):
                                if(a[ i ] > a[ j ]):
                                                b=a[ i ]
                                                a[ i ]=a[ j ]
                                                a[ j ]=b
                                                
print(a)
































