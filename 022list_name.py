name_list = []

def addlist(name):
    for i in range(50):
        name_list.append(name)
    return print(name_list)

print(addlist(input('ditt namn: ')))
