



import datetime

if __name__ == '__main__':
  print(datetime.date.today().strftime('%d/%m/%Y'))
  
  miyazakiBirthDate = datetime.date(1941, 1, 5)

  print(miyazakiBirthDate.strftime('%d/%m/%Y'))
  
  miyazakiBirthDate = datetime.date + datetime.timedelta(days=1)

  
