prices = []
grades = 0
while True:
    inp = input('Enter: ')
    if 'stop' in inp:
        if len(prices) < 4:
            print('Length of prices should be at least 4')
            continue
        break

    grades += float(inp)
    prices.append(float(inp))

minVal = prices.pop(prices.index(min(prices)))
maxVal = prices.pop(prices.index(max(prices)))
avgVal = (grades - (maxVal + minVal)) / len(prices)

print('Max val:', maxVal)
print('Min val:', minVal)
print('average val:', avgVal)


