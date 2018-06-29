

#题目：输入三个整数x,y,z，请把这三个数由小到大输出。

if __name__ == "__main__":


while l:
  try:
    x = int (input("plz input x:"))
    y = int (input("plz input y:"))
    z = int (input("plz input z:"))
    list1 = [x, y, z]
    print(sorted(list1))
    break
  except:
    print("請輸入整數")
