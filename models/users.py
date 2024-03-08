from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.residence import Resident, Coto

class Card(Base):
    __tablename__ = 'devices_card'

    id = Column(Integer, primary_key=True)
    card_code = Column(String(255))
    resident_id = Column(ForeignKey('residents_resident.id'))

    resident = relationship('Resident', backref='devices_card')

    def __repr__(self):
        return f"""
            'id': {self.id},
            'code': {self.card_code},
            'resident_id': {self.resident_id}
        """
    
    def to_json(self):
        return {
            'id': self.id,
            'code': self.card_code,
            'resident_id': self.resident_id
        }

class User(Base):
    __tablename__ = 'webapp_user'

    id = Column(Integer, primary_key=True)
    password = Column(String(255))
    username = Column(String(255))
    mqtt_topic = Column(String(100))
    is_coto = Column(Boolean)

    def __repr__(self) -> str:
        return f"""
            'id': {self.id},
            'username': {self.username},
            'mqtt_topic': {self.mqtt_topic},
            'is_coto': {self.is_coto}
        """
    
    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'mqtt_topic': self.mqtt_topic,
            'is_coto': self.is_coto
        }

class Device(Base):
    __tablename__ = 'devices_device'

    id = Column(Integer, primary_key=True)
    device_name = Column(String(255))
    coto_id = Column(ForeignKey('residents_coto.id'))
    user_id = Column(ForeignKey('webapp_user.id'))

    coto = relationship('Coto', backref='devices_device')
    user = relationship('User', backref='devices_device')

    def __repr__(self):
        return f"""
            'id': {self.id},
            'name': {self.device_name},
            'coto_id': {self.coto_id},
            'user_id': {self.user_id}
        """
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.device_name,
            'coto_id': self.coto_id,
            'user_id': self.user_id
        }