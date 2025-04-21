def dot_product_procedure(v1, v2, ps):
    """Procedure that calculates dot product and stores in ps"""
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of equal length")
    
    # Reset ps[0] to 0 (since we're modifying it by reference)
    ps[0] = 0
    
    # Calculate dot product using nested loop
    for i in range(len(v1)):
        ps[0] += v1[i] * v2[i]

def are_orthogonal_using_procedure(v1, v2):
    """Algorithm using procedure to check orthogonality"""
    ps = [0]  # Using list to simulate pass-by-reference
    dot_product_procedure(v1, v2, ps)
    return ps[0] == 0

def dot_product_function(v1, v2):
    """Function that returns dot product (pass by value)"""
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of equal length")
    
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result

def are_orthogonal_using_function(v1, v2):
    """Algorithm using function to check orthogonality"""
    return dot_product_function(v1, v2) == 0

# Test cases
vectors = [
    ([1, 0], [0, 1]),    
    ([2, 3], [-3, 2]),    
    ([1, 1], [-1, 1]),    
    ([1, 2, 3], [4, 5, 6]) 
]

print("Using procedure approach:")
for v1, v2 in vectors:
    print(f"Vectors {v1} and {v2} are orthogonal: {are_orthogonal_using_procedure(v1, v2)}")

print("\nUsing function approach:")
for v1, v2 in vectors:
    print(f"Vectors {v1} and {v2} are orthogonal: {are_orthogonal_using_function(v1, v2)}")