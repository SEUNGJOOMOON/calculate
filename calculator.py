import MySQLdb
import hashlib

class Calculator():
    def __init__(self, adate, service='REAL'):
        self.service = service

        if adate:
            self.adate = adate
        self.__getConnected__()
    
    def __getConnected__(self):
        if self.service == 'REAL':
            # 운영서버
            self.db = MySQLdb.connect(host="localhost", user="test", passwd="test", db="calculate", charset="utf8", use_unicode=True )
        else:
            # 개발서버
            self.db = MySQLdb.connect(host="localhost", user="test", passwd="test", db="calculate", charset="utf8", use_unicode=True )
        if self.db:
            self.cursor = self.db.cursor(MySQLdb.cursors.DictCursor)
        else:
            print("failed to connect db..")

    # select 쿼리 실행
    def getQueryResult(self, sql, bind=None):
        self.cursor.execute(sql, bind)
        return self.cursor.fetchall()
        
    # insert, update, delete 쿼리 실행
    def setQueryUpdate(self, sql, bind=None):
        self.cursor.execute(sql, bind)
        self.db.commit()

    # company id와 정산월로 암호화된 파일명 생성
    def getEncryptedFileName(self, company_id):
        name = str(self.adate) + str(company_id)
        return str(company_id) + "_" + hashlib.md5(name.encode()).hexdigest() + ".xlsx"

    # company id와 정산월로 암호화된 파일명 생성(알집 파일명)
    def getEncryptedFileNameForZip(self, company_id):
        name = str(self.adate) + str(company_id)
        return str(company_id) + "_" + hashlib.md5(name.encode()).hexdigest() + ".zip"

    # 정해진 만큼 글자수 줄이기
    def getShortenStr(self, str, cnt):
        if str == None or str == "":
            return ""

        result = str.replace('"','')
        if len(result) > cnt:
            result = result[:cnt] + "..."
        return result

    

