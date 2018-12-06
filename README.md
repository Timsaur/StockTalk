1. Included in the file is requirements.txt - all of the packages included in requirements are necessary to run this website properly. To run locally, execute in terminal:
$ pip install -r requirements.txt
Once in the file .../stocktalk/stocktalk/ the user can execute:
$ python main.py
and visit localhost:5000 in order to access the web app locally. Alternatively, the user can visit stocktalk.herokuapp.com to access the version of StockTalk that we have pushed to a Heroku app via GitHub.

2. The website emplys Python for the back-end, and Flask, CSS, HTML, & Javascript for the front-end website.

3. StockTalk is a web application that allows users to input a stock symbol to present relevant financial information to the user as well as predicting a stock price for the following day. We have successfully implemented our primary goal of developing a machine learning algorithm using Tensorflow that can closely predict the price movement within a reasonable margin of error. 
(tim can talk about the algorithm here)

4. The website is implemented in a similar way to Harvard College's CS50 PSET 8 Finance, as it includes user account registration and login functions, as well as stock data lookup based on a stock symbol of user input. User functions differ in that StockTalk will predict a future stock price for the user, intended to help the user make investment decisions. Additional functionality includes a bookmark function and a bookmarks.html page, which allows the user to save a stock by its ticker, and reference his/her bookmarks page to view a consolidation of their saved stocks. The user can then choose to delete a stock from their bookmarks page via a drop-down menu at the bottom.

Notably:
	1. The user must input the same password / confirmation password on the register page or they will be redirected to register page.
	2. The user must input a unique username for register to succeed, else they will be prompted by a Javascript alert
	3. The user must input a correct username/password combination for login to succeeded, or they will be redirected to the login page.
	4. The user must be logged-in to access the financial utilities.
	5. Bookmarks is implemented so that the user cannot bookmark the same stock twice.

5. Relevantly, the IEX Finance API is utilized to lookup relevant stock information. PostgresSQL is utilized as a open source database to save user log-in information and bookmarked stocks. Heroku is utilized to deploy our web application to an online host. Github was used as a method of version control and as a helper to deploy to Heroku.

6. A basic tutorial process to explore all of the utility of StockTalk - register, login, lookup, bookmark, and delete is as follows:
	1. Register an account through a three-field form with a unique username and a password and confirmation that match each other.
	2. Login with registered user information through a two-field form by inputting a correct username and password into the login page.
	3. Enter an appropriate stock symbol (ex: 'AAPL') in the lookup form from NASDAQ, NYSE markets.
	4. Observe relevant stock information and algorithm based prediction on the results page, choose to either lookup a different stock by accessing the lookup page through the navbar or bookmark the current stock using the bookmark button
	5. Upon bookmarking, the user will be redirected to the bookmarks page where they can view all of their bookmarked stocks and a prediction for each stock.
	6. At the bottom of the bookmarks page, the user can choose to delete a bookmarked stock through a drop-down menu and submit button.

StockTalk created by Harvard College students Eddie Tu '22 and Timothy Li '22