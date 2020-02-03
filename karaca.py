def encrypt(word):
    new = ''
    for i in word:
        new = i + new
    new = new.replace('a', '*')
    new = new.replace('o', '¤')
    new = new.replace('u', '0')
    new = new.replace('å', '1')
    new = new.replace('e', '#')
    new = new.replace('i', '$')
    new = new.replace('y', '2')
    new = new.replace('ä', '3')
    new = new.replace('ö', '4')
    new = new + 'aca'
    return new

def decrypt(word):
    old = ''
    for i in word:
        old = i + old
    old = old.replace('aca','')
    old = old.replace('*', 'a')
    old = old.replace('¤', 'o')
    old = old.replace('0', 'u')
    old = old.replace('1', 'å')
    old = old.replace('#', 'e')
    old = old.replace('$', 'i')
    old = old.replace('2', 'y')
    old = old.replace('3', 'ä')
    old = old.replace('4', 'ö')
    return old

print(encrypt(input('Vad vill du kryptera? \n')))

print(decrypt(input('Vad vill du dekryptera? \n')))