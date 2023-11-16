from flask import Flask
from views import views
from sports import sports
from fitness import fitness
from about import about
from contact import contact
from login import login
from signup import signup
from diet import diet
from routines import routines
from signup2 import signup2
from feedback import feedback
from store_data import store_data

def create_app():
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(sports, url_prefix='/')
    app.register_blueprint(fitness, url_prefix='/')
    app.register_blueprint(about, url_prefix='/')
    app.register_blueprint(contact, url_prefix='/')
    app.register_blueprint(login, url_prefix='/')
    app.register_blueprint(signup, url_prefix='/')
    app.register_blueprint(diet, url_prefix='/')
    app.register_blueprint(routines, url_prefix='/')
    app.register_blueprint(signup2, url_prefix='/')
    app.register_blueprint(store_data, url_prefix='/')
    app.register_blueprint(feedback, url_prefix='/')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
