import string
import fileinput

class Is_Regency:

    def __init__(self, manuscript, dictionary):
        self.manuscript = self.to_unique_set(manuscript)
        self.dictionary = self.to_unique_set(dictionary)

    def to_unique_set(self, text):

        if type(text) is not str:
            raise TypeError("Please input a string")

        to_remove = string.punctuation + '-' + "\"" + "\'" + string.digits
        stripped_string = ""
        for char in str(text):
            if char in to_remove:
                stripped_string += ' '
            else:
                stripped_string += char.lower()

        list_stripped_string = stripped_string.split()

        unique_words_set = set(list_stripped_string)
        return unique_words_set


    def find_difference(self):
        return self.manuscript - self.dictionary


    def __str__(self):
        i = 0
        difference = self.find_difference()
        return_str = ""
        for word in difference:
            if word is not None:
                return_str += str(i) + ": " + str(word) + "\n"
            i += 1
        return return_str


if __name__ == "__main__":
    ms = open('manuscript.txt', 'r', encoding='utf8')
    ms_read = ms.read()
    comparison_text = open('comparison_text.txt', 'r', encoding='utf8')
    comparison_text_read = comparison_text.read()
    ms_compare = Is_Regency(ms_read, comparison_text_read)
    print(ms_compare)