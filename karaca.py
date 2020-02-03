def encrypt(word):
    new = ''
    for i in word:
        new = i + new
    new = new.replace('a', '0')
    new = new.replace('e', '1')
    new = new.replace('o', '2')
    new = new.replace('u', '3')
    new = new + 'aca'
    return new

def decrypt(word):
    old = ''
    for i in word:
        old = i + old
    old = old.replace('aca','')
    old = old.replace('0', 'a')
    old = old.replace('1', 'e')
    old = old.replace('2', 'o')
    old = old.replace('3', 'u')
    return old

print(encrypt(input('Vad vill du kryptera? ')))

print(decrypt(input('Vad vill du dekryptera? ')))