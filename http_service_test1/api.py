from fastapi import APIRouter,Request ,status
from pydantic import BaseModel
from typing import Optional,List
from sqlalchemy.sql import and_,exists
from fastapi.responses import JSONResponse



router = APIRouter()

class RspModel(BaseModel):
    ret:str
    msg:str
    content:Optional[dict]
    time:Optional[str]


class UserModel(BaseModel):
    username:str
    age:int
    height:int
    weight:int
    like_food:Optional[str]
    like_exercise:Optional[str]
    like_movies:Optional[str]
    like_people:Optional[str]

@router.post('add_user',response_model=RspModel)
async def create_user(request:Request,query:UserModel) -> JSONResponse:
    user = User(**query.dict())
    sess = request.app.sess()
    _status = False

    try:
        if not sess.query(exists().where(
            and_(
                User.username == query.username,
                User.age == query.age,
                User.height == query.heihgt,
                User.weight == query.weight,
                User.like_food == query.like_food,
                User.like_exercise == query.like_exercise,
                User.like_movies == query.like_movies,
                User.like_people == query.like_people
            )
        )).scalar():
            sess.add(user)
            sess.commit()
            _status=True
    except Exception as err:
        sess.rollback()
    sess.close()
    if status:
        _content = RspModel(
            msg="insert success",
            content=query.dict(),
            ret = 0,

        )
        return JSONResponse(content=_content,status_code=status.HTTP_200_OK)



