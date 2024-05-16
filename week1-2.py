SCORES = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]
words_file = "words.txt"

def calculate_score(word):
    score = 0
    for character in list(word):
        score += SCORES[ord(character) - ord("a")]
    return score

def read_words(word_file):
    with open(word_file) as file:
        return [line.strip() for line in file]

def is_subset(word, input_chars):
    word_chars = [0] * 26
    for character in word:
        word_chars[ord(character) - ord("a")] += 1
    for i in range(26):
        if word_chars[i] > input_chars[i]:
            return False
    return True

def find_best_anagram(input_txt, valid_words):
    input_chars = [0] * 26
    for character in input_txt:
        input_chars[ord(character) - ord("a")] += 1

    max_score = 0
    best_word = ""

    for word in valid_words:
        if is_subset(word, input_chars):
            score = calculate_score(word)
            if score > max_score:
                max_score = score
                best_word = word

    return best_word, max_score

def process_file(input_file, output_file):
    valid_words = read_words(words_file)
    random_words = read_words(input_file)
    
    total_score = 0
    
    with open(output_file, "w") as out_f:
        for random_word in random_words:
            best_anagram, score = find_best_anagram(random_word, valid_words)
            total_score += score
            out_f.write(f"{best_anagram}\n")

    print(f"Total score for {input_file}: {total_score}")

def main():
    input_files = ["small.txt", "medium.txt", "large.txt"]
    for input_file in input_files:
        output_file = input_file.replace(".txt", "_answer.txt")
        process_file(input_file, output_file)
        print(f"Finished: {input_file}")

if __name__ == "__main__":
    main()
