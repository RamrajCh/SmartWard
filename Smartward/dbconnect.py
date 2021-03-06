import mysql.connector
import pickle

try:
    with open("ward.pickle","rb") as picklefile:
        database_name=pickle.load(picklefile)['id']
except Exception:
    pass

class database:
    def __init__(self,hostname,user,dbase,pword=""):
        try:
            self.mydb=mysql.connector.connect(
                host=hostname,
                user=user,
                password=pword,
                )
        except Exception as e:
            print("Not Connected to database.")
            print(e)

    def insertintowadatable(self,name,address,about):
        #INSERT INTO `smartward`.`ward_registration` (ID,Municipality,WardNo,State,Address,Phone,Email,IP_Address,LogoPath,Password) VALUES('1','A','B','2','sgjkf','8935734','C','576','231','123')
        mycursor=self.mydb.cursor()
        sql="INSERT INTO wada(wada_name,wada_address,wada_info) VALUES (%s,%s,%s)"
        val=(name,address,about)  
        mycursor.execute(sql,val)        
        self.mydb.commit()
        print("insert successful.")
        mycursor.close()

class database_signinwindow(database):
    def __init__(self,hostname,user,dbase,pword=""):
        super().__init__(hostname,user,dbase,pword)
        self.mycursor=self.mydb.cursor()

    def createWardTable(self):
        try:
            #"CREATE TABLE `departments` ("" `dept_no` char(4) NOT NULL,"" `dept_name` varchar(40) NOT NULL,"" PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"") ENGINE=InnoDB"
            sql="CREATE TABLE `smartward`.`ward_registration` ( `ID` VARCHAR(30) NOT NULL , `Municipality` VARCHAR(75) NOT NULL , `WardNo` VARCHAR(5) NOT NULL , `State` VARCHAR(5) NOT NULL , `Address` VARCHAR(150) NOT NULL , `Phone` VARCHAR(15) NOT NULL , `Email` VARCHAR(50) NOT NULL , `IP_Address` VARCHAR(15) NOT NULL , `LogoPath` VARCHAR(150) NOT NULL , `Password` VARCHAR(16) NOT NULL , PRIMARY KEY (`ID`)) ENGINE = InnoDB"
            self.mycursor.execute(sql)
            self.mydb.commit()
            print("table created.")
            self.mycursor.close()
        except Exception as e:
            print("table already exists")

    def checkValid(self,municipality,ward):
        sql="SELECT * FROM `smartward`.`ward_registration` WHERE Municipality=%s AND WardNo=%s"
        self.mycursor.execute(sql,(municipality,ward))
        if(self.mycursor.fetchall()):
            return False
        return True

    def checkEmailValid(self,email):
        sql="SELECT * FROM `smartward`.`ward_registration` WHERE Email=%s"
        self.mycursor.execute(sql,(email,))
        if(self.mycursor.fetchall()):
            return False
        return True

    def InsertIntoward_registrationTable(self,id,municipality,wardno,state,address,phone,email,ip,logopath,pword):
        try:
            sql="INSERT INTO `smartward`.`ward_registration` (ID,Municipality,WardNo,State,Address,Phone,Email,IP_Address,LogoPath,Password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(id,municipality,wardno,state,address,phone,email,ip,logopath,pword)
            self.mycursor.execute(sql,val)
            self.mydb.commit()
            self.mycursor.close()
            return True
        except Exception:
            print("insert failed")
            return False

    def checkLoginValidity(self,id,pswd):
        sql = "SELECT * FROM `smartward`.`ward_registration` WHERE ID=%s OR Email=%s"
        self.mycursor.execute(sql, (id,id))
        login_details=self.mycursor.fetchall()
        if(login_details):
            if(pswd==login_details[0][-1]):
                return login_details[0][-3],login_details[0][-4],login_details[0][0]
        return "invalid","",""

    def checkEmailValidity(self,email):
        sql = "SELECT * FROM `smartward`.`ward_registration` WHERE Email=%s"
        self.mycursor.execute(sql, (email,))
        return self.mycursor.fetchall()

    def updateIP(self,id,ip):
        try:
            sql="UPDATE `smartward`.`ward_registration` SET IP_Address=%s WHERE ID=%s OR Email=%s"
            self.mycursor.execute(sql,(ip,id,id))
            self.mydb.commit()
            self.mycursor.close()
        except Exception:
            print("Ip update unsucessful")

    def createDatabase(self):
        self.mycursor.execute("CREATE DATABASE 3hu4")
        self.mydb.commit()
        self.mycursor.close()

