#!/usr/bin/python3
'''Define a function'''


def text_indentation(text):
    '''This is a function that prints a text with 2 new lines after each of these characters: ., ? and :

        Args:
            text (str): the text to be printed
        raises:
            TypeError: if text is not string
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""

        for i in range(len(text)):
            if text[i] == "." or text[i] == "," or text[i] == ":":
                new_text = new_text + text[i] + "\n\n"
            else:
                new_text = new_text + text[i]
    print(new_list)
