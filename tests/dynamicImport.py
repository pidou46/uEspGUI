'''dynamicaly import a module, get class object from name and instanciate'''

moduleName = 'my_module'
my_module = __import__(moduleName) # micropython doesn't have importlib.import_module so use __import__() instead but ther is some drawback see here under

MyClass = getattr(my_module, "Test")
toto = MyClass()

toto.test()




# You probably don't want to use __import__ to dynamically import a module by name, as it does not allow you to import submodules:
# 
# >>> mod = __import__("os.path")
# >>> mod.join
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'module' object has no attribute 'join'
