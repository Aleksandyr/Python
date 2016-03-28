first_text = input('Enter first text:')
second_text = input('Enter second text:')

print(first_text.split(second_text, 1)[-1].strip())
