'''
To send mail 
    enable in gmail the 2 step verification 
Then 
    use below link to create app password
    with app password and your mail id try to run the below code

    #https://support.google.com/accounts/answer/185833?hl=en
'''

import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'prateekkannojia456@gmail.com'
email_passwd = 'loph nskk qdiw qdaf'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='mtd.nithin@gmail.com', msg="Name: Prateek Kannojia, Github Repo:https://github.com/Prateek-kannojia, Teammate Name: Tameem ahmed mulla, Team Number:T4")
connection.close()
print('Mail sent successfully')

import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)

email_addr = 'ucc.francisxavier@gmail.com'
email_passwd = ''
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='ucc.francisxavier@gmail.com', msg="Hi Nithin,\n \n Our team is Team 1 (T1) and the participants are : \n\n 1. Francis Xavier K \n 2. Saumy Tiwari \n \n And my GitHub repository link is :\n https://github.com/FrancisXavier2K/Training_Python_Sept24 \n \n \n \n Thanks and Regards \n Francis Xavier K")
connection.close()
print('Mail sent successfully')