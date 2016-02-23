import pqb
import unittest


class SelectQueryBuilderTestCase(unittest.TestCase):
    """SELECT Query Builder Test Case"""
    def test_basic_select(self):
        """Simple select"""
        assert pqb.Select().from_('V').result() == "SELECT * FROM V"
    def test_basic_select_wrong_table(self):
        """Simple select with wrong table name"""
        assert pqb.Select().from_('V\\a').result() == "SELECT * FROM Va"
    def test_basic_select_with_aliased_table(self):
        """Simple select with alias in table"""
        assert pqb.Select().from_('V as a').result() == "SELECT * FROM V as a"

if __name__ == '__main__':
    unittest.main()

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

print (pqb.Select().from_('V').where('a', 'b').result())
print (pqb.Create('VERTEX').class_('V').set('a', 'b').result())
print (pqb.Delete('VERTEX').class_('V').where('a', 'b').result())
print (pqb.Update('V').set('a', 'b').where('a', 'b').result())
'''