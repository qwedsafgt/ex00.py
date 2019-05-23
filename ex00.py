class CSV:
    def __init__(self,filename,postfix,is_head):
        self.filename=filename
        self.postfix=postfix
        self.is_head=is_head


    def judge_csv(self):
        file=open(self.filename,"r")
        content=file.read()
        global arr
        arr=content.split()
        b=arr[0]
        c=b.split()
        n=["Name","Age","No"]
        if len(c and n) > 0:
            return True
        else:
            return Flase

    def is_csv(self):
        if self.postfix=="csv":
            return True
        else:
            return Flase

    def read(self):
        file=open(self.filename,"r")
        if self.is_csv():
            if self.is_head:
                if self.judge_csv():
                    global arr

                    for a in arr:
                        print(a)
                else:
                   print("只能处理csv文件")
            else:
                print("只能处理存在head行的文件")

        else:
           print("只能处理后缀为csv的文件")

csv = CSV("ex0_sample.csv","csv",True)
csv.read()
                
