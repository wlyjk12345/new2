import re
re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
test = '010 12345'    #
if re.match(r'\d{3}\s\d{3,8}$', test):  #
    print('ok')
else:
    print('failed')
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(1))
re.match(r'[^0-9]',test)
if re.match(r'[^0-9a-z]',test):          #  ^  取反
    print('ok')
else:
    print('failed')
if re.search(r'\d{3}\s\d{3,8}$', '  010 12345'):     # search只要有就行，而match必须一模一样
    print('ok')
else:
    print('failed')
# finddall  finditer spilt sub
