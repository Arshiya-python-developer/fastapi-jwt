# the function of this file is to ckeck whether the request is authorized
# or not {verication of the protected route}

from typing import Optional
from fastapi import Request , HTTPException
from fastapi.security import HTTPBearer , HTTPAuthorizationCredentials
from fastapi.security.http import HTTPAuthorizationCredentials
from starlette.requests import Request
from .jwt_handler import decodeJWT

class JwtBearer(HTTPBearer):
    def __init__(self , auto_Error: bool = True):
        super(JwtBearer,self).__init__(auto_error=auto_Error)


    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JwtBearer
        ,self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403,detail="invalid or expred token")
            return credentials.credentials
        else :
            raise HTTPException(status_code=403,detail="invalid or expred token")


    # veridy token is valid or not 
    def verify_jwt(self,jwtoken:str):
        is_token_valid: bool = False
        payload = decodeJWT(jwtoken)
        if payload:
            is_token_valid = True
        return is_token_valid




