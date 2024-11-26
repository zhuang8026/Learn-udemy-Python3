word_list = ["is", "who", "when", "it", "is", "who", "is"]

result1 = dict()  # 字典, 特性：每個鍵必須是唯一的，不能重複，而值則可以重複
# key 不可變, value 可變

for word in word_list:  # 迴圈list
    if word not in result1:  # 字典中是否有word
        result1[word] = 1
    else:
        result1[word] += 1

print(f"result1: {result1}")  # {"result1)  # {'is': 3, 'who': 2, 'when': 1, 'it': 1}


result2 = dict()
for word in word_list:
    result2.setdefault(word, 0)  # [setdefault] 當word不存在於result中時，就給他一個預設值0 -> {"is": 0}
    result2[word] += 1

print(f"result2: {result2}")  # {'is': 3, 'who': 2, 'when': 1, 'it': 1}


from collections import defaultdict  # 導入defaultdict

result3 = defaultdict(int)  # [和setdefault一樣] 當word不存在於result中時，就給他一個預設值0 -> {"is": 0}
                            # defaultdict(默認類型) int -> {'key': 0}
                            # defaultdict(默認類型) list -> {'key': []}
                            # defaultdict(int or list)
                            # result['a'] -> {a: 0} or {a: []}

for word in word_list:
    result3[word] += 1

print(f"result3: {result3}")  # {'is': 3, 'who': 2, 'when': 1, 'it': 1}


def set_default():
    return {"name": "", "age": 0}


result4 = defaultdict(set_default)  # 默認類型: {"name": "", "age": 0}
print(f"result4: {result4['a']}")

result4["a"] = {"name": "aaa", "age": 20, "sex": "male"}

print(f"result4-a: {result4}")  # { 'a': {'name': '', 'age': 0} }
