import sys
import os, sys
sys.path.append(os.path.dirname())
import calculator
import decimal

calc = calculator.Calculator(2203, 'REAL')

print("adate is..." + str(calc.adate))
if input("Do you want to continue?") != "y":
    exit()


sql = """
        SELECT
            id,
            adate,
            company_id,
            contract_id,
            rate,
            item_code,
            item_price,
            item_sales_cnt,
            item_return_cnt
        FROM ITEM_SALES
        WHERE adate = %s
    """

sales = calc.getQueryResult(sql, [calc.adate])

seq = 0

for sale in sales:

    seq += 1

    adate = sale["adate"]

    if adate != calc.adate:
        print("error")
        exit()


    id = sale["id"] #id
    company_id = sale["company_id"] #회사 코드
    contract_id = sale["contract_id"] #계약 코드
    rate = sale["rate"] #정산 요율
    item_code = sale["item_code"] #상품 코드
    item_price = sale["item_price"] #상품 가격
    item_sales_cnt = sale["item_sales_cnt"] #상품 판매 갯수
    item_return_cnt = sale["item_return_cnt"] #상품 반품 갯수
    #item 이름 가져오기

    #계약정보 가져오기


    #End datas from DB
    
    #Start account
    sql = """UPDATE ITEM_SALES
            SET company_id = %s,
                contract_id = %s,
                rate = %s,
                item_code = %s,
                item_price = %s,
                item_sales_cnt = %s,
                item_return_cnt = %s
            WHERE id=%s"""
    
    bind = [adate,
            company_id,
            contract_id,
            rate,
            item_code,
            item_price,
            item_sales_cnt,
            item_return_cnt,
            int(ID)]

    calc.setQueryUpdate(sql, bind)

    print(str(seq) + "/" + str(id))
print("DONE.")    
