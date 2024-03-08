from sqlalchemy import Column, String,ForeignKey, DateTime, Boolean, Integer
from sqlalchemy.orm import relationship
from models.base import Base
from models.residence import House

class Visitor(Base):
    __tablename__ = 'visitors_visitor'

    id = Column(Integer, primary_key=True)
    visitor_name = Column(String(255))
    visitor_last_name = Column(String(255))
    visitor_car_brand = Column(String(255))
    visitor_car_model = Column(String(255))
    visitor_car_plate = Column(String(255))
    visitor_car_color = Column(String(255))
    visitor_entry_datetime = Column(DateTime(timezone=True))
    visitor_going_coto = Column(Boolean)
    visitor_is_entry = Column(Boolean)
    house_id = Column(ForeignKey('residents_house.id'))

    house = relationship('House', backref='visitors_visitor')

    def __repr__(self):
        return """
            'id': {self.id},
            'name': {self.visitor_name},
            'last_name': {self.visitor_last_name},
            'car': '{'
                'brand': {self.visitor_car_brand},
                'model': {self.visitor_car_model},
                'plate': {self.visitor_car_plate},
                'color': {self.visitor_car_color}
            '}',
            'entry_datetime': {self.visitor_entry_datetime},
            'flags': '{'
                'goint_coto': {self.visitor_going_coto},
                'is_entry': {self.visitor_is_entry}
            '}',
            'house_id': {self.house_id}
        """
        
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.visitor_name,
            "last_name": self.visitor_last_name,
            "car": {
                "brand": self.visitor_car_brand,
                "model": self.visitor_car_model,
                "plate": self.visitor_car_plate,
                "color": self.visitor_car_color
            },
            "entry_datetime": self.visitor_entry_datetime,
            "flags": {
                "goint_coto": self.visitor_going_coto,
                "is_entry": self.visitor_is_entry
            },
            "house_id": self.house_id
        }