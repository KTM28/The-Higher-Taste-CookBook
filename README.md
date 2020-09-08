# The Higher Taste - Online Recipe Book
### Milestone Three project: Data Centric Development – Code Institute
The Higher Taste is an online web application designed for users to find recipes added by other users and share their own recipes.

## Demo
A demo of the website can be found [HERE]( https://the-higher-taste-cookbook.herokuapp.com/).

## Table of Contents
1. [**Project overview**](#project-overview)
2. [**UX**](#ux)
  - [**User Stories**](#user-stories)
  - [**Design**](#design)
    - [**Libraries**](#libraries)
    - [**Main Color Scheme**](#main-colour-scheme)
  - [**Wireframes**](#wireframes)
 
3. [**Features**](#features)
   - [**Existing Features**](#existing-features)
   - [**Features Left to Implement**](#features-left-to-implemement)
 
4. [**Technologies Used**](#technologies-used)
 
5. [**Database Schema**](#database-schema)
6. [**Testing**](#testing)
7. [**Deployment**](#deployment)
8. [**Running Code Locally**](#running-code-locally)
8. [**Credits**](#credits)
  - [**Code**](#code)
  - [**Media**](#media)
  - [**Acknowledgements**](#acknowledgements)

## Project overview
 The Higher Taste was built using [Python](https://www.python.org/) – programming language, [Flask]( https://palletsprojects.com/p/flask/)  – which is a Python micro framework and [MongoDB Atlas]( https://www.mongodb.com/) – a document-oriented NoSQL database.

## UX
The site is intended for users with interests in gathering information about Recipes. 
The user can:

*	Register an account
*	Add their own recipe (by registered user)
*	Edit, Update and Delete recipes (by registered user subject to if the user owns the recipe)
*	Search recipes (by cuisine)
*	Search recipes (by meal type)
*	Search recipes (by ingredients)
*	View recipe details
*	Like recipes
*	Share recipes



### User Stories
*  As a user, I want to view a list / catalogue of recipes.
* As a user I want to search recipes filtered by recipe type, recipe cuisine, recipe ingredients.
* As a user, I want to be able to create an account, to perform this I go into the website clicked into login in the nav menu and clicked the signup link found in the login page.
* As a user I want to store my own recipes, to perform this action I registered into the website and login, then  I clicked on "Add recipes", doing that I achieved my goal to store only recipes that were created by myself and have a list of my own recipes.
* As a user I want to edit my own recipes, to perform this action I logged into the website, then I clicked on "My recipes" after that “View recipes” and then on "Edit recipes", doing that I achieved my goal to edit and update recipes.
* As a user I want to delete my own recipes, to perform this action I logged into the website, then I clicked on "My recipes" after that “View recipes” and then on "Delete recipes", doing that I achieved my goal to Delete recipes.

### Design
The website is implemented with standard layout which is full responsive on mobile devices and larger screens.

#### Libraries
*	[Materialize] ( https://materializecss.com/)- A modern responsive front-end framework based on Material Design. Used for layouts
*	[Font Awesome] (https://fontawesome.com/)- For various Icons used in the website.
*	[Material Icons]  (https://material.io/resources/icons/?style=baseline)- For various Icons used in the website.
*	[jQuery] (https://jquery.com/download/)- jQuery is a fast, small, and feature-rich JavaScript library.
*	[Google Fonts] (https://fonts.google.com/)- For fonts used across the site. 

#### Main Colour Scheme
- ![#FF8008](https://placehold.it/15/FF8008/#FF8008)
- ![#DB400B](https://placehold.it/15/DB400B/#DB400B)
- ![#FFC837](https://placehold.it/15/FFC837/#FFC837)

### Wireframes
The wireframes for the project can be found [Here](static/wireframe/The-higher-Taste.png)  
##### back to [top](#table-of-contents)

## Features
### Existing Features
* **Navbar/Side navbar** - The site has fully responsive navbar which allows user to easily navigate between various pages across the sites. When the user is logged in a few extra menu items are displayed in the navigation allowing logged in user to navigate to those area of the websites. 
* **Home** - this is the landing page displayed first when the user visits the site. This page is quite intuitional and allows user to easily navigate and perform desired action. If the user is logged in, the username is displayed right above the footer prefixed by user icon. 
* **Recipes** - this page allows users to access/view all the recipes in the website. The recipes itself are displayed in the card with image and there is a button in the card where the user can click to see the detail view of the recipe.
* **My recipes** - this page can only be found and accessed when the user is logged in. It displays all the recipe the logged in user have added.
* **View recipes** - this page can be accessed via recipe page where user can click in the view button displayed in the recipe card which directs user to view full details of the recipe.
* **Add recipes** - this feature is exclusively reserved to logged in user. The link can be found in the navigation menu once the user is logged in. Users are allowed to add recipe in the website via add recipe form. The form fields are all required before submission. If the user does not add a URL for recipe image then a place holder image is generated for the added recipe. Dates are automatically added from the backend.
* **Edit/Delete Recipe** - logged in user can edit or delete a recipe exclusively owned by the logged in user.
* **Search** - Users can search for any recipe in the website through a simple search form displayed in the Landing page.
* **Register** - Allows users to register for account. The registration form layout is simple with only two fields -Username and password.
* **Log in** - Allows users to login to the account if they are registered. The Login form layout is simple with only two fields -Username and password.
* **Log out** - Allows user to logout and end the session. 
* **Like Recipe**- Like recipe button can be found in the recipe view page where a user can press the like button and the amount of likes for the recipe is incremented with each click
* **Share Recipe** - Share recipe button can be found in the recipe view page where a user can press the share button to share the particular recipe to the listed social media site.
* **Custom Error Messages** - A custom error message for 405 and 500 are included. The error page allows user to re-navigate to the home page.
* **Cancel Button** (Edit Recipe Page/Delete Modal) - Cancels the form submission when clicked and redirects the user back to the relevant Recipe Page.
* **Delete Modal** - The delete modal has delete and cancel button and is displayed as final confirmation when the user in session clicks delete button in the view recipe page.

### Features left to implement
* **Recipe page pagination** - I would like to add pagination across the site. I understand as the site grows and more users add recipes, pagination would be required to improve UX.
* **Search Form expansion** - I would like to add an extended search field in the search form where the user can filter results from the provided query. 
* **Reset Password** - A reset password feature will be added in the future.
* **User Profile image** - A feature that allows user to upload their own profile image or choose an avatar provided.
* **Advance Form input** - At this moment the entry added to the form particularly ingredients and instructions later when displayed are in-fact eye-soaring to the reader. I would like to rectify that in the future and make it more accessible to the reader with a user friendly clear formatting for the input fields.

## Technologies Used
![Bson](https://img.shields.io/badge/Bson-Version%201.1-blue)
 - [Bson](http://bsonspec.org/) - short for Bin­ary JSON, is a bin­ary-en­coded seri­al­iz­a­tion of JSON-like doc­u­ments.
2. ![Chrome Developer Tools](https://img.shields.io/badge/Chrome%20Dev%20Tools-Google%20Chrome-blue)
 - [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) - is a set of web developer tools built directly into the Google Chrome browser.
3. ![CSS3](https://img.shields.io/static/v1?label=CSS&message=3&color=1572B6&logo=css3&logoColor=ffffff)
 - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used for custom added styles.
4. ![Flask](https://img.shields.io/badge/Flask-Version%201.1.2-orange)
 - [Flask](https://flask.palletsprojects.com/en/1.1.x/) - is a web framework, it provides you with tools, libraries and technologies that allow you to build a web application.
5. ![Flask-Bcrypt](https://img.shields.io/badge/Flask--Bcrypt-0.7.1-orange)
 - [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/) - is a Flask extension that provides bcrypt hashing utilities for your application.
6. ![Flask PyMongo](https://img.shields.io/badge/Flask--PyMongo-mongodb-blue)
 - [Flask PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) - Bridges between Flask and PyMongo.
7. ![Flask Session](https://img.shields.io/badge/Flask--Session-session%20object-orange)
 - [Flask Session](https://flask.palletsprojects.com/en/1.1.x/api/#flask.session) - Flask-Session is an extension for Flask that adds support for Server-side Session to your application.
9. ![Git](https://img.shields.io/badge/Git-----fast--version--control-orange)
 - [Git](https://git-scm.com/) - open source distributed version control system.
10. ![GitHub](https://img.shields.io/badge/GitHub-Git%20repository%20hosting%20service-lightgrey)
 - [GitHub](https://github.com/) - is a Web-based hosting service for version control using Git.
11. ![GitIgnore](https://img.shields.io/badge/GitIgnore-files-royalblue)
 - [GitIgnore](https://github.com/toptal/gitignore.io) - is a web service designed to help you create .gitignore files for your Git repositories.
12. ![Heroku](https://img.shields.io/badge/Heroku-Deployment-blueviolet)
 - [Heroku](https://dashboard.heroku.com/) - lets you deploy, run and manage applications written in Ruby, Node.js, Java, Python, Clojure, Scala, Go and PHP.
13. ![HTML5](https://img.shields.io/static/v1?label=HTML&message=5&color=E34F26&logo=html5&logoColor=ffffff)
 - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - used as the base for markup text.
14. ![jQuery](https://img.shields.io/badge/jQuery-3.5.1-yellowgreen)
 - [jQuery](https://jquery.com/) - is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers.
15. ![Jinja](https://img.shields.io/badge/Jinja2-2.11.2-red)
 - [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - a full featured template engine for Python.
16. ![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-4.4-green)
 - [MongoDB Atlas](https://www.mongodb.com/) - is a document database with the scalability and flexibility that you want with the querying and indexing that you need.
17. ![Phyton](https://img.shields.io/badge/Python-3.8.3-blue)
 - [Python](https://www.python.org/downloads/release/python-383/) - is a scripting language.
18. ![PyMongo](https://img.shields.io/badge/PyMongo-2.3.0-green)
 - [PyMongo](https://docs.mongodb.com/drivers/pymongo) - is a MongoDB driver for Python used to access the MongoDB database.

## Database Schema
The database used for the backend of the project is NoSql MongoDB. You can access my database structure [Here](static/collection/databaseSchema.pdf)

## Testing
* The testing of the HTML and CSS element was done using W3C Mark Validator.  
* The testing of the JavaScript was done using babeljs.io
* minor testing of python was achieved using pep8online.com
* The website has been tested and runs in a various different browser such as Chrome, Edge, Safari and Firefox and is compatible. 
* Different screen sizes in Chrome/Edge/Firefox developer tool have been tested to ensure the website is also compatible with many popular responsive sizes.
* Manual testing of all the functions and DB connection for python in the webpage was done in the editor terminal and via environment production in the web browser. 
* All test for links and action facilitated through buttons and navigation across the web-application has performed manually in various browser and devices to check for any bugs or glitches. 
* Flask testing was facilitated through Flask debug=True in app.py

##### back to [top](#table-of-contents)



## Deployment
I used VS Code IDE for development, GitHub for my version control and Heroku to host the live version of my project. To deploy my website to Heroku, I used the following steps:
1.	Created the app in Heroku.
2.	Ran the `heroku login` command in the terminal window and entered my credentials to login to Heroku.
3.	Added and committed the files to Git using the `git add .` and `git commit -m ""` commands in the terminal window.
4.	Linked the Heroku app as the remote master branch using the following command in the terminal window:   ```heroku git:remote -a <app-name>```
5.	Ran the `git push heroku master` command in the terminal window to push the app to Heroku.
6.	Ran the `heroku: ps:scale web=1` command in the terminal window to run the app in Heroku.
7.	Entered the following Config Var in Heroku: **IP** with value **0.0.0.0** then add **PORT** as **5000** then add **SECRET_KEY** then add **MONGO_URI** and then add **MONGO_DBNAME** which is the name of database.
The app was successfully deployed to Heroku at this stage.
### Running Code Locally
1.	To run locally, clone this repository to your choice of the editor by pasting `(git clone)` `https://github.com/KTM28/ The-Higher-Taste-CookBook ` into your terminal. To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.
2.	Create a new Database in MongoDB called *_MyCookbook_* and use the schema as outlined in the [Database Schema Files]().
3.	Navigate to your IDE terminal and add your MongoDB URI in the following format:

    ```MONGO_URI="insert your mongo uri details here"```
4.	In the terminal, run the `pip3 install -r requirements.txt` command to install the requirements.txt file.
5.	You should now be able to run the app locally using the `python3 run.py` command.


## Credits
### Code
* The code for user Registration and Login system was achieved by watching [This@youtube]( https://www.youtube.com/watch?v=3uuQ3g92oPQ )
* I’ve used solutions found in stack-overflow for allowing user to like recipe.
* Error Handlers[Flask]( https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/ )  
* Share button for social media site [Here](https://www.youtube.com/watch?v=YcEshVZNA5E&t )

### Media
* logo image - Dustin –[Kindpng]( https://www.kindpng.com/) 
* Landing page-[Unsplash]( https://unsplash.com/photos/hv1MrBzGGNY ) 
* Placeholder image-[Unsplash]( https://unsplash.com/s/photos/linh-nguyen )
* Recipe images are taken from copyright free material across google search engine.
 
### Acknowledgements
 I received inspiration for this project from Code Institute - Project Ideas




