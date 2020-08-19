import os
from flask import Flask, render_template, redirect, request, session, flash, url_for
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

@app.errorhandler(404)
def error_handler(e):
    return render_template('404.html')



@app.route('/get_recipes')
def get_recipes():
    """
    retrieve the recipes from the database and render below into the template
    
    """
    return render_template('recipes.html', recipe=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                            cuisines=mongo.db.cuisines.find()
                            .sort("cuisine"),
                            cooktime=mongo.db.cooktime.find(),
                            recipetype=mongo.db.recipetype.find()
                            .sort("recipe_type"),
                            servings=mongo.db.servings.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipes
    recipe.insert_one({
        'name': request.form.get('name'),
        'cuisine': request.form.get('cuisine'),
        'recipe_type': request.form.get('recipe_type'),
        'cook_time': request.form.get('cook_time'),
        'serves': request.form.get('serves'),
        'description': request.form.get('description'),
        'ingredients': request.form.get('ingredients'),
        'instruction': request.form.get('instruction'),
        'recipe_img': request.form.get('recipe_img'),
        'added_date': request.form.get('added_date')
    })
    return redirect(url_for('get_recipes'))
    







if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=(os.environ.get("PORT")),
            debug=True)