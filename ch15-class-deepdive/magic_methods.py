class Account:

    # 初始化
    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount
        self._transaction = []

    # @property 裝飾器
    # 餘額
    @property
    def balance(self):
        return self.amount + sum(self._transaction)

    # 一般函數
    # def len__transaction(self):
    #     print(f"len__transaction = {len(self._transaction)}")

    # “__len__” -> 定義物件的長度行為
    def __len__(self):
        return len(self._transaction)

    # "__repr__" -> 設定print 機器人 看到的樣子 (當沒有__str__才會顯示__repr__)
    def __repr__(self):
        print("__repr__")
        return f"Account({self.name}, {self.amount})"

    # "__str__" -> 設定print 人類 看到的樣子
    def __str__(self):
        print("__str__")
        return f"name={self.name}, amount={self.amount}"

    def add_transaction(self, amount):
        self._transaction.append(amount)

    # "__eq__" -> 定義相等運算符 (==) 的行為
    def __eq__(self, other):
        # 注意：balance如果沒有"@property",就需要改成 self.balance()
        return self.balance == other.balance

    # "__lt__" -> 定義小於運算符 (<) 的行為
    def __lt__(self, other):
        return self.balance < other.balance


a1 = Account("Jack", 10)
a1.add_transaction(100)
a1.add_transaction(-20)
# a1.len__transaction() # 一般函數
# print(f"a1 len => {len(a1)}")  # 魔法函數


a2 = Account("Mark", 10)
a2.add_transaction(200)
a2.add_transaction(-50)
a2.add_transaction(10)

print(repr(a1))
print(str(a1))
a1
print(a1 == a2)
print(a1 < a2)
