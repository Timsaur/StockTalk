# Design

StockTalk is a web application that allows users to input a stock symbol to present relevant financial information to the user as well as predict a stock price for the following day.

## Overview

The design of our project can be split between the front-end, the back-end, and the integration of the front-end and the back-end.  

## Front-end

### HTML

#### layout.html

Establishes a template for other .html pages to extend. Intial scripts/design for the template sourced from: Krajee.com. Reference LICENSE.md for more information about the authors of the template.

#### register.html

Features a 3-form submit form for the user to create an account that is saved to a PostgresSQL database. Includes a Javascript alert function in the case that the username input has already been taken by another user. Links to '/login' upon completion.

#### login.html

Features a 2-form submit form for the user to log-in with registered username/password. Pulls from PostgresSQL database to confirm validity of log-in information. Links to '/' on completion.

####  base.html

Features a 1-form submit form for the user to input a stock ticker to predict stock behavior. Links to '/result' upon correct ticker input.

#### result.html

Displays a table of relevant financial data for the user's stock of choice, and features an algorithm based prediction of the stock behavior for the following day. Optionally, the user can choose to bookmark the stock they are currently looking up. Links to '/bookmarks' on bookmark.

#### bookmarks.html

Displays tables for all user bookmarked stocks similarly to result.html for convenient access to stocks that the user is "watching". Optionally, the user can choose to delete a stock from their bookmarks list via a select menu at the bottom of the page. 

### CSS

Reference <head> of layout.html for linked stylesheets via template from Krajee.com.

### JavaScript

#### test()

Actively checks if username already exists in database and alerts the user by a jsonify TRUE/FALSE test. If FALSE, the alert will run.

## Back-end

### APIs/Packages

#### IEX Finance API

We used the IEX Finance API to get historical stock data. We did this via calls to a specific url, which then returns the relevant stock data withing a certain time frame.  The API returns the data as json data. For example, to get relavent stock data for Apple for the past 2 years, you could visit the following url:

```
https://api.iextrading.com/1.0/stock/SPY/chart/2y
```

More information on how we processed this raw data can be found in the **predict.py** file explanation.

#### PostgresSQL

PostgresSQL is a package/add on to Heroku that allows us to attach an online database (which we use to store usernames, passwords, and a user's list of stocks) to our application. Our unique database is hosted on an Amazon server, and we connect to our database by calling its unique url as shown in the following line of Python code:

```
db = create_engine('postgres://arbizklxkkfsjo:742246e607fcaaa7b1faf6e7dab54d082f551bd9abeeb3e51a4ef19dd3cca5bb@ec2-54-204-36-249.compute-1.amazonaws.com:5432/dcgq0vpeghnls2')
```

More information on how we used this database can be found in the **app.py** file explanation.

#### TensorFlow

We used TensorFlow to build and train a model. Specifically, we used tensorflow.keras to make a neural network for regression modeling. Our particular neural network had 2 hidden layers, each with 64 nodes. After training our model with our training data, we used our trained model to predict the future stock price.

More information on how we used TensorFlow can be found in the **predict.py** file explanation.

### predict.py

If you would like to run **predict.py** separately from the rest of the app, use the following command:

```
python predict.py
```

predict.py has the following methods: get_data, build_model, train, and run. Each of these methods will be explained in more detail below:

#### get_data(ticker)

get_data(ticker) takes in a company's ticker symbol and then calls the IEX API. It then stores the raw data in a variable called raw. We also repeat this process to find the relavent data from the S&P 500 stock. We then process this data and store it in train_data, which is a numpy two-dimensional array.

There are four factors in our train_data array: the present open value of the stock, the average of the open stock price for the last 25 days, the present volume of the stock traded divided by 10000000 to normalize the data, and the present value of the S&P 500 divided by 100 as a normalization factor.

The train_labels variable is a two-dimensional array once column wide. This array stores the "future" value of the corresponding row in train_data. Finally, we return these two matricies as a tuple.

#### build_model(train_data)

build_model(train_data) creates a neural network through the tensorflow.keras package. In our model, our neural network has two hidden layers, each with 64 nodes. build_model then returns the regression model. We pass in train_data so we can determine how many inputs the model needs.

#### train(data)

train(data) trains the model on the training data 10 times, then returns the trained model. Data is a tuple that contains train_data and train_labels. train returns the trained model.

#### run(ticker)

run(ticker) takes in a ticker symbol, then first runs get_data to get all the necessary data the model needs and stores it in train_data and train_labels. Then, run builds the model via the train function. Once the model is trained, we once again process the present finanial data to give to the model for it to predict our stock. run then returns the value of the prediction. For valuation purposes, run also prints to the console the value of the prediction and the error of the model when run on training data.

*Note: We do realize that evaluating the model on the same set of data it was trained on is not the best way to measure accuracy of the model, as the model may be overfitted. In the future, we would like to separate our data into training and test data to have a more accurate valuation.*

## Integration

### APIs

#### Flask

#### Heroku

### app.py

app.py has the following methods: login_required, index, result, login, register, check, bookmarks, logout

#### login_required(f)

Defines a decorator function that can be applied to other methods. Used to grant access to certain pages only to users that are logged in and have a defined session["user_id"].

#### register()

Checks to confirm if users have met certain registration criteria. User must have filled out 3-field form to completion, password and confirmation must match, the username must not match previously submitted usernames. If successful, the inputted username and hashed version of password will be saved to the database.

#### login()

Checks to confirm if users have met certain login criteria. User must have filled out 2-field form to completion, username and password must match what is queried from the database. Upon successful login, the user will be redirected to the home screen. The username used to login will be saved to as session["user_id"] for future use.

#### index()

Defines a page that prompts the user to input a stock to predict the future price for. The inputted ticker must be available to lookup from the IEX Finance API, and the ticker used will be saved to a global session["ticker"] variable. Data that is retreived from the API will be saved to a list of dictionaries called data. This information includes a date, open price, volume trade, close price, future prediction price, and ticker.

#### result()

## Additional Information

1. The user must input the same password / confirmation password on the register page or they will be redirected to the register page.
2. The user must input a unique username for register to succeed, else they will be prompted by a Javascript alert to choose a different username.
3. The user must input a correct username/password combination for login to succeeded, or they will be redirected to the login page.
4. The user must be logged-in to access the financial utilities.
5. Bookmarks is implemented so that the user cannot bookmark the same stock twice.

### Authors

* Timothy Li
* Eddie Tu

### Acknowledgments

* CS50
* Isaac Struhl
* Ben Kaplan
