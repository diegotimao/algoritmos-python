def str_order(word) -> str:
    params = list(word.lower())

    for index in range(len(params) - 1):
        for item in range(0, len(params) - 1 - index):
            if params[item] > params[item + 1]:
                params[item], params[item + 1] = params[item + 1], params[item]

    return "".join(params)


def is_anagram(first_string, second_string):
    first_str = str_order(first_string)
    second_str = str_order(second_string)

    if first_str == second_str:
        return (first_str, second_str, True)
    elif first_str == "" or second_str == "":
        return (first_str, second_str, False)
    else:
        return (first_str, second_str, False)
