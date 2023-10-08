

""""""""""
a = 77 * '1'
while '111' in a:
    if '111' in a:
        a = a.replace('111', '2', 1)
        a = a.replace('222', '11', 1)
print(a)
"""""""""""

a = '1' + 100 * '9'
while ('19' in a) or ('299' in a) or ('3999' in a):
    if '19' in a:
        a = a.replace('19', '2', 1)
    if '299' in a:
        a = a.replace('299', '3', 1)
    if '3999' in a:
        a = a.replace('3999', '1', 1)
print(a)
