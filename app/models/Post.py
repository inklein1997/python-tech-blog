from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Posts(Base):
  __tablename__ = 'posts'
  id = Column('id', Integer, primary_key=True)
  title = Column('title', String(50))
  description = Column('description', String(300))
  user_id = Column('user_id', Integer, ForeignKey("users.id"))
  created_at = Column('created_at', DateTime, default=datetime.now)
  updated_at = Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)
