
#試寫一個程式，可讓使用者輸入矩形的長寬，並於螢幕輸出為星號*所組成的矩形


if __name__ == "__main__":

  for i in range(0, 5):
    row = []
    for y in range(0, 5):
      row.append("*")
    print "\t".join(row)


