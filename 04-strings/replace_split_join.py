# Twenty-second program: use the string methods replace(), split() and join().

date = input('Enter the date in this format (dd-mm-yyyy): ')

# split() breaks the text into a list; join() puts it back together with a new separator.
date_parts = date.split('-')  # [dd, mm, yyyy]
date_new_format = '/'.join(date_parts)
print(date_new_format)

# replace() swaps one substring for another.
print(date.replace('-', '/'))
