from api import app

application = app.create_app()

if __name__ == "__main__":
    application.run(host='0.0.0.0')
