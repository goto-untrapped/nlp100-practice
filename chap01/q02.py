str = 'stressed'
print(str[::-1])

answer = ''
for i in range(len(str)-1, -1, -1):
    answer += str[i]
print(answer)

print(''.join(reversed(str)))

print(reversed(str))  # <- ちなみに reversed()はイテレータを返すだけ だった