from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
   return ("hello interns")

@app.route('/next/')
def whatnext():
   return ("Project to be followed")

if __name__ == '__main__':
   app.run(debug=True)