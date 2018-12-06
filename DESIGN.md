# Design

StockTalk is a web application that allows users to input a stock symbol to present relevant financial information to the user as well as predict a stock price for the following day.

## Overview

The design of our project can be split between the front-end, the back-end, and the integration of the front-end and the back-end.  

## Front-end

### HTML

#### base.html

#### etc etc

### CSS

####

### JavaScript

####


## Back-end

### APIs

#### IEX Finance API

We used the IEX Finance API to get historical stock data. We did this via calls to a specific url, which then returns the relevant stock data withing a certain time frame.  The API returns the data as json data. For example, to get relavent stock data for Apple for the past 2 years, you could visit the following url:

'''
https://api.iextrading.com/1.0/stock/SPY/chart/2y
'''

More information on how we processed this raw data can be found in the **predict.py** file explanation.

#### PostgresSQL

PostgresSQL is a package/add on to Heroku that allows us to attach an online database (which we use to store usernames, passwords, and a user's list of stocks) to our application. We have our unique database hosted by Heroku, and we connect to our database by calling its unique url as shown in the following line of Python code:

'''
db = create_engine('postgres://arbizklxkkfsjo:742246e607fcaaa7b1faf6e7dab54d082f551bd9abeeb3e51a4ef19dd3cca5bb@ec2-54-204-36-249.compute-1.amazonaws.com:5432/dcgq0vpeghnls2')
'''

More information on how we used this database can be found in the **app.py** file explanation.

#### TensorFlow

We used TensorFlow to build and train a model. Specifically, we used tensorflow.keras to make a neural network for regression modeling. Our particular neural network had 2 hidden layers, each with 64 nodes. After training our model with our training data, we used our trained model to predict the future stock price.

More information on how we used TensorFlow can be found in the **predict.py** file explanation.

### Files

#### predict.py




## Integration

### APIs

#### Flask

#### Heroku

## Additional Information

1. The user must input the same password / confirmation password on the register page or they will be redirected to the register page.
2. The user must input a unique username for register to succeed, else they will be prompted by a Javascript alert to choose a different username.
3. The user must input a correct username/password combination for login to succeeded, or they will be redirected to the login page.
4. The user must be logged-in to access the financial utilities.
5. Bookmarks is implemented so that the user cannot bookmark the same stock twice.

### Built With

StockTalk employs Python for the back-end, and Flask, CSS, HTML, & Javascript for the front-end website. StockTalk uses Iex to gather financial data, and tensorflow to build and train a model.

### Authors

* Timothy Li
* Eddie Tu

### Acknowledgments

* CS50
* Isaac Struhl
* Ben Kaplan
