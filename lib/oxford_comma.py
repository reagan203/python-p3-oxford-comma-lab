
def oxford_comma(items):
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    oxford_string = ", ".join(items[:-1])  
    oxford_string += f", and {items[-1]}"  
    return oxford_string

