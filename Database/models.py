from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from Database.session import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    is_admin = Column(Boolean, default=False)
    join_date = Column(DateTime)
    
    subscriptions = relationship("Subscription", back_populates="user")

class Group(Base):
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, unique=True)
    title = Column(String)
    force_sub_enabled = Column(Boolean, default=True)
    
    channels = relationship("GroupChannel", back_populates="group")

class Channel(Base):
    __tablename__ = 'channels'
    
    id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, unique=True)
    username = Column(String)
    title = Column(String)
    is_verified = Column(Boolean, default=False)

class GroupChannel(Base):
    __tablename__ = 'group_channels'
    
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.id'))
    channel_id = Column(Integer, ForeignKey('channels.id'))
    
    group = relationship("Group", back_populates="channels")
    channel = relationship("Channel")

class Subscription(Base):
    __tablename__ = 'subscriptions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    channel_id = Column(Integer, ForeignKey('channels.id'))
    join_date = Column(DateTime)
    
    user = relationship("User", back_populates="subscriptions")
