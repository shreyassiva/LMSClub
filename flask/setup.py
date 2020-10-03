from flask import 	

app = Flask(__name__)

@app.route("/")
def home():
  return "hello this is the main page <h1>Hello shreyas we are going to take a part of your life and share it with the world one day you were very happy the End Just kidding you were very happy on that day becasue it was your birthday when you were turning 11 on that day in the morning your parents called you to come look at the hall when you went there it was full of gifts and there was three gifts which were big they were scooter,monoply and a gyroscope on that day you were allowed to play games which were rarley played by my friends .<h1>"

if __name__=="__main__":
  app.run()