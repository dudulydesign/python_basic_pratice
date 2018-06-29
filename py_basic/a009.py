
#字串反轉。如：輸入 abcdef，則輸出 fedcba

def reverse(str):
  out = ''
  li = list(str)
  for i in range(len(li), 0, -1):
    out += ''.join(li[i-1])
  return out



