

if __name__ == "__main__":

  for x in range(1, 10):
    print
    for y in range(1, x+1):
      print "%d*%d=%d" % (x, y, x*y),
