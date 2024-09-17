

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about')
def about():
    return "This is a simple DevOps project to showcase CI/CD and Docker."

if __name__ == "__main__":
    app.run(debug=True)







# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Welcome to my Flask App!"

# @app.route('/about')
# def about():
#     return "This is a simple DevOps project to showcase CI/CD and Docker."

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
