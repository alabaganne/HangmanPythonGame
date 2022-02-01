def clear_input(element):
    element.delete(0, "end")

def update_string_char(string, index, new_char):
    string_list = list(string)
    string_list[index] = new_char
    string = "".join(string_list)
    return string