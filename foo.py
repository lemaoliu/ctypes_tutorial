
import ctypes
lib = ctypes.cdll.LoadLibrary('./build/libfoo.so')

class Foo(object):
    def __init__(self, val):
        lib.Foo_new.argtypes = [ctypes.c_int]
        lib.Foo_new.restype = ctypes.c_void_p
        lib.Foo_bar.argtypes = [ctypes.c_void_p]
        lib.Foo_bar.restype = ctypes.c_void_p
        lib.Foo_foobar.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.Foo_foobar.restype = ctypes.c_int
        lib.Foo_show.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.Foo_show.restype = ctypes.c_char_p
        self.obj = lib.Foo_new(val)

    def bar(self):
        lib.Foo_bar(self.obj)
    
    def foobar(self, val):
        return lib.Foo_foobar(self.obj, val)

    def show(self, val):
        # for python3 I have to encode ascii or utf-8 before passing
        val = str(val).encode("utf-8")
        return lib.Foo_show(self.obj, val)

a = Foo(4)
a.bar()
val = "hellow, world"
print a.show(val)
