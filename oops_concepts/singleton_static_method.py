class Singleton:
    _instance = None

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance


# Usage
singleton_instance1 = Singleton.get_instance()
singleton_instance2 = Singleton.get_instance()
print(singleton_instance1 is singleton_instance2)
