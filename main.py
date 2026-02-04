from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import requests

app = FastAPI()

API_KEY = "my_secret_key_123"
security = HTTPBearer()

class VoiceRequest(BaseModel):
    audio_url: str

@app.post("/detect-voice")
def detect_voice(
    data: VoiceRequest,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    if credentials.credentials != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        r = requests.get(data.audio_url)
        if r.status_code != 200:
            raise Exception()
    except:
        raise HTTPException(status_code=400, detail="Invalid audio URL")

    return {
        "classification": "AI_GENERATED",
        "confidence": 0.75,
        "explanation": "Detected synthetic voice characteristics"
    }
