# Checkpoint-Introduction-to-Data-Structures-and-Procedural-programming
#Problem 1.
# Distinct Elements Sum Calculator

## Description
This Python algorithm calculates the sum of all distinct elements between two arrays (lists). An element is considered distinct if it appears in one array but not the other.

## Features
- Uses Python lists to represent arrays
- Implements nested loop comparison as specified
- Handles integer elements
- Returns the sum of all distinct elements

## Usage
```python
def sum_distinct_elements(set1, set2):
    sum = 0
    
    # Check elements in set1 not in set2
    for element in set1:
        found = False
        for compare in set2:
            if element == compare:
                found = True
                break
        if not found:
            sum += element
    
    # Check elements in set2 not in set1
    for element in set2:
        found = False
        for compare in set1:
            if element == compare:
                found = True
                break
        if not found:
            sum += element
    
    return sum

# Example
set1 = [3, 1, 7, 9]
set2 = [2, 4, 1, 9, 3]
print(sum_distinct_elements(set1, set2))  # Output: 13
```
## How It Works
Initializes sum to 0

First nested loop:

Compares each element in set1 against set2

Adds to sum if element is unique to set1

Second nested loop:

Compares each element in set2 against set1

Adds to sum if element is unique to set2

Returns the total sum of distinct elements

Requirements
Python 3.x

#Problem 2

# Vector Operations: Dot Product and Orthogonality Checker

## Description
This Python project implements two approaches to calculate the dot product of vectors and determine if vectors are orthogonal:
1. **Procedure-based approach** (modifies a parameter by reference)
2. **Function-based approach** (returns the dot product value)

The dot product of two orthogonal vectors is zero, which is used to check for orthogonality.

## Features
- Calculates dot product of vectors in ℝⁿ
- Checks orthogonality for multiple vector pairs
- Implements both procedure and function approaches
- Handles vectors of different dimensions with error checking
- Demonstrates different parameter passing techniques:
  - Pass-by-reference (simulated using lists)
  - Pass-by-value (standard function return)

Requirements
Python 3.x

No external dependencies

Implementation Details
Vectors represented as Python lists (arrays)

Nested iteration for dot product calculation

Error handling for unequal vector lengths

Clear separation between calculation and orthogonality check

Requirements
Python 3.x
