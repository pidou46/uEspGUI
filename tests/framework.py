'''share dictionary between object from different classes'''
class Data():
    __data__ = {}
    
    def append(self,key,value):
        self.__data__[key]=value
    
    def get_data(self):
        return self.__data__

class Client(Data):
    def __init__(self):
        pass
    

class Sensor(Data):
    ID_counter=0
    def __init__(self):
        self.ID=Sensor.ID_counter
        Sensor.ID_counter+=1
        
    def get_ID(self):
        return self.ID


cl=Client()
s1=Sensor()

s1.append(4,"hyyte")
print(cl.get_data())

print("s1 ID: {}".format(s1.get_ID()))

s2=Sensor()

print("s2 ID: {}".format(s2.get_ID()))

s2.append(5,"jkjl")
print("data: {}".format(s1.get_data()))