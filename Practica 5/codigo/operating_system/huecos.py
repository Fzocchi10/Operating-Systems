class Hueco:
        
    def __init__(self, baseDir, memorySize):
        self.__baseDir = baseDir
        self.__memoySize = memorySize


    @property
    def baseDir(self):
        return self.__baseDir
    

    @property
    def memorySize(self):
        return self.__memoySize
