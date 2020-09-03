import os
from flask import Flask, render_template, redirect, request, session, flash, url_for
from datetime import date
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "myCookBook"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def home_template():
    return render_template("home.html")


@app.route("/login_user", methods=["GET", "POST"])
def login_user():
    if request.method == "POST":
        users = mongo.db.users
        valid_login = users.find_one({"username": request.form["username"]})
        if valid_login:
            if (
                bcrypt.hashpw(
                    request.form["password"].encode("utf-8"), valid_login["password"]
                )
                == valid_login["password"]
            ):
                session["username"] = request.form["username"]
                session["logged_in"] = True
                return redirect(url_for("home_template"))
        flash("Invalid username / password. Please try again.")
    return render_template("login.html", login_page=True)


@app.route("/register_user", methods=["POST", "GET"])
def register_user():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one(
            {"username": request.form.get("username").lower()}
        )
        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form["password"].encode("utf-8"), bcrypt.gensalt()
            )
            users.insert_one(
                {"username": request.form["username"], "password": hashpass,}
            )
            session["username"] = request.form["username"]
            flash(
                "Thank you for registering, please login to view more recipes and add your own!"
            )
            return redirect(url_for("login_user"))
        flash("Username already exists")
    return render_template("register.html", login_page=True)


@app.route("/logout_user")
def logout_user():
    if "username" in session:
        session["logged_in"] = False
        session.pop("username")
        flash("You were logged out.")
    return render_template("home.html")


@app.route("/user_recipes")
def user_recipes():
    recipe = mongo.db.recipes.find({"added_by": session["username"]})
    return render_template("recipes.html", recipe=recipe, user_recipes=True)


@app.route("/get_recipes")
def get_recipes():
    """retrieve the recipes from the database and render below into the template"""
    return render_template("recipes.html", recipe=mongo.db.recipes.find())


@app.route("/add_recipe")
def add_recipe():
    return render_template(
        "addrecipe.html",
        cuisines=mongo.db.cuisines.find().sort("cuisine"),
        cooktime=mongo.db.cooktime.find(),
        recipetype=mongo.db.recipetype.find().sort("recipe_type"),
        servings=mongo.db.servings.find(),
    )


@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    today = date.today()
    today_date = today.strftime("%d %B %Y")
    recipe = mongo.db.recipes
    recipe.insert_one(
        {
            "name": request.form.get("name"),
            "cuisine": request.form.get("cuisine"),
            "recipe_type": request.form.get("recipe_type"),
            "cooking_time": request.form.get("cooking_time"),
            "serves": request.form.get("serves"),
            "description": request.form.get("description"),
            "ingredients": request.form.get("ingredients"),
            "instruction": request.form.get("instruction"),
            "recipe_img": request.form.get("recipe_img"),
            "added_date": today_date,
            "added_by": session["username"],
        }
    )
    flash("Your Recipe has been Added Sucessfully")
    return redirect(url_for("get_recipes"))


@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("viewrecipe.html", recipe=the_recipe)


@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    the_owner = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if session["username"] == the_owner["added_by"]:
        the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        all_cuisines = mongo.db.cuisines.find().sort("cuisine")
        all_recipetype = mongo.db.recipetype.find().sort("recipe_type")
        all_servings = mongo.db.servings.find()
        all_cooktimes = mongo.db.cooktime.find()
        return render_template(
            "editrecipe.html",
            recipe=the_recipe,
            cuisines=all_cuisines,
            recipetype=all_recipetype,
            servings=all_servings,
            cooktime=all_cooktimes,
        )
    else:
        return redirect(url_for("get_recipes"))


@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    today = date.today()
    today_date = today.strftime("%d %B %Y")
    recipe = mongo.db.recipes
    recipe.update(
        {"_id": ObjectId(recipe_id)},
        {
            "name": request.form.get("name"),
            "cuisine": request.form.get("cuisine"),
            "recipe_type": request.form.get("recipe_type"),
            "cooking_time": request.form.get("cooking_time"),
            "serves": request.form.get("serves"),
            "description": request.form.get("description"),
            "ingredients": request.form.get("ingredients"),
            "instruction": request.form.get("instruction"),
            "recipe_img": request.form.get("recipe_img"),
            "added_date": request.form.get("added_date"),
            "updated_date": today_date,
            "added_by": session["username"],
        },
    ),
    flash("Your Recipe has been Updated Sucessfully")
    return redirect(url_for("get_recipes"))


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/search_recipe", methods=["POST"])
def search_recipe():
    find_recipes = request.form.get("find_recipes")
    mongo.db.recipes.create_index([("$**", "text")])
    recipe = recipe = mongo.db.recipes.find({"$text": {"$search": find_recipes}})
    return render_template("search.html", recipe=recipe, find=True)


@app.route("/likes/<recipe_id>")
def likes(recipe_id):

    the_recipe = mongo.db.recipes.find_one_and_update(
        {"_id": ObjectId(recipe_id)}, {"$inc": {"likes": 1}}
    )
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return redirect(url_for("view_recipe", recipe_id=recipe_id))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=(os.environ.get("PORT")), debug=True)

