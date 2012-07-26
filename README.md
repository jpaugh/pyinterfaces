Interfaces
==========

Adds interfaces to Python. Loosely based on either Java interfaces, or
Haskell typeclasses. This provides some informal assurances to client
code that your class or objects behave in a certain fashion.

To create an interface, subclass `Interface`, and add fill out the
`__name__` and `__interface__` fields. Also, adding comments is very
necessary, as the details of the interface are left unspecified.

- `__name__` is a pretty name for your interface
- `__interface__` is a list of attributes that implementors are required
  to support.

```python
import interfaces

class Strable(Interface):
  '''Anything that can be converted to a (pretty) string.
  To implement, define a function __str__ like so:
  def __str__(self):
    return "Pretty description of " + self.name
  '''
  __name__ = 'Strable'
  __interface__ = [ 
      '__str__',    # obj.__str__(self) returns a pretty string
    ]
```

Then, to declare that a class is Strable, we use the `@implements`
decorator:

```python
@implements(Strable)
class MyClass:
  def __init__(self, name="Fred"):
    self.name = name

  def __str__(self):
    return "A " + self.name
```

Of course, the raison d'etre of interfaces is so that you can test for
them:

```python
if implements(myobj, Strable):
  print "Foo with your " + str(myobj)
```
