from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Boolean, DateTime
from datetime import datetime
from flask_login import UserMixin

#Create Database
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# Create Table
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password : Mapped[str] = mapped_column(String(100))
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    last_login: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    votes = relationship("UserVote", back_populates="user")
    messages = relationship("Message", back_populates="user")

class Vote(db.Model):
    post_id: Mapped[str] = mapped_column(String, primary_key=True)
    like: Mapped[int] = mapped_column(Integer, default=0)
    dislike: Mapped[int] = mapped_column(Integer, default=0)
    user_votes = relationship("UserVote", back_populates="vote")

class UserVote(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    vote_type : Mapped[str] = mapped_column(String)
    vote_post : Mapped[str] = mapped_column(String, ForeignKey('vote.post_id'), nullable=False)

    user = relationship("User", back_populates="votes")
    vote = relationship("Vote", back_populates="user_votes")

class Message(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id : Mapped[int] = mapped_column(Integer, ForeignKey('user.id', name="message_user_id"), nullable=True)
    name : Mapped[str] = mapped_column(String)
    surname : Mapped[str] = mapped_column(String)
    email : Mapped[str] = mapped_column(String)
    subject : Mapped[str] = mapped_column(String)
    message : Mapped[str] = mapped_column(String)
    read : Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    user = relationship("User", back_populates="messages")