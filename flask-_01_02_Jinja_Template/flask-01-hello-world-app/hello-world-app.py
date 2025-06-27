from flask import Flask 

app = Flask(__name__)

@app.route("/")
def home(): 
  return "Hello World!"


@app.route("/bye")
def thend(): 
  return "<h1> Good Bye. Come Again</h1>"



if __name__ == '__main__':
  app.run(port=8080)
