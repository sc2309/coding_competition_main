from flask import Flask

def myFirstApp():
    app = Flask(__name__)
    from views import views
    from diet import diet
    app.register_blueprint(diet, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    return app

app = myFirstApp()
app.run(debug=True)