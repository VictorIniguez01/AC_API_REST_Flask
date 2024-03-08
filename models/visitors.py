from models.residence import House
from models.base import db

class Visitor(db.Model):
    __tablename__ = 'visitors_visitor'

    id = db.Column(db.Integer, primary_key=True)
    visitor_name = db.Column(db.String(255))
    visitor_last_name = db.Column(db.String(255))
    visitor_car_brand = db.Column(db.String(255))
    visitor_car_model = db.Column(db.String(255))
    visitor_car_plate = db.Column(db.String(255))
    visitor_car_color = db.Column(db.String(255))
    visitor_entry_datetime = db.Column(db.DateTime(timezone=True))
    visitor_going_coto = db.Column(db.Boolean)
    visitor_is_entry = db.Column(db.Boolean)
    house_id = db.Column(db.ForeignKey('residents_house.id'))

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