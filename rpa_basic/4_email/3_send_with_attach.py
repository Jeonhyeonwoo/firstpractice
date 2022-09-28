import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일 입니다"
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "jhw7348@gmail.com" # 받는 사람 
msg.set_content("다운로드하세요.")


# MINE Type
# msg.add_attachment()
with open("btn_brush.png", "rb") as f:
    msg.add_attachment(f.read(), maintype = "image", subtype = "png", filename = f.name)

with open("테스트파일.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype = "application", subtype = "pdf", filename = f.name)

with open("엑셀.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype = "application", subtype = "octet-stream", filename = f.name)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)