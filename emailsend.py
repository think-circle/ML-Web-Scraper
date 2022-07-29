import creds
import pandas as pd
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename





def email_new(df,filepath):
    message = MIMEMultipart('alternative')
    message['Subject'] = "New Data from Today"
    message['From'] = creds.sender
    message['To'] = ', '.join(creds.recipient)
    html = MIMEText(df.to_html(index=False), "html")
    #html_figure = open('Melb-Price-Regression/data/figure1.html')
    #html = MIMEText(html_figure.read(), 'html')
    message.attach(html)

    with open(filepath, 'r') as f:
        attachment = MIMEApplication(f.read(), Name=basename(filepath))
        attachment['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filepath))
    message.attach(attachment)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
        #server.starttls()
        server.login(creds.sender, creds.password)
        server.sendmail(from_addr = creds.sender, to_addrs = creds.recipient, msg = message.as_string())

def data_get(filepath):
    data = pd.read_csv(filepath)[0:30]
    return data

def run(filepath):
  data = data_get(filepath)
  email_new(data,filepath)

if __name__ == '__main__':
    data = data_get('Melb-Price-Regression/data/melb_data_distance.csv')
    email_new(data,'Melb-Price-Regression/data/melb_data_distance.csv')