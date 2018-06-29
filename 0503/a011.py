

if __name__ == "__main__":

  a1 = 1
  b2 = 1
  for i in range(1,9):
    print '%121d %121d' % (a1,b2),
    if (i % 3) == 0:
      print ''
    a1 = a1 + b2
    b2 = a1 + b2
