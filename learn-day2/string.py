# -*- coding:utf-8 -*-

name = "my name is elvis"

print(name.capitalize())
print(name.count("a"))
print(name.center(50,"-"))
print(name.endswith("is"))
print(name.expandtabs(tabsize=30))
print(name.find('name'))
print(name.format(name='elvis',year=31))
print(name.format_map({'name':'elvis','year':12}))
print('adfb123'.isalnum())
print('adfA'.isalpha())
print('1A'.isdecimal())
print('1A'.isdigit())
print('a 1A'.isidentifier())#判断是不是一个合法的标识符
print('22A'.islower())
print('33A'.isnumeric())
print('My Name is '.istitle())
print('My Name is '.isprintable())
print('My Name is '.isupper())
print(','.join(['1','2','3']))
print(name.ljust(50,'*'))
print(name.rjust(50,'*'))
print('Elvis'.lower())
print('Elvis'.upper())
print('\nElvis'.lstrip())
print('Elvis\n'.rstrip())
print('  Elvis'.strip())
p = str.maketrans("abcdef","123456")
print("elvis li".translate(p))
print('elvis li'.replace('l','L',1))
print('elvis li'.rfind("i"))
print('1+2+3+4'.split('+'))
print('1+2\n3+4'.splitlines())
print('Elvis Li'.swapcase())
print('lvis li'.title())
print('elvis li'.zfill(50))



