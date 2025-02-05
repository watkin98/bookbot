def main():

    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = get_num_of_words(file_contents)
    number_of_chars_in_string = get_num_of_each_char(file_contents)

    report = generate_report("books/frankenstein.txt", word_count, number_of_chars_in_string)
    print(report)

def get_num_of_words(words):
    count = 0
    words_in_list = words.split()

    for word in words_in_list:
        count += 1

    return count

def get_num_of_each_char(words):
    num_of_each_char = {}

    characters = list(words)

    for character in characters:
        lowered_character = character.lower()
        
        if lowered_character not in num_of_each_char:
            num_of_each_char[lowered_character] = 1
        else:
            num_of_each_char[lowered_character] += 1
        
    return num_of_each_char

def generate_report(file_path, word_count, character_dictionary):
    report = ""
    
    report += f"--- Begin report of {file_path} ---\n"
    report += f"{word_count} words found in the document\n"

    list_of_alphabet_counts = []

    for entry in character_dictionary:
        if entry.isalpha():
            list_of_alphabet_counts.append([entry, character_dictionary[entry]])

    for char in list_of_alphabet_counts:
        report += f"The '{char[0]}' character was found {char[1]} times\n"

    report += "--- End report ---"

    return report

main()