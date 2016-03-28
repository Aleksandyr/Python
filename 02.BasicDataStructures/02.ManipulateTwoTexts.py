firstText = input('Enter first text:')
secondText = input('Enter second text:')

if firstText.find(secondText) != -1:
    startPos = firstText.find(secondText) + len(secondText)
    print(firstText[startPos:len(firstText)].strip())
else:
    print(firstText)
