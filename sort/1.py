def recursive_sum(numbers, index=0, total=0):
    # Base case: reached end of list
    if index == len(numbers):
        return total

    # Check if the current element is divisible by both 3 and 7
    if numbers[index] % 3 == 0 and numbers[index] % 7 == 0:
        total += numbers[index]

    # Recursive case: call function with next index and updated total
    return recursive_sum(numbers, index + 1, total)

nList = [1,3,5,7,3,7,89,77,33]
print(recursive_sum(nList))