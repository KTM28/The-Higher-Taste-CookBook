import os
import math
from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'myCookBook'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route('/')
def home_template():
    return render_template('home.html')



@app.route('/get_recipes')
def get_recipes():
    """retrieve the recipes from the database and render below into the template"""
    return render_template('recipes.html', recipe = mongo.db.recipes.find())



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
        'cooking_time': request.form.get('cooking_time'),
        'serves': request.form.get('serves'),
        'description': request.form.get('description'),
        'ingredients': request.form.get('ingredients'),
        'instruction': request.form.get('instruction'),
        'recipe_img': request.form.get('recipe_img'),
        'added_date': request.form.get('added_date')
    })
    return redirect(url_for('get_recipes'))
    

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    try:
        the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        return render_template('viewrecipe.html', recipe=the_recipe)
    except Exception:
        return render_template("404.html")

        
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines = mongo.db.cuisines.find().sort("cuisine")
    all_recipetype = mongo.db.recipetype.find().sort("recipe_type")
    all_servings = mongo.db.servings.find()
    all_cooktimes = mongo.db.cooktime.find()
    return render_template('editrecipe.html', recipe=the_recipe,
                            cuisines=all_cuisines,
                            recipetype=all_recipetype,
                            servings=all_servings,
                            cooktime=all_cooktimes)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes
    recipe.update({'_id': ObjectId(recipe_id)},
                { 
                'name': request.form.get('name'),
                'cuisine': request.form.get('cuisine'),
                'recipe_type': request.form.get('recipe_type'),
                'cooking_time': request.form.get('cooking_time'),
                'serves': request.form.get('serves'),
                'description': request.form.get('description'),
                'ingredients': request.form.get('ingredients'),
                'instruction': request.form.get('instruction'),
                'recipe_img': request.form.get('recipe_img'),
                'added_date': request.form.get('added_date')
                })
    flash('Your Recipe has been Updated Sucessfully')
    return redirect(url_for('get_recipes'))






if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=(os.environ.get("PORT")),
            debug=True)