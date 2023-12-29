# Cook Book

## Table of Contents

- [UX](#ux)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
- [Technologies Used](#technologies-used)
  - [Flask](#flask)
  - [WTForms](#wtforms)
  - [Jinja](#jinja)
  - [jQuery](#jquery)
  - [Materialize](#materialize)
  - [MongoDB Atlas](#mongodb-atlas)
  - [gunicorn](#gunicorn)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Environment Variables](#environment-variables)

## UX

### Strategy

#### Business Goals

The purpose of the business is to provide users with a social hub for sharing cooking recipes. The business will want to maximize the social aspect of the website by providing features commonly found in other social websites such as the ability to "like" and comment on users' recipes, and the ability to "follow" and be followed by other users.

#### User Goals

1. To submit one's own recipes for use by other users.
2. To find other users' recipes.
3. To save recipes for later viewing.
4. To follow and be followed by other users so they can be notified of these users' new recipes when they are uploaded.

#### Prioritization Grid

<details open>
<summary><em>Click to expand grid image</em></summary>

![Prioritization grid](/documentation/images/prioritization-grid.jpg)

</details>

<br>

| Number | Opportunity/Problem                                                                | Importance | Viability/Feasibility |
| ------ | ---------------------------------------------------------------------------------- | ---------- | --------------------- |
| 1      | Provide secure login and account management functions                              | 10         | 10                    |
| 2      | Provide functions for creating and managing one's own recipes to be seen by others | 10         | 10                    |
| 3      | Provide functions for searching and browsing others' recipes                       | 10         | 8                     |
| 4      | Provide functions for storing recipes to make them easy to find again              | 8          | 10                    |
| 5      | Allow users to add comments to recipes                                             | 8          | 10                    |
| 6      | Allow users to follow and be followed by other users                               | 6          | 6                     |
|        |                                                                                    | **52**     | **54**                |

##### 1. Provide secure login and account management functions

This problem has maximum importance because it is vital to fulfilling the users' and business's goals established above. Account management functions are vital to provide users with the security and control over their personal data that they have come to expect with the modern internet. It is highly feasible because the features required to do this are easily provided by any database system and many security frameworks that are available.

##### 2. Provide functions for creating and managing one's own recipes to be seen by others

This problem has maximum importance because it is vital to the social aspect of the website which is desired by the business and the users. It is highly feasible because it can be easily facilitated by a database system and a web server framework.

##### 3. Provide functions for searching and browsing others' recipes

This problem has maximum importance because it is vital to the social aspect of the website which is desired by the business and the users. It is highly feasible because it can be easily facilitated by certain database systems and a web server framework.

##### 4. Provide functions for storing recipes to make them easy to find again

This problem has high importance because it is important for the social aspect of the website which is desired by the business and the users. It is highly feasible because it can be easily facilitated by any database system and web server framework.

##### 5. Allow users to add comments to recipes

This problem has high importance because it is important for the social aspect of the website which is desired by the business and the users. It is highly feasible because it can be easily facilitated by any database system and web server framework.

##### 6. Allow users to follow and be followed by other users

This problem has been given a lower importance because although it is important for the social aspect of the website it is not vital to providing the basic functions of the website. It has a lower feasibility because it may be complicated to implement.

##### Priority Evaluation

It is recommended that the first release should focus on delivering a minimum viable product (MVP) which aims to fulfil user goals #1, #2 and #3, with a view to fulfilling #4 in a later release. This is due to the complexity of the feature.

Problems #1 to #5 are vital to fulfilling the business goals and have high feasibility.

[↑ Back to top](#cook-book)

### Scope

The scope plane is about defining requirements based on the goals established on the strategy plane.

#### Provide functions for creating and managing one's own recipes to be seen by others

##### Data storage

MongoDB will be chosen as the database system for storage and retrieval of data. This is because a recipe contains collections of ingredients and steps that are specific to that recipe, meaning no ingredients or steps can be shared between recipes, so there will be no saving of data space this way. Instead the recipes will be stored as documents, with the ingredients and steps forming arrays in the document.

##### Web server

Flask will be chosen as the web server technology for its simplicity. It supports the Jinja templating engine which will allow compartmentalization of code to make the program easier to expand in the future and reduce code duplication. Flask-PyMongo will be used to provide integration with the MongoDB database. Flask-WTF will be used to provide integration with WTForms to make the programming of forms on the website simpler.

#### Provide secure login and account management functions

Flask makes use of Werkzeug which provides security functions for salting and hashing passwords. The user's credentials will be stored as a username and salted and hashed password pair. Werkzeug will compare the password submitted by the user to determine its correctness. Heroku's automatic SSL configuration will be used to secure data in transit between the client and the web server. TLS mode will be enabled with the MongoDB connection string to secure data in transit between the web server and the database server.

At minimum, functions to login, register, and change password will be provided. Other functionality such as multi-factor authentication, account deletion, verification, etc. will be reserved for future releases; it will be considered out of scope for a minimum viable product.

#### Provide functions for searching and browsing others' recipes

MongoDB makes available search indexes which will facilitate this function.

#### Provide functions for storing recipes to make them easy to find again

A user object in the database will be stored with an array of favourite recipes' IDs. Functionality will be provided for a user to see their array of favourite recipes, and to add and remove recipes from this array.

#### Allow users to add comments to recipes

A recipe object in the database will be stored with an array of comments. Functionality will be provided to display a recipe's comments and to allow a user to add their comment.

[↑ Back to top](#cook-book)

### Structure

[↑ Back to top](#cook-book)

### Skeleton

[↑ Back to top](#cook-book)

### Surface

[↑ Back to top](#cook-book)

## Technologies Used

### Flask

[Flask](https://flask.palletsprojects.com/en/3.0.x/) is a web server for Python. It will be used for processing HTTP requests and producing responses to be used by a client web browser.

### WTForms

[WTForms](https://wtforms.readthedocs.io/en/3.1.x/) is "a flexible forms validation and rendering library for Python web development." It will be used for its validation capabilities, especially its ability to define validation rules that can be written once and applied both to client-side and server-side validation.

### Jinja

[Jinja](https://jinja.palletsprojects.com/en/3.1.x/) is "a fast, expressive, extensible templating engine" which is leveraged by Flask to allow code reuse and compartmentalization to the production of HTML views by the web server.

### jQuery

[jQuery](https://jquery.com/) is "a fast, small, and feature-rich JavaScript library." It will be used to expedite the development of custom JavaScript that will be required for certain features of the website.

### Materialize

[Materialize](https://materializecss.com/) is "a modern responsive front-end framework based on Material Design" that will be used to provide styling, icons and components to the website.

### MongoDB Atlas

[MongoDB Atlas](https://www.mongodb.com/atlas) is "an integrated suite of cloud database and data services to accelerate and simplify how you build with data." It will be used to store and retrieve the data that will back the website.

### gunicorn

[Gunicorn](https://gunicorn.org/) is "a Python WSGI HTTP Server for UNIX". It is used to load and run the app in the Heroku production environment. As specified in the [Procfile](./Procfile) it will import the `app` variable from the `app.py` file. Heroku supports this well as described [here](https://devcenter.heroku.com/articles/python-gunicorn).

[↑ Back to top](#cook-book)

## Testing

[↑ Back to top](#cook-book)

## Deployment

The website is deployed on Heroku at <https://cookbook-dm-635232ac3f84.herokuapp.com/>

### Environment Variables

| Variable       | Description                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------------------- |
| PORT           | The port number on which the web server will listen for connections.                                      |
| SECRET_KEY     | The secret key that is used to sign session cookies.                                                      |
| MONGO_URI      | The connection string to the MongoDB database.                                                            |
| EMAIL_FROM     | The 'from' address of contact emails sent by the server.                                                  |
| EMAIL_TO       | The 'to' address of contact emails sent by the server.                                                    |
| EMAIL_HOST     | The SMTP host used to send contact emails.                                                                |
| EMAIL_PORT     | The port used to connect to the SMTP host used to send contact emails.                                    |
| EMAIL_USER     | The login user name used to connect to the SMTP host.                                                     |
| EMAIL_PASSWORD | The password used to connect to the SMTP host.                                                            |

[↑ Back to top](#cook-book)
