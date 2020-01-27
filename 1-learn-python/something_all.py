__all__ = ['_a_private_variable', 'APublicClass']
# The rest is the same as before
a_public_variable = 42
_a_private_variable = 141
def a_public_function():
    print("I'm a public function! yay!")
def _a_private_function():
    print("Ain't nobody accessing me from another module...usually")
class APublicClass(object):
    pass
class _AWeirdClass(object):
    pass
