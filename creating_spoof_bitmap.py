import random
for col in range(6):
    for row in range(3):
        r = random.randint(0,255)
        r = "{0:b}".format(r).zfill(8)
        g = random.randint(0,255)
        g = "{0:b}".format(g).zfill(8)
        b = random.randint(0,255)
        b = "{0:b}".format(b).zfill(8)
        print(r+g+b,end = " ")
        #print('pixel['+str(col)+','+str(row)+'] = ('+r+','+g+','+b+')',end=' ')
    print()
#print("{0:b}".format(10).zfill(8))