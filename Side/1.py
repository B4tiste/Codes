# Write a function to reverse a string

string = "bonjour"

def rev(string):
    return "".join([letter for letter in reversed(string)])

print(string, rev(string))