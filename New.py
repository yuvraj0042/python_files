while 1:
    x=int(raw_input("please enter an iteger:"))
    if x<0:
        x=0
        print 'negative changed to zero'
    elif x==0:
        print 'zero'
    elif x==1:
        print 'single'
    else:
        print 'more'
