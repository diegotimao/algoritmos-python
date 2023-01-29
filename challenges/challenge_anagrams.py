alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z']


def list_numbers(list):
    list_index = []

    for index in list:

        for search_index in alfa:
            if search_index == index.upper():
                list_index.append(alfa.index(search_index))
    
    return list_index

def is_anagram(first_string, second_string):
    
    first_str = list_numbers(first_string)
    second_str = list_numbers(second_string)
    
    print(first_str)
    print(second_str)

