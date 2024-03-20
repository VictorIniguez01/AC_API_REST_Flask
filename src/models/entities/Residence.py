from models.entities.base import db

class Coto(db.Model):
    __tablename__ = 'Coto'

    id = db.Column(db.Integer, primary_key=True)
    coto_name = db.Column(db.String(20))

    house = db.relationship('House', backref='Coto')
    device = db.relationship('Device', backref='Coto')

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

class House(db.Model):
    __tablename__ = 'House'

    id = db.Column(db.Integer, primary_key=True)
    house_address = db.Column(db.String(20))
    coto_id = db.Column(db.ForeignKey('Coto.id'))

    resident = db.relationship('Resident', backref='House')
    visitor = db.relationship('Visitor', backref='House')

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

class Resident(db.Model):
    __tablename__ = 'Resident'
    
    id = db.Column(db.Integer, primary_key=True)
    resident_name = db.Column(db.String(50))
    resident_last_name = db.Column(db.String(50))
    resident_cellphone_number = db.Column(db.Integer)
    house_id = db.Column(db.ForeignKey('House.id'))

    card = db.relationship('Card', backref='Resident')

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