
# from smtplib import *
#
# my_gmail = ''
# my_gmail_password = ''
# sending_mail = 'ridwan.abdulwaheed@yahoo.com'
# from datetime import *
#
# current_date = datetime.now()
# print(current_date.weekday())
# date_of_birth = datetime(year=2002, month=10, day=17)
# print(date_of_birth)
# with open('quotes.txt') as quotes:
#     quotes_list = [i for i in quotes.readlines()]
# if current_date.weekday() == 0:
#     num = randint(0, len(quotes_list) - 1)
#     with SMTP('smtp.gmail.com') as gmail_connection:
#         gmail_connection.starttls()
#         gmail_connection.login(user=my_gmail, password=my_gmail_password)
#         gmail_connection.sendmail(from_addr=my_gmail, to_addrs=sending_mail,
#                                   msg=f'Subject:Motivational Quote\n\n{quotes_list[num]}')
#
#
from random import *
from datetime import *
import smtplib
import pandas
my_gmail = ''
my_gmail_password = '' # use your password
letters = ['letter_1.txt','letter_2.txt','letter_3.txt']
current_day = datetime.now().day
current_month = datetime.now().month
current_year = datetime.now().year

birthday = pandas.read_csv('birthdays.csv')
birthday_dic = birthday.to_dict(orient='records')

names = [{'name': i['name'], 'age': int(current_year - i['year']), 'email': i['email']} for i in birthday_dic if
         i['month'] == current_month and i['day'] == current_day]

for i in names :
    birthday_letter = choice(letters)
    ready_to_send =''
    age = i.get('age')
    with open(f'letter_templates/{birthday_letter}') as letter :
        check = letter.read()
    ready_to_send = check.replace('[NAME]',i['name'])
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(user=my_gmail,password=my_gmail_password)
    s.sendmail(from_addr=my_gmail,to_addrs=i['email'], msg= f'Subject:Happy Birthday You Are {age} Today !\n\n{ready_to_send}')
    s.quit()
