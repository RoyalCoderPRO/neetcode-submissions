class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None]*capacity
        print('init')


    def get(self, i: int) -> int:
        print(self.array)
        print('get')
        return self.array[i]
        

    def set(self, i: int, n: int) -> None:
        self.array[i] = n
        print('set')

    def pushback(self, n: int) -> None:
        if not self.array[self.capacity-1] is None:
            self.resize()
            print(self.capacity)
            self.array[int((self.capacity/2))] = n
            print('pushback1', self.array)
        else:
            for i in range(self.capacity):
                if self.array[i] is None:
                    self.array[i] = n
                    print('pushback2', self.array)
                    break

    def popback(self) -> int:
        if self.getSize() == 0:
            return
        for i in range(self.capacity-1,-1,-1):
            if not self.array[i] is None:
                temp = self.array[i]
                self.array[i] = None
                break
        return temp

    def resize(self) -> None:
        self.array += [None]*self.capacity
        self.capacity *= 2
        print('resize')

    def getSize(self) -> int:
        c = 0
        for i in range(self.capacity):
            if not self.array[i] is None:
                c+=1
        print('getsize')
        return c
    def getCapacity(self) -> int:
        print('getcap')
        return self.capacity
