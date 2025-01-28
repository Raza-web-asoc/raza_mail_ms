from fastapi import FastAPI, HTTPException
from app.models.email_request import EmailRequestMatch
from app.email_sender import send_email

app = FastAPI()



@app.post("/send-new-match")
async def send_email_endpoint(email_request: EmailRequestMatch):
    result = send_email(
        to_email=email_request.to_email,
        subject="Notificación Nuevo Match",
        body=None,
        template="app/templates/match_confirmation.html",
        context = {
            "name1": email_request.name1,
            "name2": email_request.name2,
            "pet_name1": email_request.pet_name1,
            "pet_name2": email_request.pet_name2
        }
    )

    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["message"])

    return result
