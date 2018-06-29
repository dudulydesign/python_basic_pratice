

if __name__ == "__main__":

  text = raw_input("enter:")
  print text
  n1 = int(text)
  c1 = n1 % 4
  c2 = n1 % 100
  c3 = n1 % 400
  print "c1", c1

  if c1 == 0 and c2 != 0:
    print u"閏年"
  elif c3 == 0:
    print u"閏年"
  else:
    print u"平年"




  



