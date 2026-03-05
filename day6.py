# THIS IS DAY 5 OF THE 100 DAYS OF CODE CHALLENGE

# --Palindrome Checker(String)--
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
string = input("Enter a string: ")
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')