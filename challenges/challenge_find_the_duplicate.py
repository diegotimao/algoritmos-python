def find_duplicate(nums):
    numbers = sorted(nums)

    if len(nums) < 2:
        return False

    for item in range(len(numbers) - 1):
        type_item = isinstance(numbers[item], int)

        if not type_item or numbers[item] < 0:
            return False
        if numbers[item] == numbers[item + 1]:
            return numbers[item]
    return False
