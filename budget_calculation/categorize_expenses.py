# from time import strftime
# from datetime import datetime
# import x
# from bottle import response
# def calculate_expenses():
#         try:
#             expenses = x.database_query("SELECT * FROM expenses", is_modification=False)
        
          
#             year = {
#                 1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]
#             }
    
#             for row in expenses:

# #################### 1.if expenses appear every month and have an undefined end-date 
# #################### 2.if expenses appear every month and have an defined end-date 
            
#                 if row["expenses_frequency"] == "1" and row["expenses_first_payment_date"] == datetime(2024, 1, 1).date() and row["expenses_last_payment_date"] == datetime(9999, 1, 1).date():
#                     for month in year:
#                         year[month].append(row)

#                 if row["expenses_frequency"] == "1" and row["expenses_first_payment_date"] == datetime(2024, 1, 1).date() and row["expenses_last_payment_date"] != datetime(9999, 1, 1).date():
#                     for month in year:
#                         if int(row["expenses_last_payment_date"].strftime("%m")) >= month:
#                             year[month].append(row)
                          
# #################### 1.if the expense start on 01/01/24 and it is not a monthly payment and have undefined end-date
# #################### 2.if the expense start on 01/01/24 and it is not a monthly payment and have end-date

            
#                 if row["expenses_first_payment_date"] == datetime(2024, 1, 1).date() and row["expenses_last_payment_date"]==datetime(9999, 1, 1).date() and row["expenses_frequency"] != "1" :
#                     month = 1     
#                     while month<= 12:
#                         year[month].append(row)
#                         month += int(row["expenses_frequency"])



#                 if row["expenses_first_payment_date"] == datetime(2024, 1, 1).date() and row["expenses_last_payment_date"] != datetime(9999, 1, 1).date() and row["expenses_frequency"] != "1" :
#                     for month in year:
#                         if int(row["expenses_last_payment_date"].strftime("%m")) >= month:
#                             year[month].append(row)
                
# #################### 1.if the first payment is not 01/01/24, then append the row according to frequency. If the row has undefined end-date
# #################### 2.if the first payment is not 01/01/24, then append the row according to frequency. If the row has defined end-date

           
#                 if row["expenses_first_payment_date"] != datetime(2024, 1, 1).date() and row["expenses_last_payment_date"] == datetime(9999, 1, 1).date():
#                     row_date = int(row["expenses_first_payment_date"].strftime("%m"))
#                     month = row_date
#                     while month<= 12:
#                         year[month].append(row)
#                         month += int(row["expenses_frequency"])

#                 if row["expenses_first_payment_date"] != datetime(2024, 1, 1).date() and row["expenses_last_payment_date"] != datetime(9999, 1, 1).date():
#                         row_date = int(row["expenses_first_payment_date"].strftime("%m"))
#                         month = row_date
#                         while month<= 12 and int(row["expenses_last_payment_date"].strftime("%m")) >= month:
#                             year[month].append(row)
#                             month += int(row["expenses_frequency"])
                          
#         except Exception as e:
#                print(e.args[1])
#                response.status = e.args[0]
#         finally:
#              return year
 