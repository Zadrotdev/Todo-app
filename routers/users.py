from typing import Annotated
from schemas import UserChangePassword
from fastapi import APIRouter, Depends, status, HTTPException

from general import db_dependency
from models import User
from routers.auth import get_current_user

router = APIRouter(prefix="/user", tags=["user"])

user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/me", status_code=status.HTTP_200_OK)
async def get_me(db: db_dependency, user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="UnAUTH")
    print(user)
    user_model = db.query(User).filter(User.id == user.get("id")).first()
    return {"data": user_model}


# @router.post("/change-password", status_code=status.HTTP_200_OK)
# async def change_password(db: db_dependency, user: user_dependency, user_request: UserChangePassword):
#     if user is None:
#         raise HTTPException(status_code=401, detail="UnAUTH")
#
#     user_model: User = db.query(User).filter(User.id == user.get("id")).first()
#
#     if user_model.password == user_request

