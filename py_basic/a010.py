
'''
撰寫一程式可供使用者輸入一整數N
a.假如(N < 60)印出"不及格"
b.假如(N≥60)而且(N < 90)印出"及格"
c.假如(N≥90)而且(N < 100)印出"表現優異"
'''


if __name__ == "__main__":

  text = raw_input("enter:")
  print text
  n1 = int(text)


  if n1 < 60:
    print u"不及格"
  elif n1 >= 60 and n1 < 90:
    print u"及格"
  elif n1 >= 90 and n1 <= 100:
    print u"表現優異"

 
