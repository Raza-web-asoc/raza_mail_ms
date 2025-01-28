from fastapi import FastAPI, HTTPException
from app.models import EmailRequest
from app.email_sender import send_email

app = FastAPI()



@app.post("/send-email")
async def send_email_endpoint(email_request: EmailRequest):
    result = send_email(
        to_email=email_request.to_email,
        subject=email_request.subject,
        body=email_request.body
    )

    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["message"])

    return result
