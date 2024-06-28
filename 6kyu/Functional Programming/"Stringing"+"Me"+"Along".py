"""
Implement a function that receives a string, and lets you extend it with repeated calls. When no argument is passed you should return a string consisting of space-separated words you've received earlier.

Note: There will always be at least 1 string; all inputs will be non-empty.

For example:
<< create_message("Hello")("World!")("how")("are")("you?")() == "Hello World! how are you?" >>
"""

def create_message(s):
    def extend_message(new_string=""):
        nonlocal s
        if new_string:
            s += " " + new_string
        else:
            return s
        return extend_message

    return extend_message
