# Video Game Sale Dashboard

## 1. What is it?
This is a simple web application that displays video game sales data. The data is stored in an SQLite database and displayed using Flask and Jinja2 templates. The application has two main pages:

1. Gamelist: displays a table of video game titles, including the rank, name, platform, year, genre, and publisher.
2. Gamesale: displays a table of video game sales data, including the game title, sales in various regions, and global sales.
## 2. Design and development
The original intention was to make the data in the database available on the page so that people could read the data they wanted in a more comfortable and intuitive way.
## 3.Installation
The network platform we use here is called code, so we need to install some models before using the program.
1. To get started, clone the repository and navigate to the project directory:

```
 git clone https://github.com/qixuan-wu/flaskProject3.git
 cd flaskProject3
```
2. Create a virtual environment and activate it:
```
1  pyenv local 3.7.0 # this sets the local version of python to 3.7.0/ 
2. python3 -m venv .venv # this creates the virtual environment for you/ 
3. source .venv/bin/activate # this activates the virtual environment/ 
4. pip install --upgrade pip # package installer for python/ 

```
3. Install the required packages:
```
pip install flask
```
4. Initialize the database:
```
flask init-db
```
5. Run the application:
```
1. cd flaskProject3
2. export FLASK_APP=game.py
3. export FLASK_ENV=development
4. python -m flask run -h 0.0.0.0/
5. project Box info 
6. Click on the website under WEB: Static Content
```
### If you want to run locally
```
1.  Clone this repository: `git clone https://github.com/qixuan-wu/flaskProject3.git
2.  Navigate into the project directory: `cd Video-Game-Sales`
3.  Create a virtual environment: `python -m venv env`
4.  Activate the virtual environment: (for Mac/Linux) or (for Windows)`source env/bin/activate``env\Scripts\activate`
5.  Install the required packages: `pip install -r requirements.txt`
6.  Initialize the database: `flask init-db`
7.  Start the application: `flask run`
```

## 4. Usage

In the beginning, you will see two files **game list** and**gamesale** when you click on the web page. 
Under the game list, you will find the name of the game, the release date, the company that released it, and the type of game.
Under the game sale, you will find the sales of the game in each region and the total number of sales worldwide.
### If you want to run locally
```
1.  Navigate to in a web browser to view the home page.`http://localhost:5000/`
2.  Click on the "Gamelist" link in the navigation bar to view a list of video games.
3.  Click on a game title to view the sales data for that game in various regions.
```
## 5. Background

The data is come from kaggle:**[link(https://www.kaggle.com/datasets/gregorut/videogamesales)]**
## 6.Contributing
Contributions are welcome! Please fork this repository and submit a pull request.
## 7.  License
This project is licensed under the MIT License. See the file for more information.`LICENSE`
