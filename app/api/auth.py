import os
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

load_dotenv()

BRONIFY_TOKEN = os.getenv("BRONIFY_TOKEN")

security = HTTPBearer()


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != BRONIFY_TOKEN:
        print("Credentials:", credentials.credentials)
        print("Expected Token:", BRONIFY_TOKEN)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token"
        )
