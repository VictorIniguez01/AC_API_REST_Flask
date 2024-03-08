from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Coto(Base):
    __tablename__ = 'residents_coto'

    id = Column(Integer, primary_key=True)
    coto_name = Column(String(255))

    def __repr__(self):
        return f"""
            'id': {self.id},
            'name': {self.coto_name}
        """
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.coto_name
        }

class House(Base):
    __tablename__ = 'residents_house'

    id = Column(Integer, primary_key=True)
    house_address = Column(String(255))
    coto_id = Column(ForeignKey('residents_coto.id'))

    coto = relationship('Coto', backref='residents_house')

    def __repr__(self):
        return f"""
            'id': {self.id},
            'address': {self.house_address},
            'coto_id': {self.coto_id}
        """
    
    def to_json(self):
        return {
            'id': self.id,
            'address': self.house_address,
            'coto_id': self.coto_id
        }

class Resident(Base):
    __tablename__ = 'residents_resident'
    
    id = Column(Integer, primary_key=True)
    resident_name = Column(String(255))
    resident_last_name = Column(String(255))
    resident_cellphone_number = Column(Integer)
    house_id = Column(ForeignKey('residents_house.id'))

    house = relationship('House', backref='residents_resident')

    def __repr__(self):
        return f"""
            'id': {self.id},
            'name': {self.resident_name},
            'last_name': {self.resident_last_name},
            'cellphone number': {self.resident_cellphone_number},
            'house_id': {self.house_id}
        """
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.resident_name,
            'last_name': self.resident_last_name,
            'cellphone number': self.resident_cellphone_number,
            'house_id': self.house_id
        }