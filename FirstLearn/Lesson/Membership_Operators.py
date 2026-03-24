fruits = ['apple', 'banana', 'cherry']
print('apple' in fruits)     # True
print('grape' in fruits)     # False

print('orange' not in fruits)  # True
print('banana' not in fruits)  # False

text = "hello world"
print('h' in text)          # True
print('z' in text)          # False

person = {'name': 'Alice', 'age': 25}
print('name' in person)     # True (checks keys only)
print('Alice' in person)    # False (value, not key)
