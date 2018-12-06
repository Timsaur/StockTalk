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


## Back-end

### APIs

#### IEX Finance API

#### PostgresSQL

#### 

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
