# responsible for signing for encoding & decoding& return jwt tokens


import time
import jwt
from decouple import config


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")



# Function returns the generated tokens
def token_response(token: str):
    return {
        "access token": token
        }


# Function used for siginig the jwt 
def SignJWT(userID:str):
    payload = {
        "userID": userID,
        "expiration":time.time() + 600
    }
    token = jwt.encode(payload,JWT_SECRET,algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token,JWT_SECRET,algorithm=JWT_ALGORITHM)
        return decode_token if decode_token["expiration"] >= time.time() else None
    except:
        return {}


