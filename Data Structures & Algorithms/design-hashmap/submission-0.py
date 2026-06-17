class MyHashMap:

    def __init__(self):
        self.output = []
        #self.output = {}
        
    def put(self, key: int, value: int) -> None:
        #self.output[key] = value
        for pair in self.output:
            if pair[0] == key:
                pair[1] = value
                return

        self.output.append([key,value])

    def get(self, key: int) -> int:
        # if key in self.output:
        #     return self.output[key]
        # return -1
        for pair in self.output:
            if pair[0] == key:
                return pair[1]
        
        return -1


    def remove(self, key: int) -> None:
        # if key in self.output:
        #     self.output.pop(key, None)
        for pair in self.output:
            if pair[0] == key:
                self.output.remove(pair)
                return
            
                




        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)