import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'myCookBook'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

#DB = mongo.db

@app.route('/')
def home_template():
    return render_template('home.html')

@app.route('/get_recipes')
def get_recipes():
    """
    retrieve the recipes from the database and render below into the template
    
    """
    return render_template('recipes.html', recipes=mongo.db.recipes.find())


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=(os.environ.get("PORT")),
            debug=True)