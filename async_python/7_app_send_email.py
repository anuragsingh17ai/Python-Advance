import asyncio
import smtplib

async def send_email(subject,body,to):
    content = "hello world"
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    sender = 'mvl@gmail.com'
    recipient = 'tester@gmail.com'
    mail.login('mvl@gmail.com','**')
    header='To:'+recipient+'\n'+'From:'\
    +sender+'\n'+'subject:testmail\n'
    content= header+content 
    mail.sendmail(sender,recipient,content)
    mail.close()

async def main():
    asyncio.create_task(send_email('Test Email','this is email','xyz@gmail.com'
    ))

    print('doing something')


asyncio.run(main)