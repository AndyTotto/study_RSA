import sys

# input
key_num = "23011819"

def number_to_alphabet(key_num):
    alphabet = [
        "A", "B", "C", "D", "E", "F", "G",
        "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T", "U",
        "V", "W", "X", "Y", "Z"
    ]

    # check_format
    if len(key_num) % 2 != 0:
        print("unmatch format")
        sys.exit()

    key_word_char = []
    for char_num in range(len(key_num) // 2):
        slice_start = char_num * 2
        slice_end = slice_start + 1

        char_slice = key_num[slice_start:slice_end+1]
        append_char = alphabet[int(char_slice)-1]
        key_word_char.append(append_char)

    key_word = "".join(key_word_char)
    print(key_word)
    return key_word

if __name__ == "__main__":
    key_word = number_to_alphabet(key_num)