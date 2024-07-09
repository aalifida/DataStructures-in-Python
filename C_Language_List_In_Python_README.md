# Dynamic Array Implementation in Python

This repository contains a Python implementation of a dynamic array, similar to Python's built-in list. The dynamic array is designed to automatically resize itself as elements are added or removed, providing efficient memory usage and performance.

## Features

- **Initialization**: Create a dynamic array with an initial capacity of 1.
- **Append**: Add elements to the end of the array, resizing the array when necessary.
- **Pop**: Remove and return the last element of the array.
- **Clear**: Clear all elements in the array.
- **Find**: Find the position of an element in the array.
- **Insert**: Insert an element at a specific position.
- **Remove**: Remove an element from the array by its value.
- **Resize**: Automatically resize the array to accommodate more elements.
- **String Representation**: Return a string representation of the array.
- **Index Access**: Access elements by their index.
- **Deletion**: Delete an element at a specific position.

## Usage

Here's a quick example of how to use the dynamic array:

```python
from dynamic_array import DynamicArray

# Initialize the array
arr = DynamicArray()

# Append elements
arr.append(1)
arr.append(2)
arr.append(3)

# Print the array
print(arr)  # Output: [1, 2, 3]

# Pop an element
arr.pop()  # Output: 3

# Insert an element at a specific position
arr.insert(1, 5)

# Print the array
print(arr)  # Output: [1, 5, 2]

# Remove an element by value
arr.remove(5)

# Print the array
print(arr)  # Output: [1, 2]
```

## Methods

- `__init__()`: Initialize the dynamic array.
- `__len__()`: Return the number of elements in the array.
- `append(item)`: Add an item to the end of the array.
- `pop()`: Remove and return the last item of the array.
- `clear()`: Clear all elements from the array.
- `find(item)`: Find the position of an item in the array.
- `insert(pos, item)`: Insert an item at the specified position.
- `remove(item)`: Remove the first occurrence of an item from the array.
- `__resize(new_capacity)`: Resize the array to the new capacity.
- `__str__()`: Return a string representation of the array.
- `__getitem__(index)`: Get the item at the specified index.
- `__delitem__(pos)`: Delete the item at the specified position.
- `__make_array(capacity)`: Create a new array with the specified capacity.

## Contact

For any questions or suggestions, feel free to contact me at Waleed.fida2@gmail.com.
