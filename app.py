# from crypt import methods
from turtle import color
from flask import Flask, escape, request, render_template
import pickle
model = pickle.load(open("Final_model_news.pkl",'rb'))
vector = pickle.load(open("vectorizer2.pkl",'rb'))

#initialize Tfidfvectorizer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Home.html")
@app.route('/Prediction')
def Prediction():
    return render_template("index.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/home')
def Home():
    return render_template("home.html")
@app.route('/Check',methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        news = str(request.form['news'])
        print(news)
        pred = model.predict(vector.transform([news]))[0]
        print(pred)
        if pred == "REAL":
            color = "white"
        with open("Predict.txt",'w') as f:
            f.write(pred)
        return render_template("index.html",prediction_text=f"{pred} ".format(pred))
    else:
        return render_template("index.html")
if __name__=='__main__':
    app.run()