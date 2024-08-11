print("hello") 
print("Hello \nnew line") # multiple lines; backslash is special and indicated that next character is special
print("1", "two", "three") # multiple arguments possible; combined when executed

# keyword arguments
# keyword "end" 
# which says in this case to not use the default "new line" and put an empty string instead
print("Hello", end="")
print("hello2")

print("different end argument", end="<3")

# keyword "sep"
print("i", "use", "the", "sep", "keyword", sep="-")

# combining them
print("sep", "and", "end", "keyword", sep="-", end="<3")

