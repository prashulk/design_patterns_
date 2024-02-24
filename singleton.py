class Singleton:

    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Singleton object already created!")
        else:
            Singleton.__instance = self


s1 = Singleton.getInstance()
print(s1)
s2 = Singleton.getInstance()
print(s2)
#s1, s2 are referring to the same object

s1.x = 5

print(s2.x) #shared object

s3 = Singleton()

# Singleton Database Connection
class DatabaseConnection:
    __instance = None

    @staticmethod
    def get_instance():
        if DatabaseConnection.__instance is None:
            DatabaseConnection.__instance = DatabaseConnection()
            DatabaseConnection.__instance.connect()
        return DatabaseConnection.__instance

# Usage
db = DatabaseConnection.get_instance()
