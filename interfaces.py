'''
Interface system. This is inspired by Haskell's typeclass instances

Interfaces are subclasses of Interface.

To declare that a class supports an interface use
@implementing(interface), where interface is an Interface. Multiple
interfaces can be specified: @implementing(i1, i2, ...)

To check whether a given class or object implements an interface, use
implements(obj, interface)
'''


class ImplementError(TypeError): pass

class Interface(object): pass


def implementing(*impl_list):
  intface_names = {}
  for intface_class in impl_list:
    for func_name in intface_class.__interface__:
      if func_name in intface_names:
        raise ImplementError (func_name + 
              " defined in multiple intface_names: %s, %s"
              % (intface_names[func_name], intface_class.__name__))
      else:
        intface_names[func_name] = intface_class.__name__

  def deco(klass):
    for ifunc_name in intface_names:
      try:
        getattr(klass, ifunc_name)
      except AttributeError:
        raise ImplementError (
            "Interface %s requires %s to be implemented"
            % (intface_names[ifunc_name], ifunc_name))
      klass.__implements__ = impl_list
      return klass

  return deco


def implements(obj, intface):
  if not issubclass(intface, Interface):
    raise TypeError("2nd argument must be an Interface (or subclass)")

  if not getattr(obj, '__implements__', False):
    return False

  return intface in obj.__implements__
