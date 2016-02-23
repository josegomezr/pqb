# PQB

Python Query Builder

## Example

Hacer funcionar este fragmento de codigo.

```python
import pqb
print (pqb.Select().from_('V').where('a', 'b').result())
# SELECT * FROM V WHERE a = 'b'
```

## @TODO
- [ ] awesome description
- [ ] implement sql *flavors*
- [ ] unit tests
