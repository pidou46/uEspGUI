'''import submodule from module dynamicaly using name
This is usefull because micropython doesn't have importlib'''

moduleName = 'my_module'
_temp = __import__(moduleName, fromlist=['Test'])


toto = _temp.Test()

toto.test()

