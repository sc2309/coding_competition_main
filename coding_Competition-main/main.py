from flask import Flask

def myFirstApp():
    app = Flask(__name__)
    from views import views
    app.register_blueprint(views, url_prefix='/')
    return app

app = myFirstApp()
app.run(debug=True)