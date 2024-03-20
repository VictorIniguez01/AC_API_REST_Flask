from models.entities.base import db

class Card(db.Model):
    __tablename__ = 'Card'

    id = db.Column(db.Integer, primary_key=True)
    card_code = db.Column(db.String(32))
    resident_id = db.Column(db.ForeignKey('Resident.id'))

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
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(20))
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    mqtt_topic = db.Column(db.String(50))
    is_coto = db.Column(db.Boolean)

    device = db.relationship('Device', backref='User')

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
    __tablename__ = 'Device'

    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(20))
    coto_id = db.Column(db.ForeignKey('Coto.id'))
    user_id = db.Column(db.ForeignKey('User.id'))

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