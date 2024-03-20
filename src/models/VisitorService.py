from models.entities import Visitor

class VisitorService():

    @classmethod
    def get_visitors(cls):
        try:
            result = Visitor.Visitor.query.all()
            visitors = [visitor.to_json() for visitor in result]
            return visitors
        except Exception as e:
            return {'Error': str(e)}