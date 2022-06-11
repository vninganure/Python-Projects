import pandas
import datetime as dtm
import random
import smtplib
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
df = pandas.DataFrame(data)
month_list = df.month.tolist()
day_list = df.day.tolist()
letter_data = ""


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def pick_ltr():
    global letter_data
    letter_list = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]
    letter = random.choice(letter_list)
    print(letter)
    with open(letter, mode="r") as ltr:
        content = ltr.read()
        letter_data = content.replace("[NAME]", birth_name)

    with open(letter, "w") as llt:
        llt.write(letter_data)


# 2. Check if today matches a birthday in the birthdays.csv
now = dtm.datetime.now()
present_month = now.month
present_day = now.day
if present_month in month_list and present_day in day_list:
    current_data = data[data["month"] == now.month]
    df1 = pandas.DataFrame(current_data)

    birth_name_list = df1.name.tolist()
    birth_name = birth_name_list[0]
    email_list = df1.email.tolist()
    email = email_list[0]

    print(email)

    pick_ltr()
    print(letter_data)




# 4. Send the letter generated in step 3 to that person's email address.

    my_mail = "vjsmvit@gmail.com"
    password = "vijay1998"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(from_addr=my_mail,
                        to_addrs=email,
                        msg=f"Subject:Birthday wishes\n\n {letter_data}")
    connection.close()
#

