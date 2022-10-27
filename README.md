# red-devil-fixtures
https://red-devil-fixtures.herokuapp.com/

My final project for Computing I course at IUPUI.

It is a Flask app that displays soccer fixtures (matches, games, whatever you’d like to call them) for a selected date. The application defaults to today’s date in UTC and then allows the user to select the date via calendar, and it shows current season fixtures for 8 top-flight competitions across Europe (Bundesliga, Eredivisie, Primera Division, Primeira Liga, English Championship and Premier League, Ligue 1, and Serie A) and the Brasileiro Serie A in Brazil. Information for each match includes the teams playing and their club crests, the venue of the match (home team’s stadium name), the time of the match (UTC), and where to watch the match (the channel/app). There's also a Standings page that shows the current standings for each league, but as the database hasn't been updated in quite some time, it's no longer accurate.

## Matches: ##

[![red-devil-matches](https://github.com/conshipl/red-devil-fixtures/blob/main/red-devil-matches.PNG)](github.com/conshipl)

## Shows Final Score After Full-Time: ##

[![red-devil-fulltime](https://github.com/conshipl/red-devil-fixtures/blob/main/red-devil-fulltime.PNG)]()

## No Matches: ##

[![red-devil-no-matches](https://github.com/conshipl/red-devil-fixtures/blob/main/red-devil-no-matches.PNG)](github.com/conshipl)


## Backstory
My project started as an idea to clone this ESPN website (https://www.espn.com/soccer/schedule), which I think I was pretty successful in doing, but I wanted to solve the specific problem of not knowing where to watch each match. Soccer viewing is highly fragmented, and in fact, the 9 leagues previously mentioned represent 6 different apps/channels, so finding the correct channel can sometimes feel like playing app roulette. Thus, I added a column that shows where you can watch each match.

Initially I created a Bottle app that tapped into an SQLite Database and was hosted on PythonAnywhere. I wanted to get experience working with databases and SQL, so rather than tap directly into an API from the front-end, I wrote a Python script that parsed the API JSON data into relevant classes and made these classes into tables in the database. Then I hooked up the Bottle app to the database, and that uses HTML templates and CSS to generate the web pages. I set up another Python script to run every 24 hours on PythonAnywhere and update the database, and life was good. Life was easy.

Then, for an additional challenge, I decided that I wanted to rewrite the project in Flask, host it on Heroku, add additional features and CSS, update the database every 5 minutes instead of every 24 hours, and show the final scores of games that had ended. It turns out, however, that Heroku has an ephemeral filesystem that would delete my SQLite database every 24 hours, so over the summer, I had to learn about database migrations and switch to a PostgreSQL database.

In its final form shown in the above link, I used database models and a Python script to retrieve data from an API, store the data in a PostgreSQL database hosted on AWS, access the database via Flask and generate the webpages with HTML/CSS, and it's all hosted on Heroku. The catch is that none of it is up-to-date because I could never get the update script working on Heroku.

## Project Status
Working...Sort Of

The webpages are displaying data from a database that probably hasn't been updated since June/July 2022.

I feel like the project morphed into a Frankenstein monster that I have little interest in fully fixing, so it will likely remain in this state. I probably spent 200 hours on this project in total and learned a ton from it, so I feel like it has served its purpose, and just like Frankenstein, it is now free to vanish into the Arctic wastelands.

## Technologies
Python, Flask, PostgreSQL, Psycopg, HTML, CSS
