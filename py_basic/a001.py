

#輸入三個整數x,y,z，請把這三個數由小到大輸出。


if __name__ == "__main__":

  l = []
  for i in range(3):
    x = int(raw_input("enter:\n"))
    l.append(x)
  #l.sort()
  l2 = sorted(l)
  print l, l2



