def read_book_contents(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    
    return file_contents

def count_words(contents):
    return len(contents.split())

def count_characters(words):
    chars_dict = {}
    for char in words.lower():
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1

    return chars_dict

def sort_on(dict):
    return dict["num"]

def convert_into_dictionaries(chars_dict):
    list_of_dicts = []
    for key, value in chars_dict.items():
        if key.isalpha():
            list_of_dicts.append({"name": key, "num": value})
    
    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts

def print_report(path):
    text = read_book_contents(path)
    words = count_words(text)
    chars = count_characters(text)
    dicts = convert_into_dictionaries(chars)

    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    for letter in dicts:
        print(f"The '{letter["name"]}' character was found {letter["num"]} times")
    print("--- End report ---")

def main():
    path = "books/frankenstein.txt"
    print_report(path)

main()