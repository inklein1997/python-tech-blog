from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Comments(Base):
  __tablename__ = 'comments'
  id = Column('id', Integer, primary_key=True)
  content = Column('content',String(500))
  created_at = Column('created_at', DateTime, default=datetime.now)
  post_id = Column('post_id', Integer, ForeignKey("posts.id"))
  user_id = Column('user_id', Integer, ForeignKey("users.id"))