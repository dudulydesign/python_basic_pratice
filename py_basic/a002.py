

#列出九九乘法表



if __name__ == "__main__":

  for x in range(1, 10):
    row = []
    for y in range(1, 10):
      row.append("%sx%s=%s" % (x, y, x*y))

    print "\t".join(row)


  for x in range(1, 10):
    print
    for y in range(1, x+1):
      print "%d*%d=%d" % (x, y, x*y),


