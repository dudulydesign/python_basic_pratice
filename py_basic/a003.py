

#寫一個函數，求一個字串的長度，在main函數中輸入字串，並輸出其長度。

def func1(a):
  return len(a)

if __name__ == "__main__":

  a = raw_input("hello")
  str_len = func1(a)
  str_len2 = func1("12345678")
  str_len3 = func1("123458")
  print "hello: %s" % a, "len", str_len, str_len2, str_len3




