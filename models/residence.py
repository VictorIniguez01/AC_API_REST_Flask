from models.base import db

class Coto(db.Model):
    __tablename__ = 'residents_coto'

    id = db.Column(db.Integer, primary_key=True)
    coto_name = db.Column(db.String(255))

    house = db.relationship('House', backref='residents_coto')
    device = db.relationship('Device', backref='residents_coto')

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
    __tablename__ = 'residents_house'

    id = db.Column(db.Integer, primary_key=True)
    house_address = db.Column(db.String(255))
    coto_id = db.Column(db.ForeignKey('residents_coto.id'))

    resident = db.relationship('Resident', backref='residents_house')
    visitor = db.relationship('Visitor', backref='residents_house')

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
    __tablename__ = 'residents_resident'
    
    id = db.Column(db.Integer, primary_key=True)
    resident_name = db.Column(db.String(255))
    resident_last_name = db.Column(db.String(255))
    resident_cellphone_number = db.Column(db.Integer)
    house_id = db.Column(db.ForeignKey('residents_house.id'))

    card = db.relationship('Card', backref='residents_resident')

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