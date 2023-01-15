def sort_list(numbers, order):
    # check the order and sort the list accordingly

    if order == "asc":
        # sort the list in ascending order
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                if numbers[i] > numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return numbers
    elif order == "desc":
        # sort the list in descending order
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                if numbers[i] < numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return numbers
    elif order == "none":
        # return the original list
        return numbers
    else:
        return "Invalid order"

# pass in your arguments to the function
print(sort_list([3,-1,2], "asc"))