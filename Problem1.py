def sum_distinct_elements(set1, set2):
    sum = 0  # Initialize sum to 0

    # Check elements in set1 that are not in set2
    for element in set1:
        found = False
        for compare in set2:
            if element == compare:
                found = True
                break  # Exit inner loop if duplicate is found
        if not found:
            sum += element  # Add if element is unique to set1

    # Check elements in set2 that are not in set1
    for element in set2:
        found = False
        for compare in set1:
            if element == compare:
                found = True
                break  # Exit inner loop if duplicate is found
        if not found:
            sum += element  # Add if element is unique to set2

    return sum

# Example usage
set1 = [3, 1, 7, 9]
set2 = [2, 4, 1, 9, 3]
result = sum_distinct_elements(set1, set2)
print("Output:", result)  # Output: 13 (7 + 2 + 4)

