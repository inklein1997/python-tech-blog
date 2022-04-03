from turtle import back
from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates, relationship
import bcrypt

salt = bcrypt.gensalt()

class Users(Base):
  __tablename__ = 'users'
  id = Column('id', Integer, primary_key=True)
  user = Column('user', String(50), nullable=False)
  password = Column('password', String(100), nullable=False)
  
  
  posts = relationship('Posts',  backref="user")
  comments = relationship('Comments', backref="user")
  
  
  @validates('email')
  def validate_email(self, key, email):
    # make sure email address contains @ character
    assert '@' in email

    return email

  @validates('password')
  def validate_password(self, key, password):
    assert len(password) > 4
    return bcrypt.hashpw(password.encode('utf-8'), salt)
  
  def verify_password(self, password):
    return bcrypt.checkpw(
    password.encode('utf-8'),
    self.password.encode('utf-8')
  )