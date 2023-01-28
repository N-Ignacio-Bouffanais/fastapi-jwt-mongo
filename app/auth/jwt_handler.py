import time
import jwt
from decouple import config

JWT_SECRET = config('JWT_SECRET_KEY')
JWT_ALGORITHM = config('JWT_ALGORITHM')

# Function returns the generated token (JWT)
def token_response(token:str):
    return{
        "access_token":token,
    }


# Function used to sign the JWT string
def signJWT(userID:str):
    payload = {
        "UserID":userID,
        "expiry":time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token:str):
    try:
        decodeToken = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decodeToken if decodeToken['expires'] >= time.time() else None
    except:
        return {}

