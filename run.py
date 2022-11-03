from new_app import myapp
from new_app.boards.views import boards
myapp.register_blueprint(boards)

if __name__ == "__main__":
    myapp.run()
