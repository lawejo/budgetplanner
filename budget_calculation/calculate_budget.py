import x
from bottle import response
import budget_calculation.monthly as monthly
def calculate_budget():
        try:
            income = x.database_query("SELECT * FROM income", is_modification=False)
            
            total_income = 0
            for row in income:
                  total_income += row["income_amount"]
                  print('*'*40)
                  print(f'FROM calculate_budget.py = {row["income_name"]}')
                  print('*'*40)
            available_income =  total_income - monthly.sum_expenses_current_month_number 
            print('*'*40)
            print(f'FROM calculate_budget.py = {available_income}')
            print('*'*40)
            return {"info":"ok","message":""}
        except Exception as e:
              print(e.args[1])
              response.status = e.args[0]
        finally:
              pass