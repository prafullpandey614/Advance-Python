my_iter = iter([1, 2, 3, 4, 5])

print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2

#Custom Iterator
class Iter:
    def __init__(self,data):
        self.index=0
        self.data = data
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        self.index+=1 
        return self.data[self.index-1]
        
obj = Iter([1,2,3,4,56,32,23])

print(obj.__iter__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
