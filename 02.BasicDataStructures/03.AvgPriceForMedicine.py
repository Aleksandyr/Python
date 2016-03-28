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

min_val = prices.pop(prices.index(min(prices)))
max_val = prices.pop(prices.index(max(prices)))

for i in prices:
    if i == min_val:
        prices.pop(prices.index(i))

for i in prices:
    if i == max_val:
        prices.pop(prices.index(i))

if len(prices) != 0:
    avg_val = sum(prices) / len(prices)

    print('Max val:', max_val)
    print('Min val:', min_val)
    print('average val:', avg_val)
else:
    print('We have no prices!')





