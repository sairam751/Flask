from flask import Flask


###WSGI Application
app = Flask(__name__)

#decorator
@app.route("/")
def welcome():
    return "Welcome to flask app run by Sai Ram. Developed to practise flask after making debut is equal to true"

if __name__ == "__main__":
    app.run(debug=True)