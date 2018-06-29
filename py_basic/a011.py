


#文字順序反轉。如輸入 see you later，則輸出 later see you


def func1(a):
  return len(a)

if __name__ == "__main__":

  a = raw_input("enter:")
  str_len = func1(a)

  print "%s" % a,
  
  b = [a]
  for i in b[::-1]:
    print i

