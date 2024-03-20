from flask import Blueprint, jsonify
from models.entities.Visitor import Visitor

from models.VisitorService import VisitorService

main = Blueprint('visitor_blueprint', __name__)

@main.get('/')
def get_visitor():
    try:
        visitors = VisitorService.get_visitors()
        return jsonify(visitors)
    except Exception as e:
        raise Exception(e)