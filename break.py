spam = 0
while spam < 10:
    print(spam)
    spam = spam + 1
    if spam == 4:
        print('spam reached 4 which we dont want')
        break