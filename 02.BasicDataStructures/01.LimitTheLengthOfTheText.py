text = input()

if len(text) < 10:
    print(text)
else:
    print(text[0:10] + '...')
