n=int(input('enter the number to be checked'))
for i in range(1,100):
    if i*i==n:
        print('perfect square')
        break
    elif(i==99):
        print('not a perfect square')