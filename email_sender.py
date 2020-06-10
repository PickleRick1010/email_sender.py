import smtplib

my_gmail = "youremailaddress@gmail.com" #Your email address
my_pass = "yourpassword" #your passsword,PREFFERABLY EASY ACCESS PASSWORD
receiver = ["xyz@gmail.com"] #write the receivers email address.You can also write multiple recipients addresses in the list


def email_spammer(receiver_email):
    """ this function lets the user spam someones email account with messages """
    with smtplib.SMTP("smtp.gmail.com" , 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(my_gmail,my_pass) #logs in to the given user account

        subject = "subject of text"
        body = "Your message"

        msg = f"subject:{subject} \n\n{body}"

        smtp.sendmail(my_gmail,receiver_email,msg) #sends the email

try:
    n = int(input("How many times do you want to send the message? "))

    for k in receiver:
        for i in range(n):
            email_spammer(k)
    print("message sent!!!")
except:
    print("Mission failed!!")