from mydb.database import Base
from sqlalchemy.orm import mapped_column, Mapped

class Posts(Base):
    __tablename__ =  'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str]


