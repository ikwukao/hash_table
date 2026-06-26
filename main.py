class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hashed_key = self.hash(key)

        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}

        self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]

                if not self.collection[hashed_key]:
                    del self.collection[hashed_key]

    def lookup(self, key):
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            return self.collection[hashed_key].get(key, None)

        return None


ht = HashTable()

ht.add("golf", "sport")
print(ht.collection)

ht.add("dear", "friend")
ht.add("read", "book")
print(ht.collection)

print(ht.lookup("golf"))

ht.remove("golf")
print(ht.lookup("golf"))
