class HashTable:
    def __init__(self):
        self.collection = {}
        
    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hash_key = self.hash(key)

        if hash_ky not in self.collection:
            self.collection[hashed_key] = {}

        self.collection[hashed_ky][key] = value

