# Fifth program: convert a value from one data type to another (casting).

age = input('Please enter your age: ')
print(type(age))  # str, because input() always returns text

age = int(age)    # cast the text into an integer and store the result
print(type(age))  # int, after the conversion
