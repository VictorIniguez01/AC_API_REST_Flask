from models.residence import Coto, Resident
from models.base import db

class Card(db.Model):
    __tablename__ = 'devices_card'

    id = db.Column(db.Integer, primary_key=True)
    card_code = db.Column(db.String(255))
    resident_id = db.Column(db.ForeignKey('residents_resident.id'))

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

class User(db.Model):
    __tablename__ = 'webapp_user'

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(255))
    username = db.Column(db.String(255))
    mqtt_topic = db.Column(db.String(100))
    is_coto = db.Column(db.Boolean)

    device = db.relationship('Device', backref='webapp_user')

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

class Device(db.Model):
    __tablename__ = 'devices_device'

    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(255))
    coto_id = db.Column(db.ForeignKey('residents_coto.id'))
    user_id = db.Column(db.ForeignKey('webapp_user.id'))

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