from flask import Flask, render_template, request
import pickle

tokenizer = pickle.load(open("models/cv.pkl","rb"))
model = pickle.load(open("models/clf.pkl", "rb"))

#initialize the flask
app = Flask(__name__) 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])