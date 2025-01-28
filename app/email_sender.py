import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import settings
from jinja2 import Template

def send_email(to_email: str, subject: str, body: str, template: str = None, context: dict = None):
    if template and context:
        with open(template) as f:
            template = Template(f.read())
            body = template.render(context)


    try:
        # Crear el mensaje de correo
        msg = MIMEMultipart()
        msg["From"] = settings.EMAIL_FROM
        msg["To"] = to_email
        msg["Subject"] = subject

        # Agregar el cuerpo del correo
        msg.attach(MIMEText(body, "html"))

        # Conexión al servidor SMTP
        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.starttls()  # Asegura la conexión usando TLS
            server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            server.sendmail(settings.EMAIL_FROM, to_email, msg.as_string())

        return {"status": "success", "message": f"Email sent to {to_email}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
