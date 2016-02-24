import pqb
import unittest
from nose.plugins.attrib import attr

@attr('select')
class SelectQueryBuilderTestCase(unittest.TestCase):
    """SELECT Query Builder Test Case"""

    def test_basic_select(self):
        """Simple select"""
        expected = "SELECT * FROM V"
        result = pqb.Select().from_('V').result()
        assert result == expected

    def test_basic_select_wrong_table(self):
        """Simple select with wrong table name"""
        expected = "SELECT * FROM Va"
        result = pqb.Select().from_('V\\a').result()
        assert result == expected

        expected = "SELECT * FROM Vb"
        result = pqb.Select().from_('V#b').result()
        assert result == expected

    def test_basic_select_with_aliased_table(self):
        """Simple select with alias in table"""
        expected = "SELECT * FROM V AS a"
        result = pqb.Select().from_('V as a').result()
        assert result == expected

    def test_basic_select_with_where(self):
        """Simple select with where clause"""
        expected = "SELECT * FROM V WHERE a = 'b'"
        result = pqb.Select().from_('V').where('a', 'b').result()
        assert result == expected

    def test_basic_select_with_where_and_malformed_field(self):
        """Simple select with where clause and malformed field"""
        expected = "SELECT * FROM V WHERE ac = 'b'"
        result = pqb.Select().from_('V').where('a\\c', 'b').result()
        assert result == expected

    def test_basic_select_with_where_and_malformed_value(self):
        """Simple select with where clause and malformed value"""
        expected = "SELECT * FROM V WHERE ac = 'b\\\\'"
        result = pqb.Select().from_('V').where('a\\c', 'b\\').result()
        assert result == expected
    
    def test_basic_select_with_complex_where(self):
        """Simple select with complex where conditions"""
        expected = "SELECT * FROM V WHERE ac = 'b\\\\' AND bf = 'c'"
        result = pqb.Select().from_('V').where('a\\c', 'b\\').where('b\\f', 'c').result()
        assert result == expected
        
        expected = "SELECT * FROM V WHERE ac = 'b\\\\' OR bf = 'c'"
        result = pqb.Select().from_('V').where_or('a\\c', 'b\\').where_or('b\\f', 'c').result()

        assert result == expected

        expected = "SELECT * FROM V WHERE ac = 'b\\\\' OR bf = 'c'"
        result = pqb.Select().from_('V').where('a\\c', 'b\\').where_or('b\\f', 'c').result()

        assert result == expected

        expected = "SELECT * FROM V WHERE alpha = 'beta' AND gamma = 'delta' OR pi = 'omega'"
        result = pqb.Select().from_('V').where({
            'alpha': 'beta',
            'gamma': 'delta',
        }).where_or({
            'pi': 'omega'
        }).result()

        assert result == expected

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