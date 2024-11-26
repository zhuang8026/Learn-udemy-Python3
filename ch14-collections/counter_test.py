from collections import Counter

word_list = ['is', 'who', 'when', 'it', 'is', 'who', 'is']

a = Counter(word_list) # 自動計算每個字出現的次數
print("1->",a) # Counter({'is': 3, 'who': 2, 'when': 1, 'it': 1})

c = Counter('afdeofiafeafeieaafdhfasdfelkiencs')

print("2->", c) 


print("3->", c.most_common(3) ) # 打印前三名出現次數最多的字母

c.update('xsiefaefafeafefsesfe') # 更新 (累加資料，並非替換)

print("4->", c)