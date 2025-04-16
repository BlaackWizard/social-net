from sqlalchemy.orm import Session
from mod.models import models, schemas


def get_post_by_id(db: Session, id: int):
    return db.query(models.Posts).filter(models.Posts.id == id).first()


def create_post(db: Session, new_post: schemas.DatabaseCreatePost):
    db_post = models.Posts(title=new_post.title,
                           content=new_post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post




#def update_task(db: Session, task_id: int, new_task: schemas.UpdateTask):
#    db_update = get_task_by_id(db=db, id=task_id)
#    for k, v in new_task.model_dump().items():
#        if k is not None:
#            setattr(db_update, k, v)
#    db.commit()
#    db.refresh(db_update)
#    return db_update


def update_post(db: Session, post_id: int, new_post: schemas.UpdateTask):
    db_update = get_post_by_id(db=db, id=post_id)
    for k, v in new_post.model_dump().items():
        if k is not None:
            setattr(db_update, k, v)
    db.commit()
    db.refresh(db_update)
    return db_update