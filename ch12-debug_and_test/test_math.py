import unittest

from demo.math import add  #  引入要測試的方法

# python -m unittest
# 所有測試 都是以 class 形式定義
# 每一個測試類都必須是 unittest.TestCase 的子類
# 每一個測試方法必須以 test_ 開頭
# 使用 assert 進行測試


class TestAdd(unittest.TestCase):

    # 測試方法一
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 4), 5)

    # 測試方法二
    def test_add_2(self):
        self.assertEqual(add(10, 20), 30)
        self.assertNotEqual(add(10, 20), 31)

    # 測試方法三 觸發錯誤結果
    def test_add_3(self):
        self.assertRaises(ValueError, add, 1, 1.2)  # 檢查ValueError是否會被觸法


if __name__ == "__main__":
    unittest.main()
