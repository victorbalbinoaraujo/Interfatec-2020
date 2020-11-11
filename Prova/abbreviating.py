list_names = []
check = 0
while True:
    try:
        name = str(input())
        middle = ' '
        names = name.split(' ')
        if len(names) == 1:
            full_name = name
            check = 1
        for i in range(1, len(names) - 1):
            middle += names[i][0] + ". "
        if check == 0:
            aux = len(names) - 1
            last_name = names[aux]
            full_name = names[0] + middle + last_name
        list_names.append(full_name)
        check = 0    
    except EOFError:
        break
    
    list_names.sort()
    print(*list_names, sep='\n')