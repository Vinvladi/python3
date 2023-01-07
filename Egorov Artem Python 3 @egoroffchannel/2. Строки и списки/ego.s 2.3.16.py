i = input()
i = i.lower().replace("a", "").replace("o", "").replace("y", "").replace("e", "").replace("u", "").replace("i", "")
i1 = ".".join(i)  # на этом этапе немного считерил подсмотрев, как это делается
i1 = "." + i1
print(i1)
