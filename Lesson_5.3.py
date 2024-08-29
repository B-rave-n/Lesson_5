import string
del_symbols = [' ']
for i in string.punctuation:
    del_symbols += i
hashtag = []
users_frase = input(print('Введи вираз, який хочеш перетворити на #хештег:' )).title()
for i in users_frase:
    hashtag += i
for i in del_symbols:
    if hashtag.count(i) > 0:
        for j in range(hashtag.count(i)):
            hashtag.remove(i)
length = len(hashtag)
# Якщо решітка теж входить в 140 символів:
while length > 139:
    length = len(hashtag)
    hashtag.pop()
print('#', sep='', end ='')
for i in hashtag:
    print(i, sep='', end ='')