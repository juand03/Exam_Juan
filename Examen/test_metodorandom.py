import string

generador=string.ascii_letters

List=[]
for i in range(len(generador)):
    result=""
    for palabra in range(0,len(generador)):
        if i<palabra:
            result+=" "
        else:
            result+=generador[palabra]
    List.append(result)

    print(result)

for i in range(len(List)-1,0):
    print(List[i-1])


