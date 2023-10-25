def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(chars_dict)

def print_report(chars_dict):
    sorted_chars = sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_chars:
        count = chars_dict[char]
        print(f"the '{char}' character was found {count} times")

def get_chars_dict(text):
    chars_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars_dict:
                chars_dict[lowered] += 1
            else:
                chars_dict[lowered] = 1
    return chars_dict
    chars_list = list(chars_dict)
    chars_list.sort()
    return chars_list


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()