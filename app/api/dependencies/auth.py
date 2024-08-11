from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.services.users import UserService

security = HTTPBasic()


async def get_current_login(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    is_auth = await UserService.is_auth_admin(
        credentials.username,
        credentials.password,
    )

    if not is_auth:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
