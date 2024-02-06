from datetime import datetime
from bottle import get, response, template
import x

@get("/")
def _():
    try:
        all_expenses_raw = x.database_query("SELECT * FROM expenses", is_modification=False)
        all_expenses_dict = [dict(row) for row in all_expenses_raw]
     
  
        year = {
            1:[],
            2:[],
            3:[],
            4:[],
            5:[],
            6:[],
            7:[],
            8:[],
            9:[],
            10:[],
            11:[],
            12:[],
        }
 
        for row in all_expenses_dict:
            if row["expenses_frequency"] == "1":
                for month in year:
                    year[month].append(row)
            if row["expenses_first_payment_date"] == datetime(2024, 1, 1).date() and row["expenses_frequency"] != "1":
                month = 1     
                while month<= 12:
                    year[month].append(row)
                    month += int(row["expenses_frequency"])
            if row["expenses_first_payment_date"] != datetime(2024, 1, 1).date():
                row_date = int(row["expenses_first_payment_date"].strftime("%m").strip("0"))
                year[row_date].append(row)

                     
        for expense in year[10]:
            if expense["expenses_frequency"] != "1":
                print('*'*40)
                print(f'FROM render_index.py = {expense}')
                print('*'*40)
                    
        return template("index")
    except Exception as e:
        print(e.args[1])
        response.status = e.args[0]
        return {"info":"error","errortype":str(e.args[0])}
 