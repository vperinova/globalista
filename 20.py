for i in range(1,101):
    if i%15==0:
        print('bum-bac')
    elif i%3==0:
        print('bum',end=' ')
    elif i%5==0:
        print('bac',end=' ')
    else:
        print(i, end=' ')
        