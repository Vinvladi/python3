def past(h,m,s):
    return h*60*60*1000+m*60*1000+s*1000


past(1,2,3)
past(0,0,0)
past(8,0,0)
print(past(1,2,3),past(0,0,0),past(8,0,0))