class database_wardwindow(database):
    def __init__(self,hostname,user,dbase=database_name,pword=""):
        super().__init__(hostname, user, dbase, pword)
        self.mycursor = self.mydb.cursor()
        try:
            self.mycursor.execute("CREATE DATABASE {0}".format(dbase))
            self.mydb.commit()
        except Exception:
            pass
        self.mycursor.execute("USE {0}".format(dbase))
        self.mydb.commit()


    def createFormTable(self,tablename):
        try:
            sql="CREATE TABLE {0} (RegDate VARCHAR(10) NOT NULL,RegNo VARCHAR(15) NOT NULL, PRIMARY KEY(RegNo)) ENGINE=InnoDB".format(tablename)
            self.mycursor.execute(sql)
            self.mydb.commit()
        except Exception as e:
            print(e)
            return

    def addColumns(self,tablename,*columns):
        try:
            for column in columns:
                sql="ALTER TABLE {0} ADD COLUMN {1} VARCHAR(1600)".format(tablename,column)
                self.mycursor.execute(sql)
                self.mydb.commit()
        except Exception:
            return

    def insertValues(self,tablename,columnandvaluselist):
        csv=columnandvaluselist
        #print(csv)
        try:
            sql="INSERT INTO {0} ({1},{2}) VALUES ('{3}','{4}')".format(tablename,csv[0],csv[2],csv[1],csv[3])
            self.mycursor.execute(sql)
            self.mydb.commit()
        except Exception:
            return False
        for i in range(4,len(csv),2):
            sql="UPDATE {0} SET {1}='{2}' WHERE {3}='{4}'".format(tablename,csv[i],csv[i+1],csv[2],csv[3])
            self.mycursor.execute(sql)
            self.mydb.commit()
        return True

class database_statwindow(database):
    def __init__(self,hostname,user,dbase=database_name,pword=""):
        super().__init__(hostname, user, dbase, pword)
        self.mycursor = self.mydb.cursor()
        try:
            self.mycursor.execute("CREATE DATABASE {0}".format(dbase))
            self.mydb.commit()
        except Exception:
            pass
        self.mycursor.execute("USE {0}".format(dbase))
        self.mydb.commit()

    def getRowCount(self,column,tablename,value):
        try:
            sql = "SELECT {0} FROM {1} WHERE {0} LIKE '{2}'".format(column,tablename,value)
            self.mycursor.execute(sql)
            rows=self.mycursor.fetchall()
            if(rows):
                return len(rows)
            return 0
        except Exception as e:
            #print(e)
            return 0

class database_receipt(database):
    def __init__(self,hostname,user,dbase=database_name,pword=""):
        super().__init__(hostname, user, dbase, pword)
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("USE {0}".format(dbase))
        self.mydb.commit()

    def createReceiptGenerateTable(self):
        try:
            sql="CREATE TABLE ReceiptGenerate (sn INTEGER(3) NOT NULL,details VARCHAR(15) NOT NULL,amount INTEGER(8) NOT NULL, PRIMARY KEY(sn)) ENGINE=InnoDB"
            self.mycursor.execute(sql)
            self.mydb.commit()
        except Exception as e:
            print(e)
            return

    def insertintoreceiptgenerate(self,data):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO ReceiptGenerate (sn,details,amount) VALUES (%s,%s,%s)"
        val = (data[0],data[1],data[2])
        mycursor.execute(sql, val)
        self.mydb.commit()
        mycursor.close()

    def selectAmountfromReceiptGenerate(self):
        sql = "SELECT amount FROM ReceiptGenerate"
        self.mycursor.execute(sql)
        amount=self.mycursor.fetchall()
        total=0
        for a in amount:
            total+=a[0]
        return total

    def dropReceiptGenerate(self):
        self.mycursor.execute('DROP TABLE ReceiptGenerate')
        self.mydb.commit()

    def createReceiptTable(self):
        try:
            sql="CREATE TABLE Receipt(date VARCHAR(15) NOT NULL,receiptno VARCHAR(13) NOT NULL,name VARCHAR(50) NOT NULL,amount INTEGER(8) NOT NULL, PRIMARY KEY(receiptno)) ENGINE=InnoDB"
            self.mycursor.execute(sql)
            self.mydb.commit()
        except Exception as e:
            print(e)
            return

    def insertintoreceipt(self,data):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO Receipt (date,receiptno,name,amount) VALUES (%s,%s,%s,%s)"
        val = (data[0],data[1],data[2],data[3])
        mycursor.execute(sql, val)
        self.mydb.commit()
        mycursor.close()

    def getRowCount(self,date):
        try:
            sql = "SELECT amount FROM Receipt WHERE date LIKE '{0}'".format(date)
            self.mycursor.execute(sql)
            rows=self.mycursor.fetchall()
            if(rows):
                return len(rows)
            return 0
        except Exception as e:
            #print(e)
            return 0

    def getAmount(self,date):
        try:
            sql = "SELECT amount FROM Receipt WHERE date LIKE '{0}'".format(date)
            self.mycursor.execute(sql)
            rows=self.mycursor.fetchall()
            if(rows):
                total = 0
                for a in rows:
                    total += a[0]
                return total
            return 0
        except Exception as e:
            #print(e)
            return 0

#a=database_receipt("localhost", "root")
#print(a.getRowCount('2076/12/%'))
