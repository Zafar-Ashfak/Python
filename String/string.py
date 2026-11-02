text = "    the power            of your subconscious mind   "
print(text, type(text))

# ***************** STRING METHODS *****************
# 1. upper() -> Convert to uppercase
upr = text.upper()
print(upr)

# 2. lower() -> Convert to lowercase
lwr = text.lower()
print(lwr)

# 3. capitalize() -> Capitalize the first letter
cap = text.capitalize()
print(cap)

# 4. title() -> Capitalize each word
cap_each = text.title()
print(cap_each)

# 5. strip() -> remove spaces from both sides
s = text.strip()
print(s)

# 6. lstrip() -> remove spaces from left side
ls = text.lstrip()
print(ls)

# 7. rstrip() -> remove spaces from right side
rs = text.rstrip()
print(rs)

# 8. find() -> Find first occurrence (-1 if absent)
t = text.find("pow")
print(t)

f = text.find("python")
print(f)

# 9. index() -> Find first occurrence (raises error if absent)
print(text.index("o"))

# 10. count() -> Count occurrences (0 if absent)
print(text.count("of"))
print(text.count("md"))

# 11. replace() -> Replace substring
new_str = "I love Java"
rp = new_str.replace("Java", "Python")
print(new_str)
print(rp)

# 12. startswith() -> check prefix
sw = text.startswith(" ") # True
print(sw)

sw = text.startswith("the") # False
print(sw)

# 13. endswith() -> check suffix
ew = text.endswith(" ") # True
print(ew)

ew = text.endswith("mind") # False
print(ew)

# 14. split() -> split into a list
spl = text.split()
print(spl)

# 15. join() -> join elements of an iterable into a string
words = ["Python", "Java", "C++", "JavaScript", "Ruby", "SQL"]
print(" ".join(words))
print(", ".join(words))

# 16. isalpha() -> True if all characters are alphabets
print("Python".isalpha()) # True
print("Python123".isalpha()) # False

# 16. isalnum() -> True if all characters are alphabets or digits
print("Python".isalnum()) # True
print("Python123".isalnum()) # True

# 17. islower() -> check for lower case string
print("Python".islower()) # False
print("python".isalnum()) # True

# 18. isupper() -> check for upper case string
print("PYTHON".isupper()) # True
print("python".isupper()) # False
print("Python".isupper()) # False

# 19. isspace() -> check for only space
print(" python".isspace()) # False
print("  ".isspace()) # True

# 20. center() # wrap the string with the given symbol
print("Python".center(20, "-"))

# 21. ljust()
print("Python".ljust(15, "*"))

# 22. rjust()
print("Python".rjust(15, "*"))

# 23. zfill()
print("25".zfill(5))

# 24. len() -> returns the length of the string
print(len("Python")) # 6
print(len(text))

# 25. reverse() -> reverse a string
my_str = "Python"
print(my_str[::-1])















