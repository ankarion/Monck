class Monck(object):
    __indexed_moncks = {}
    __monck = None
    def __getitem__(self, index):
        if index not in self.__indexed_moncks:
            self.__indexed_moncks[index] = Monck()
        return self.__indexed_moncks[index]

    def __call__(self):
        if not self.__monck:
            self.__monck=Monck()
        return self.__monck 

    def __getattr__(self, attribute):
        return Monck()
