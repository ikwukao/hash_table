# Hash Table Implementation in Python

A simple implementation of a **Hash Table** from scratch using Python and Object-Oriented Programming (OOP). This project demonstrates the core principles of hash tables, including hashing, collision handling, insertion, deletion, and lookup operations without relying on Python's built-in dictionary as the primary data structure.

## Overview

A **hash table** is a data structure that stores data as **key-value pairs**. It uses a **hash function** to convert a key into an index, allowing for fast insertion, retrieval, and deletion of data.

This implementation uses:

* A custom hashing function based on the sum of Unicode (ASCII) values of the characters in a key.
* **Separate chaining** (nested dictionaries) to handle hash collisions.
* Basic CRUD-style operations for managing key-value pairs.

## Features

* Custom hash function
* Add key-value pairs
* Remove existing keys
* Look up values by key
* Collision handling using separate chaining
* Object-Oriented Design
* Simple and readable implementation

## Project Structure

```text
HashTable
│
├── collection (dictionary)
│
├── hash(key)
├── add(key, value)
├── remove(key)
└── lookup(key)
```

## How the Hash Function Works

The hash function calculates the sum of the Unicode values of every character in a string.

Example:

```python
sum(ord(char) for char in "golf")
```

Output:

```text
424
```

This hash value becomes the index used to store the key-value pair.

## Collision Handling

Different keys can sometimes produce the same hash value. This is called a **hash collision**.

For example:

```python
"dear"
"read"
```

Both produce the hash value:

```text
412
```

Instead of overwriting one another, both key-value pairs are stored together inside a nested dictionary:

```python
{
    412: {
        "dear": "friend",
        "read": "book"
    }
}
```

This collision-handling technique is known as **Separate Chaining**.

## Example Usage

```python
ht = HashTable()

ht.add("golf", "sport")
ht.add("dear", "friend")
ht.add("read", "book")

print(ht.lookup("golf"))

ht.remove("golf")

print(ht.lookup("golf"))
```

## Example Output

```text
{424: {'golf': 'sport'}}

{
    424: {'golf': 'sport'},
    412: {
        'dear': 'friend',
        'read': 'book'
    }
}

sport

None
```

## Time Complexity

| Operation     | Average Case | Worst Case |
| ------------- | -----------: | ---------: |
| Insert        |         O(1) |       O(n) |
| Lookup        |         O(1) |       O(n) |
| Remove        |         O(1) |       O(n) |
| Hash Function |         O(k) |       O(k) |

**Note:** *k* represents the length of the key being hashed.

## Concepts Demonstrated

This project reinforces several important computer science concepts:

* Hash Tables
* Hash Functions
* Unicode / ASCII Encoding
* Collision Handling
* Separate Chaining
* Dictionaries
* Object-Oriented Programming (OOP)
* Data Structures
* Algorithm Design

## Requirements

* Python 3.8 or later

No external libraries are required.

## Running the Program

Clone the repository:

```bash
git clone https://github.com/ikwukao/hash_table.git
```

Navigate to the project directory:

```bash
cd hash_table
```

Run the program:

```bash
python3 main.py
```

## Learning Objectives

By completing this project, you will understand:

* How hash tables store data
* How custom hash functions work
* Why collisions occur
* Techniques for handling collisions
* The average-case efficiency of hash tables
* Basic implementation of a fundamental data structure

## Possible Improvements

Future enhancements could include:

* Dynamic resizing (rehashing)
* Configurable bucket sizes
* Alternative collision resolution strategies (linear probing, quadratic probing, double hashing)
* Generic type support
* Iteration over keys and values
* Unit tests
* Better hash functions for improved distribution

## Author

Created as part of a Python Data Structures learning journey and the freeCodeCamp Python curriculum.

## License

This project is provided for educational and personal learning purposes.
