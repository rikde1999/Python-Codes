def appendmiddle(s1,s2):
    middle = int(len(s1)/2)
    middle1 = s1[:middle:] +s2 + s1[middle:]
    print(middle1)
appendmiddle("riik",'dey')