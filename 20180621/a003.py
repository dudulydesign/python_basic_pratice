

if __name__ == "__main__":

  a = raw_input("enter:")
  arr = a.split(" ")
  print arr

  m = int(arr[0])
  d = int(arr[1])
  s = (m*2+d) % 3

  if s == 0:
    print u"普通"
  elif s == 1:
    print u"吉"
  elif s == 2:
    print u"大吉"

#ASCII

  



