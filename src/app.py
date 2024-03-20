from flask import Flask
from config import config
from models.entities import base

#routes
from routes import Visitor

app = Flask(__name__)

def page_not_found(error):
    return '<h1>Page not found</h1>', 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(Visitor.main, url_prefix='/api/visitors')

    app.register_error_handler(404, page_not_found)
    base.db.init_app(app)
    app.run()