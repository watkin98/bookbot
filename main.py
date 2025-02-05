def main():

    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    '''
    print(file_contents)
    return 0
    '''
    num_of_words(file_contents)

def num_of_words(words):
    count = 0
    words_in_list = words.split()

    for word in words_in_list:
        count += 1

    print(count)

main()