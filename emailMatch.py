import re
print('please input your email adress')
email = input()
e = re.compile(r'^([0-9a-zA-Z\.\-]+)\@(\w+)\.([a-zA-Z]+)$')
m = e.match(email)
print('user\'s name: %s'%(m.group(1)))
print('organisation: %s'%(m.group(2)))
print('type: %s'%(m.group(3)))
