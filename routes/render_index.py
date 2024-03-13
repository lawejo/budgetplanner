from bottle import get, response, template
import budget_calculation.categorize_expenses as expenses
import budget_calculation.calculate_budget as budget
import budget_calculation.monthly 
import x
@get("/")
def _():
    try:
        test = x.database_query('SELECT * FROM budget', is_modification=False)
        print('*'*40)
        print(f'FROM render_index.py = {test}')
        print('*'*40)
        # yearly_expenses = expenses.calculate_expenses()
        # income = budget.calculate_budget()
   
        # budget_calculation.monthly.budget()

        return template("index")
    except Exception as e:
        print(e.args[1])
        response.status = e.args[0]
        return {"info":"error","errortype":str(e.args[0])}
 
