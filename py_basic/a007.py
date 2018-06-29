

'''
34.撰寫程式輸入三個整數N1, N2與N3
a.將三個數字中最大的值列印出來
b.將三個數字中最小的值列印出來
c.將三個數字中間的值列印出來
d.如果三個數字相同則列印"三個數字相同"
'''


if __name__ == "__main__":

  l = []
  for i in range(3):
    x = int(raw_input("enter:\n"))
    l.append(x)

  l = sorted(l)
  print l

  print "min", l[0]
  print "max", l[-1]
  mid_index = int(len(l) / 2.0)
  print "mid", l[mid_index]
  print len(l) / 2, "vs", len(l) / 2.0, int(1), int(1.5)
  print "mid_index", mid_index



