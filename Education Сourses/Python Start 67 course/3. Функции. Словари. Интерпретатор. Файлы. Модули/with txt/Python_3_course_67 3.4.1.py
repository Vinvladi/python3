with open('dataset_3363_2.txt') as inf:
    s1 =inf.readline().strip()
good_list = []
c = ''
for i in s1:
    if i.isalpha() == True:
        good_list.append(c)
        c = ''
        good_list.append(i)
    else:
        c = c + i
good_list.append(c)
del good_list[0]
# print(good_list)
d = []
for i in range(0, len(good_list)-1,2):
    k = good_list[i]*int(good_list[i+1])
    d.append(k)
# print(d)
l = ""
for i in d:
    l += i
# print(l)
with open("output.txt", "w") as ouf:
    ouf.write(l)
