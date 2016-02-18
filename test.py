import pyqb

'''
s = queries.Select()
s.from_('lol', 'a') \
.where("a", 'b') \
.where_or('c', 'd') \
.where("a", 'b') \
.group_by('lol') \
.order_by('a') \
.order_by('b', 'DESC')

print (s.result(pretty=True))
'''

print (pyqb.Select().from_('V').where('a', 'b').result())
print (pyqb.Create('VERTEX').class_('V').set('a', 'b').result())
print (pyqb.Delete('VERTEX').class_('V').where('a', 'b').result())
print (pyqb.Update('V').set('a', 'b').where('a', 'b').result())

