
str = 'パタトクカシーー'
answer = ''
for i in range(len(str)):
    if i % 2 == 1:
        answer += str[i]
print(answer)

print(str[1::2])