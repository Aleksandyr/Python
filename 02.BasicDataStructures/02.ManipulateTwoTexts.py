firstText = input('Enter first text:')
secondText = input('Enter second text:')

print(firstText.split(secondText, 1)[-1].strip())
