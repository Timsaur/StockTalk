# Design

StockTalk is a web application that allows users to input a stock symbol to present relevant financial information to the user as well as predict a stock price for the following day.

## Overview

Project
 |
 +-- file 1
 |    
 +-- dir 2
 |  |  
 |  +-- file 2.1
 |    
 +-- dir 3
 |  |  
 |  +-- file 3.1
 |  +-- file 3.2
 |    
 +-- dir 4
 |  |  
 +  |-- dir 4.1

### Prerequisites

In requirements.txt are all of the packages necessary to run this website properly on your local machine. First, navigate to the main project folder. To download all of the necessary packages, use the following command:

```
$ pip install -r requirements.txt
```

### Running the App

To run the app, run the following command:

```
$ python stocktalk/main.py
```

This should set up and run the app on your local machine. The website will be hosted on your localhost. You can open up the website by visiting the url *localhost:5000* on your local internet browser.

## Using the App

StockTalk has the following features: register, login, predict, bookmark, and delete. A guide to each of these features follows.

### Register

Create a new account by navigating to the register page via the navigation bar at the top of the page.  To successfully register a new user, you must have a unique username and correctly input the same password twice.

### Login

To login and use the app/save your bookmarked stocks, navigate to the login page via the navigation bar at the top of the page. Provided that you have inputted an existing username and the correct password, you should now be redirected to the predict page. You must be logged in to use StockTalk.

### Predict

On the predict page, you can input the ticker symbol of an existing stock and have the website predict the future value of the stock. This process may take some time, as the app must build and train a model to give a prediction.

### Bookmark

After predicting the future value of a stock, you are given the option to save this stock to your bookmarked stocks. Bookmarks is implemented such that you cannot bookmark the same stock twice. After bookmarking a stock, you will be redirected to the bookmarks page, which predicts the stock price for all of your bookmarked stocks. Alternatively, you can navigate directly to the bookmarks page via the navigation bar at the top, provided you are logged in.

The bookmark page also allows you to select a stock via a dropdown menu and delete said stock from your bookmarked stocks.  Once the stock is deleted, the bookmark page will reload with your updated stocks and their predictions.

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
