import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
from datetime import datetime

# Configurações do servidor de e-mail
SMTP_SERVER = 'smtp.seuservidor.com'
SMTP_PORT = 587
SMTP_USER = 'email@dominio.com'
SMTP_PASSWORD = 'senha'

# Configurações do e-mail
FROM_EMAIL = 'email@dominio.com'
TO_EMAIL = 'destinatarioemail@dominio.com'
EMAIL_SUBJECT_TEMPLATE = 'Mensagem do Dia - {date}'
EMAIL_BODY = 'Corpo do email para o relatório'
SEND_TIME = "06:00"  # Horário em que o e-mail será enviado diariamente

def send_email():
    """Envia um e-mail com o relatório diário."""
    subject = EMAIL_SUBJECT_TEMPLATE.format(date=datetime.now().strftime("%Y-%m-%d"))
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(EMAIL_BODY, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
        print(f'E-mail enviado com sucesso para {TO_EMAIL}')
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')

def schedule_daily_report():
    """Agenda o envio diário do relatório por e-mail."""
    schedule.every().day.at(SEND_TIME).do(send_email)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    schedule_daily_report()
