# from multiprocessing import dummy
# import smtplib
# import ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import budget_calculation.categorize_expenses as calculate
# from datetime import datetime
# from yattag import Doc
# ########################################

# expenses_current_m = []
# expenses_current_m_st = []
# expenses_current_m_x = []
# expenses_future_x = []
# ########################################

# # Get the current month number
# current_month_number = datetime.now().month
# # Get the current month as a string
# current_month_str = datetime.now().strftime('%B')
# # Calculate yearly expenses
# yearly_expenses = calculate.calculate_expenses()
# ########################################


# for row in yearly_expenses[current_month_number]:
#     expenses_current_m.append(row['expenses_single_expense'])

# # Calculate sum of current month and append it to list
# sum_expenses_current_month_number = sum(expenses_current_m)

# # sorted = sorted(yearly_expenses[current_month_number], key=lambda k:k["expenses_single_expense"], reverse=True)





# for row in sorted(yearly_expenses[current_month_number], key=lambda k:k["expenses_single_expense"], reverse=True):
#     if row["expenses_frequency"] == "1":
#         expenses_current_m_st.append(row)
#     else:
#         expenses_current_m_x.append(row)

# # future 3 months
# coming_3_months = current_month_number + 4


# for month in yearly_expenses:
#     if month > current_month_number and month < coming_3_months:
#         for row in yearly_expenses[month]:
#             if not row["expenses_frequency"] == "1":
#                 expenses_future_x.append((row, month))



# def generate_expenses_html(expenses):
#     expense_items_html = ""
#     for types in expenses:
#         if type(types) == dict:    
#             for expense in expenses:
#                 expense_name = expense.get('expenses_name', '')
#                 single_expense = expense.get('expenses_single_expense', 0)
#                 expense_items_html += f"<li style='margin:0px;'>{expense_name}: {single_expense},-</li>"
#             return expense_items_html    

# def generate_expenses_html_tuple(expenses):
#     expense_items_html = ""
#     correlating_month = ""

#     for expense_tuple  in expenses:
#         expense_dict, month = expense_tuple 
#         # Handle month
#         dummy_date = datetime(2000, month, 1)
#         correlating_month = dummy_date.strftime('%B')

#         # Handle dict
#         expense_name = expense_dict.get('expenses_name', '')
#         single_expense = expense_dict.get('expenses_single_expense', 0)
#         expense_items_html += f"<li style='margin:0px;'>{expense_name}: {single_expense},- <i4>{correlating_month}</i4></li>"
                
#     return expense_items_html    

              





# def budget():

#     sender_email = "fulldemo93@gmail.com"
#     receiver_email = "lwj1993@gmail.com"
#     password = "iwzoxytyzkhwuqqu"

#     message = MIMEMultipart("alternative")
#     message["Subject"] = "Månedlige budget"
#     message["From"] = sender_email
#     message["To"] = receiver_email

#     # Create the plain-text and HTML version of your message
#     text = """\
#             Hi,
#             How are you?
#             www.your_website_here.com"""
#     html = f"""<!DOCTYPE html
#             PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
#             <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"
#             xmlns:v="urn:schemas-microsoft-com:vml" lang="en">

#             <head>
#             <link rel="stylesheet" type="text/css" hs-webfonts="true"
#             href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
#             <title>Email template</title>
#             <meta property="og:title" content="Email template">

#             <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

#             <meta http-equiv="X-UA-Compatible" content="IE=edge">

#             <meta name="viewport" content="width=device-width, initial-scale=1.0">


#             </head>

#                <body bgcolor="#F5F8FA"
#         style="width: 100%; margin: auto 0; padding:0; font-family:Lato, sans-serif; font-size:18px; color:#33475B; word-break:break-word">

#         <! First Row -->
#         <table role="presentation" border="0" cellpadding="0" cellspacing="10px"
#             style="padding: 30px 30px 0px 60px; height:100%;">
#             <tr>
#                 <td style="vertical-align: top; height:100%;">
#                     <h2 style="font-size: 28px; font-weight: 900;">Overblik</h2>
#                     <p style="font-weight: 100;">
#                         Her har du dit månedlige overblik over dine kommende udgifter for {current_month_str} måned,
#                     </p>
#                     <p style="font-weight: 100;">
#                         Samlede udgifter: {sum_expenses_current_month_number} kroner.
#                     </p>
#                     <div style="display:flex; flex-direction: row; width:100%;">
#                     <article style="margin:0px; width:100%">
#                     <h4>Måndelige udgifter</h4>
#                     <ul style="list-style-type: none; padding: 0;">
#                         {generate_expenses_html(expenses_current_m_st)}
#                     </ul>
#                     </article>
#                     <article style="margin:0px; width:100%">
#                     <h4>Kvartals, halvårlige og diverse udgifter</h4>
#                     <ul style="list-style-type: none; padding: 0;">
#                         {generate_expenses_html(expenses_current_m_x)}
#                     </ul>
#                     </article>
#                     </div>
#                     <div style="display:flex; flex-direction: row; width:100%;">
#                      <article style="margin:0px; width:100%">
#                     <h4>Fremtidige kvartals og halvårlige udgifter</h4>
#                     <ul style="list-style-type: none; padding: 0;">
#                         {generate_expenses_html_tuple(expenses_future_x)}
#                     </ul>
#                      </article>
#                     </div>
#                 </td>
#             </tr>
#         </table>
#     </body>

#             </html>


#             """

#     # Turn these into plain/html MIMEText objects
#     part1 = MIMEText(text, "plain")
#     part2 = MIMEText(html, "html")

#     # Add HTML/plain-text parts to MIMEMultipart message
#     # The email client will try to render the last part first
#     message.attach(part1)
#     message.attach(part2)

#     # Create secure connection with server and send email
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message.as_string())
# budget()