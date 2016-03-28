prices = []
grades = 0

while True:
    inp = input('Enter: ')
    if 'stop' in inp:
        if len(prices) < 4:
            print('Length of prices should be at least 4')
            continue
        break

    prices.append(float(inp))

minVal = prices.pop(prices.index(min(prices)))
maxVal = prices.pop(prices.index(max(prices)))

for i in prices:
    if i == minVal:
        prices.pop(prices.index(i))

for i in prices:
    if i == maxVal:
        prices.pop(prices.index(i))

if len(prices) != 0:
    avgVal = sum(prices) / len(prices)

    print('Max val:', maxVal)
    print('Min val:', minVal)
    print('average val:', avgVal)
else:
    print('We have no prices!')





