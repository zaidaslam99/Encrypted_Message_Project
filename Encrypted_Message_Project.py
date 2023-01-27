# So this code opens a specifed text file reads its content then uses a dict to write an encrypted version of the
    # file contents to a second file each character for the secoond file should contain the code for the
    # corresponding character in the first file
def main():
    codes = encrypt_key()

    read_from_dummy_data()

    list_containing_text = read_from_dummy_data()

    each_letter_list = get_letter_list(list_containing_text)

    encrypted_file = translate_document(each_letter_list, codes)

    write_encrytped_message_to_file_function(encrypted_file)

def encrypt_key():

    codes = {"A": "%", "a": "1", "B": "@", "b": "2", "C": "*", "c": "3", "D": ">" , "d": "4", "E": "<",
             "e": "5", "F": "?", "f": "6", "G": ":", "g": "7", "H": "}", "h": "8", "I": "[", "i": "9",
             "J": "_", "j": "10","K": "||", "k": "11", "L": "+", "l": "12", "M": ",,", "m": "13", "N": "+",
             "n": "14", "O": "==", "o": "15", "P": "^^", "p": "16", "Q": "%%", "q": "17", "R": "^&",
             "r": "18", "S": "{=", "s": "19", "T": "}|", "t": "20", "U": "?>", "u": "21", "V": "$A^",
             "v": "22", "W": ",||", "w": "25", "X": "_+_", "x": "26", "Y": "_*)", "y": "27", "Z": "_{||",
             "z": "27", " ": "|||" }

    return codes

def read_from_dummy_data():

        obj_file = open("dummy_data.txt", "r")

        obj_file_readlines = obj_file.readlines()

        list_containing_text = []

        index = 0

        while index < len(obj_file_readlines):
            element = obj_file_readlines[index].rstrip("\n")
            list_containing_text.append(element)
            index += 1

        return list_containing_text

def get_letter_list(list_containing_text):

    list_of_words = []
    list_of_each_letter = []

    for each_line in list_containing_text:
        for each_word in each_line.split():
            list_of_words.append(each_word)

    for each_word in list_of_words:
        for each_letter in each_word:
            list_of_each_letter.append(each_letter)

    return list_of_each_letter

def translate_document(each_letter_list, codes):

    translated_list = []

    for each_char in each_letter_list:
        if each_char in codes.keys():
            encrypt_code = codes[each_char]
            translated_list.append(encrypt_code)

    return translated_list

def write_encrytped_message_to_file_function(encrypted_file):

    dummy_write_encrypt_obj = open("encrypted_message.txt", "w")

    for each_line in encrypted_file:
        dummy_write_encrypt_obj.write(each_line)

    dummy_write_encrypt_obj.close()

    print(f"data has been copied to encrypted_message.txt")

main()