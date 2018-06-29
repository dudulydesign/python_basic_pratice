#這邊是我想要查找的基因變異variant的ID
test = RSID.iteritems()
 
#我希望開的線程數量
concurrent = 10
 
#因為資料是以json檔傳回，最後我都要塞回這個test_list中
test_list = {}
 
#使用queue的重點，是要解決共享變數不能被thread同時讀取的問題，
#他可以有效解決thread間在取用共享變數的問題
que = queue.Queue()
for i in range(concurrent):
    que.put(next(test)[1])
 
def doWork(*args):
    tmp = args[0]
    while tmp.qsize() > 0:
        rsid = tmp.get()
        test_list[rsid]=rsid
        #這邊是ensembl Rest API的接口
        server = "http://grch37.rest.ensembl.org"
        url_1 = "/variation/human/"
        url_2 = "?pops=1"
        ext = url_1+rsid+url_2
        r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
        if not r.ok:
            r.raise_for_status()
            sys.exit()
        decoded = r.json()
        test_list[rsid] = decoded
 
print("\t[Info] Queue size={0}".format(que.qsize()))
 
# 這邊是線程開啟和運行的地方
for i in range(concurrent):
    thread_name='Thd'+i
    t = threading.Thread(target=doWork, name=thread_name, args=(que,))
    t.daemon = True
    t.start() 
 
td = datetime.datetime.now() - st
print("\t[Info] Spending time={0}!".format(td))
