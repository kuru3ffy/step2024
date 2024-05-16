from itertools import permutations

def generate_permutations(input_txt):
    return ["".join(it) for it in permutations(input_txt)]

def create_sorted_dictionary(dict_list):
    new_dictionary = []
    for word in dict_list:
        sorted_word = "".join(sorted(word))
        new_dictionary.append([sorted_word, word])
    new_dictionary.sort()
    return new_dictionary

def binary_search(new_dictionary, target):
    start_idx = 0
    last_idx = len(new_dictionary) - 1
    center_idx = -1
    
    while start_idx <= last_idx:
        center_idx = (start_idx + last_idx) // 2
        if target == new_dictionary[center_idx][0]:
            return center_idx
        elif target > new_dictionary[center_idx][0]:
            start_idx = center_idx + 1
        else:
            last_idx = center_idx - 1

    return -1

def find_other_anagrams(new_dictionary, target_idx):
    if target_idx == -1:
        return []

    anagram_list = [new_dictionary[target_idx][1]]
    target_idx_before = target_idx
    target_idx_after = target_idx

    while target_idx_before > 0 and new_dictionary[target_idx_before][0] == new_dictionary[target_idx_before - 1][0]:
        anagram_list.append(new_dictionary[target_idx_before - 1][1])
        target_idx_before -= 1

    while target_idx_after + 1 < len(new_dictionary) and new_dictionary[target_idx_after][0] == new_dictionary[target_idx_after + 1][0]:
        anagram_list.append(new_dictionary[target_idx_after + 1][1])
        target_idx_after += 1

    return anagram_list

def better_solution(input_txt, dict_list):
    target = "".join(sorted(input_txt))
    new_dictionary = create_sorted_dictionary(dict_list)
    target_idx = binary_search(new_dictionary, target)
    return find_other_anagrams(new_dictionary, target_idx)

def read_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

if __name__ == "__main__":
    dict_list = read_dictionary("words.txt")
    input_text = input("Enter a word: ")
    print(*better_solution(input_text, dict_list))
