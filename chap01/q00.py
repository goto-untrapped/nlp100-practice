# 00. パタトクカシーー
# 2つの文字列「パトカー」と「タクシー」の文字を先頭から交互に連結し、文字列「パタトクカシーー」を得よ。

alternation = 'パタトクカシーー'
word1 = ''
word2 = ''
for i in range(0, len(alternation), 2):
    word1 += alternation[i]
    word2 += alternation[i + 1]

print(word1, word2, sep=", ")

# 解くべき問題を間違えた・・・。結合文字列を分解するのではなく、結合文字列をつくる。

word1 = 'パトカー'
word2 = 'タクシー'
alternation = ''
# 結合元の単語の長さが一緒の場合
for i in range(len(word1)):
    alternation += word1[i] + word2[i]

print(alternation)

# 結合元の単語の長さが異なるの場合
max_len = max(len(word1), len(word2))
for i in range(max_len):
    if i < len(word1):
        alternation += word1[i]
    if i < len(word2):
        alternation += word2[i]

print(alternation)

# ai
# Pythonの組み込み関数を使う場合
from itertools import zip_longest
word1 = 'パトカー'
word2 = 'タクシー'
# {('パ', 'タ'), ('ト', 'ク'), ('カ', 'シ'), ('ー', 'ー')} 
# => {('パタ'), ('トク'), ('カシ'), ('ーー')} 
# => 'パタトクカシーー'
alternation = ''.join(''.join(pair) for pair in zip_longest(word1, word2, fillvalue=''))
print(alternation)

# zip()を使う場合
# fillvalueを指定しない場合、長さの短い方に合わせてタプルが作成される
# 長さが異なったらエラーにする場合、zit(..., strict=True)にする
from itertools import zip_longest
word1 = 'パトカーa'
word2 = 'タクシー'
alternation = ''.join(''.join(pair) for pair in zip(word1, word2))
print(alternation)

# other






# ちなみに
# Python で文字列を囲むのに '', "" の技術的な違いはないので、趣味or慣習に合わせれば良さそう
