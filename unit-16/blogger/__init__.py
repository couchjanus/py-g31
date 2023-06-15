from  flask import Flask
import os

# app = Flask(__name__)

# @app.route('/hello')
# def hello():
#     return 'Hello World'

def create_app():
    app = Flask(__name__, instance_relative_config=True )
        
    app.config.from_mapping(
        SECRET_KEY="Bala bala bal",
        DATABASE=os.path.join(app.instance_path, 'blogger.sqldb')    
    )
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello World'
    
    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    return app
