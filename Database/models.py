from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True, nullable=False)
    username = Column(String(50))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    is_admin = Column(Boolean, default=False)
    join_date = Column(DateTime, nullable=False)
    last_active = Column(DateTime)
    
    subscriptions = relationship("Subscription", back_populates="user")

class Group(Base):
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, unique=True, nullable=False)
    title = Column(String(100), nullable=False)
    force_sub_enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False)
    
    channels = relationship("GroupChannel", back_populates="group")

class Channel(Base):
    __tablename__ = 'channels'
    
    id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, unique=True, nullable=False)
    username = Column(String(50))
    title = Column(String(100), nullable=False)
    is_verified = Column(Boolean, default=False)
    added_at = Column(DateTime, nullable=False)

class GroupChannel(Base):
    __tablename__ = 'group_channels'
    
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    channel_id = Column(Integer, ForeignKey('channels.id'), nullable=False)
    added_by = Column(Integer, nullable=False)
    added_at = Column(DateTime, nullable=False)
    
    group = relationship("Group", back_populates="channels")
    channel = relationship("Channel")

class Subscription(Base):
    __tablename__ = 'subscriptions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    channel_id = Column(Integer, ForeignKey('channels.id'), nullable=False)
    join_date = Column(DateTime, nullable=False)
    
    user = relationship("User", back_populates="subscriptions")
