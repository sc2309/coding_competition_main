from flask import Flask

def myFirstApp():
    app = Flask(__name__)
    from views import views
    from sports import sports
    from fitness import fitness
    from login import login
    from signup import signup
    from diet import diet
    app.register_blueprint(diet, url_prefix='/')
    app.register_blueprint(sports, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(fitness, url_prefix='/')
    app.register_blueprint(login, url_prefix='/')
    app.register_blueprint(signup, url_prefix='/')
    return app

app = myFirstApp()
app.run(debug=True)