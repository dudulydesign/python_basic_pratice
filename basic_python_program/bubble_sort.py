'''
氣泡排序法 - 使用Python (Bubble Sort)

 

插入排序法的原理是，從未排序的數列裡挑一個值(通常從最後一個開始)，並將相鄰的值做比較，如數值大小與排序不符，則兩者對調，並繼續往下一個進行比較(這邊特別的是，如果大小順序是正確的，則會拿小的那一個值繼續往下比較)，直到所有的值都比較且排序完成，下面直接用每個步驟氣泡排序法做的事情來讓大家瞭解。

原始數列 = [6, 5, 4, 3, 2, 1]  刷紫色是已排序的值，刷紅色是本次要比較的值。

第 1 次要排序的陣列  =  [6, 5, 4, 3, 2, 1]，本次要比較的值 = 1
  sourceBubbleSortList = [6, 5, 4, 3, 2, 1]
  sourceBubbleSortList = [6, 5, 4, 3, 1, 2]
  sourceBubbleSortList = [6, 5, 4, 1, 3, 2]
  sourceBubbleSortList = [6, 5, 1, 4, 3, 2]
  sourceBubbleSortList = [6, 1, 5, 4, 3, 2]
第 2 次要排序的陣列  =  [1, 6, 5, 4, 3, 2]，本次要比較的值 = 2
  sourceBubbleSortList = [1, 6, 5, 4, 3, 2]
  sourceBubbleSortList = [1, 6, 5, 4, 2, 3]
  sourceBubbleSortList = [1, 6, 5, 2, 4, 3]
  sourceBubbleSortList = [1, 6, 2, 5, 4, 3]
第 3 次要排序的陣列  =  [1, 2, 6, 5, 4, 3]，本次要比較的值 = 3
  sourceBubbleSortList = [1, 2, 6, 5, 4, 3]
  sourceBubbleSortList = [1, 2, 6, 5, 3, 4]
  sourceBubbleSortList = [1, 2, 6, 3, 5, 4]
第 4 次要排序的陣列  =  [1, 2, 3, 6, 5, 4]，本次要比較的值 = 4
  sourceBubbleSortList = [1, 2, 3, 6, 5, 4]
  sourceBubbleSortList = [1, 2, 3, 6, 4, 5]
第 5 次要排序的陣列  =  [1, 2, 3, 4, 6, 5]，本次要比較的值 = 5
  sourceBubbleSortList = [1, 2, 3, 4, 6, 5]
'''
#Bubble Sort

sampleList = [6,5,4,3,2,1]

def bubbleSort(sourceBubbleSortList):
  #how long the list
  listLength = len(sourceBubbleSortList)
  i = 0
  # the i here to count how many value not in
  while i < listLength-1:
    j = listLength - 1
    # here to compare two value
    while j > i:
      print(" sourceBubbleSortList = " + str(sourceBubbleSortList))
      #compare two value, replace it if here are diffrent big, and continute to compare until finish all of it
      if sourceBubbleSortList[j] < sourceBubbleSortList[j-1]:
        tempNum = sourceBubbleSortList[j]
        sourceBubbleSortList[j] = sourceBubbleSortList[j-1]
        sourceBubbleSortList[j-1] = tempNum
      
      j = j - 1
    i = i + 1

  return sourceBubbleSortList

