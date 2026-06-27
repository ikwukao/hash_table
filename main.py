"""
Hash Table Implementation

A simple implementation of a hash table using Object-Oriented Programming (OOP)
principles in Python.

The hash table stores key-value pairs by computing a hash value from each key.
Hash collisions are handled using the Separate Chaining technique, where
multiple key-value pairs sharing the same hash are stored within a nested
dictionary.

Features:
- Custom hash function
- Key-value insertion
- Key removal
- Value lookup
- Collision handling using separate chaining

Created as part of the freeCodeCamp Python Data Structures curriculum.
"""


# =========================================================
# HASH TABLE IMPLEMENTATION
# =========================================================


class HashTable:
    """
    A simple hash table implementation.

    The hash table stores data as key-value pairs inside a dictionary,
    where each key is the computed hash value and each value is another
    dictionary that stores one or more original key-value pairs.

    Attributes:
        collection (dict):
            Stores hashed buckets containing key-value pairs.
    """

    def __init__(self):
        """
        Initialize an empty hash table.
        """
        self.collection = {}

    def hash(self, key):
        """
        Compute the hash value for a given string.

        The hash is calculated by summing the Unicode (ASCII)
        values of every character in the key.

        Args:
            key (str):
                The string to hash.

        Returns:
            int:
                The computed hash value.
        """
        return sum(ord(char) for char in key)

    def add(self, key, value):
        """
        Add a key-value pair to the hash table.

        If another key already exists with the same hash value,
        the new key-value pair is stored in the same bucket
        (collision handling via separate chaining).

        Args:
            key (str):
                The lookup key.

            value:
                The value associated with the key.
        """
        # Compute the hash for the provided key.
        hashed_key = self.hash(key)

        # Create a new bucket if one does not already exist.
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}

        # Store the key-value pair inside the bucket.
        self.collection[hashed_key][key] = value

    def remove(self, key):
        """
        Remove a key-value pair from the hash table.

        If the key does not exist, the method exits without
        raising an exception.

        Args:
            key (str):
                The key to remove.
        """
        hashed_key = self.hash(key)

        # Check whether the corresponding bucket exists.
        if hashed_key in self.collection:
            # Remove only the requested key.
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]

                # Remove the bucket if it becomes empty.
                if not self.collection[hashed_key]:
                    del self.collection[hashed_key]

    def lookup(self, key):
        """
        Retrieve the value associated with a key.

        Args:
            key (str):
                The key to search for.

        Returns:
            Any:
                The associated value if found,
                otherwise None.
        """
        hashed_key = self.hash(key)

        # Return the stored value if the bucket exists.
        if hashed_key in self.collection:
            return self.collection[hashed_key].get(key, None)

        # Key not found.
        return None


# =========================================================
# APPLICATION ENTRY POINT
# =========================================================

# Create a new hash table.
ht = HashTable()

# ---------------------------------------------------------
# Insert sample data
# ---------------------------------------------------------

ht.add("golf", "sport")
print(ht.collection)

# Demonstrate collision handling.
# "dear" and "read" produce the same hash value.
ht.add("dear", "friend")
ht.add("read", "book")

print(ht.collection)

# ---------------------------------------------------------
# Retrieve a stored value
# ---------------------------------------------------------

print(ht.lookup("golf"))

# ---------------------------------------------------------
# Remove a key-value pair
# ---------------------------------------------------------

ht.remove("golf")

# Verify that the key no longer exists.
print(ht.lookup("golf"))
