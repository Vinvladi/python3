# 2000 100 000 to 2003 599 999
for item in range(2000100000,2003600000,1):
    with open("output.txt", "a") as external_file:
        print("<record from=","\"",item,"\"", sep="", file=external_file)
        print("to=\"graphics/pictures/person/",item,"/portrait\"/>", sep='', file=external_file)
        external_file.close()
