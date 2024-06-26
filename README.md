# Daily Email Report Scheduler

This project provides a Python script to schedule and send daily email reports using SMTP. The email includes a subject line with the current date and a predefined body.

## Prerequisites

Ensure you have Python 3.x installed. You also need the following Python libraries:
- `smtplib`
- `email`
- `schedule`

You can install the `schedule` library using pip:
```bash
pip install schedule
```

## Configuration

Update the script with your email server and account details.

### Email Server Configuration
Set your SMTP server details:
```python
SMTP_SERVER = 'smtp.yourserver.com'
SMTP_PORT = 587
SMTP_USER = 'youremail@domain.com'
SMTP_PASSWORD = 'yourpassword'
```

### Email Details
Set the sender and receiver email addresses, subject template, and body of the email:
```python
FROM_EMAIL = 'youremail@domain.com'
TO_EMAIL = 'recipientemail@domain.com'
EMAIL_SUBJECT_TEMPLATE = 'Daily Report - {date}'
EMAIL_BODY = 'Email body for the daily report'
SEND_TIME = "06:00"  # Time to send the email daily in HH:MM format
```

## Usage

Run the script to start scheduling the daily email report:
```bash
python daily_email_report.py
```

The script will run indefinitely, checking every minute to see if it is time to send the email.

## Functions

### `send_email()`
This function creates and sends an email using the SMTP server configuration. It constructs the email subject with the current date and attaches the email body.

### `schedule_daily_report()`
This function schedules the `send_email` function to run daily at the specified time. It uses the `schedule` library to handle the scheduling and continuously checks for pending tasks.

## Example

Here's an example of the configuration and function usage:

```python
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USER = 'user@example.com'
SMTP_PASSWORD = 'password'

FROM_EMAIL = 'user@example.com'
TO_EMAIL = 'recipient@example.com'
EMAIL_SUBJECT_TEMPLATE = 'Daily Report - {date}'
EMAIL_BODY = 'This is the body of the daily report.'
SEND_TIME = "06:00"

def send_email():
    # Function code here...

def schedule_daily_report():
    # Function code here...

if __name__ == '__main__':
    schedule_daily_report()
```

This setup ensures that an email is sent daily at 6:00 AM with the specified subject and body content.

# Agendador de Relatório Diário por Email

Este projeto consiste em um script Python para agendar e enviar relatórios diários por email utilizando SMTP. O email inclui uma linha de assunto com a data atual e um corpo predefinido.

## Pré-requisitos

Certifique-se de ter o Python 3.x instalado. Você também precisa das seguintes bibliotecas Python:
- `smtplib`
- `email`
- `schedule`

Você pode instalar a biblioteca `schedule` usando o pip:
```bash
pip install schedule
```

## Configuração

Atualize o script com os detalhes do seu servidor de email e conta.

### Configuração do Servidor de Email
Defina os detalhes do seu servidor SMTP:
```python
SMTP_SERVER = 'smtp.seuservidor.com'
SMTP_PORT = 587
SMTP_USER = 'seuemail@dominio.com'
SMTP_PASSWORD = 'suasenha'
```

### Detalhes do Email
Configure os endereços de email do remetente e do destinatário, o modelo do assunto do email e o corpo do email:
```python
FROM_EMAIL = 'seuemail@dominio.com'
TO_EMAIL = 'emaildodestinatario@dominio.com'
EMAIL_SUBJECT_TEMPLATE = 'Relatório Diário - {date}'
EMAIL_BODY = 'Corpo do email para o relatório diário'
SEND_TIME = "06:00"  # Horário para enviar o email diariamente no formato HH:MM
```

## Uso

Execute o script para iniciar o agendamento do relatório diário por email:
```bash
python agendador_relatorio_diario.py
```

O script será executado indefinidamente, verificando a cada minuto se é hora de enviar o email.

## Funções

### `send_email()`
Esta função cria e envia um email usando a configuração do servidor SMTP. Ela constrói o assunto do email com a data atual e anexa o corpo do email.

### `schedule_daily_report()`
Esta função agenda a função `send_email` para ser executada diariamente no horário especificado. Ela utiliza a biblioteca `schedule` para lidar com o agendamento e verifica continuamente as tarefas pendentes.

## Exemplo

Aqui está um exemplo da configuração e uso das funções:

```python
SMTP_SERVER = 'smtp.exemplo.com'
SMTP_PORT = 587
SMTP_USER = 'usuario@exemplo.com'
SMTP_PASSWORD = 'senha'

FROM_EMAIL = 'usuario@exemplo.com'
TO_EMAIL = 'destinatario@exemplo.com'
EMAIL_SUBJECT_TEMPLATE = 'Relatório Diário - {date}'
EMAIL_BODY = 'Este é o corpo do relatório diário.'
SEND_TIME = "06:00"

def send_email():
    # Código da função aqui...

def schedule_daily_report():
    # Código da função aqui...

if __name__ == '__main__':
    schedule_daily_report()
```

Esta configuração garante que um email seja enviado diariamente às 6:00 da manhã com o assunto e conteúdo especificados.
