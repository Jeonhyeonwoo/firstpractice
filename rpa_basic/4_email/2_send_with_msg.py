import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일 입니다"
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "jhw7348@gmail.com" # 받는 사람 

msg.set_content("테스트 본문입니다.") # 본문

# 여러명에기 메일을 보낼 때
# msg["To"] = "jhw7348@gmail.com, jhw7348@gmail.com"
# to_list=["jhw7348@gmail.com","jhw7348@gmail.com"]
# msg["To"]=",".join(to_list)

# 참조
# msg["Cc"] = "jhw7348@gmail.com"

# 비밀 참조
# msg["Bcc"] = "jhw7348@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)