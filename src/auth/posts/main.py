from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from mydb import crud
from mydb.database import get_db, session, engine
from mod import schemas, models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post('/posts/', response_model=schemas.ReadPost)#
def create_post_API(post: schemas.DatabaseCreatePost, db: Session = Depends(get_db)):
    new_post = crud.create_post(db=db, new_post=post)
    return new_post


@app.get('/posts/{post_id}', response_model=schemas.ReadPost)
def read_post_API(post_id: int, db: Session = Depends(get_db)):
    read_post = crud.get_post_by_id(db=db, id=post_id)
    if read_post is None:
        raise HTTPException(status_code=404, detail="Пост не найден")
    return read_post


@app.put('/posts/{post_id}', response_model=schemas.UpdatePost)
def update_post(post_id: int, new_post: schemas.UpdatePost, db: Session = Depends(get_db)):
    upd_post = crud.update_post(db=db, post_id=post_id, new_post=new_post)
    return upd_post


@app.delete('/posts/{post_id}', response_model=str)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    del_post = crud.get_post_by_id(db=db, id=post_id)
    if del_post is None:
        raise HTTPException(status_code=404, detail="Пост не найден")
    db.delete(del_post)
    db.commit()
    return "Пост успешно удален"