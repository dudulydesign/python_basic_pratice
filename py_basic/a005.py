


#將一整數一位一位的拆開，再將這些數字加起來。

if __name__ == "__main__":
    
    a = raw_input("enter:")
    arr = a.split(" ")
    
    print arr

    b = int (arr[0]) + int (arr[1]) + int (arr[2]) + int (arr[3])
    print b



