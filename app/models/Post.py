from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Post(Base):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'))
  # datime module python built in to generate timestamps
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

  user = relationship('User')

#In MySQL, an ON DELETE CASCADE statement deletes the corresponding foreign key records when a record from the specified table is deleted. In this case, deleting a post from the database also deletes all its associated comments.
  comments = relationship('Comment', cascade='all,delete')