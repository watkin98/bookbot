def main():

    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    '''
    print(file_contents)
    return 0
    '''
    #get_num_of_words(file_contents)
    number_of_chars_in_string = get_num_of_each_char(file_contents)
    print(number_of_chars_in_string)

def get_num_of_words(words):
    count = 0
    words_in_list = words.split()

    for word in words_in_list:
        count += 1

    print(count)

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

main()