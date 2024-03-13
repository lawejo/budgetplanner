import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import expenses.categorize_expenses as calculate
from datetime import datetime

current_month = datetime.now().month
yearly_expenses = calculate.calculate_expenses()

# Extracting the expenses for the current month
current_month_expenses = yearly_expenses[current_month]

# Extracting all expenses for a specific month (let's say December - month 12)
all_expenses = yearly_expenses[12]

# Calculate the total expenses for the month
total_expenses = sum(row['expenses_single_expense'] for row in all_expenses)

def generate_expenses_html(expenses):
    expense_items_html = ""
    for expense in expenses:
        expense_name = expense.get('expenses_name', '')
        single_expense = expense.get('expenses_single_expense', 0)
        expense_items_html += f"<li>{expense_name}: {single_expense}</li>"

    return expense_items_html

def budget():

    sender_email = "fulldemo93@gmail.com"
    receiver_email = "lwj1993@gmail.com"
    password = "iwzoxytyzkhwuqqu"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Månedlige budget"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text version of your message
    text = """\
    Hi,
    How are you?
    Here is your monthly budget overview:
    Total Expenses: {}
    """.format(total_expenses)

    # Create the HTML version of your message
    html = f"""<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <!-- ... (your existing HTML code) ... -->
    <body bgcolor="#F5F8FA"
        style="width: 100%; margin: auto 0; padding:0; font-family:Lato, sans-serif; font-size:18px; color:#33475B; word-break:break-word">

        <! First Row -->
        <table role="presentation" border="0" cellpadding="0" cellspacing="10px"
            style="padding: 30px 30px 30px 60px;">
            <tr>
                <td style="vertical-align: top;">
                    <h2 style="font-size: 28px; font-weight: 900;">Overblik</h2>
                    <p style="font-weight: 100;">
                        Her har du dit månedlige overblik over dine kommende udgifter,
                    </p>
                    <p style="font-weight: 100;">
                        Total Expenses: {total_expenses}
                    </p>
                    <ul style="list-style-type: none; padding: 0;">
                        {generate_expenses_html(current_month_expenses)}
                    </ul>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

budget()
