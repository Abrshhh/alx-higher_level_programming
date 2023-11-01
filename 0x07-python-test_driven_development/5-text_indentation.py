#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
        for i in range(len(text)):
            if text[i] == "." or text[i] == "," or text[i] == ":":
                new_text = new_text + text[i] + "\n\n"
            else:
                new_text = new_text + text[i]
