from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import datetime
# from apscheduler.schedulers.background import BackgroundScheduler
# from updatedatabase import UpdateDatabase

# sched = BackgroundScheduler(daemon=True)
# sched.add_job(UpdateDatabase, 'interval', minutes=10)
# sched.start()

app = Flask(__name__)

app.config.from_object(os.environ["APP_SETTINGS"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from models import Competition, Season, Team, Match, Standing

migrate = Migrate()
migrate.init_app(app, db)

all_comps = Competition.query.order_by(Competition.name).all()

@app.route('/', methods=['GET', 'POST'])
def today():
    all_matches = []
    if request.method == 'POST':
        selected_date = request.form['input-date']
        for comp in all_comps:
            matches = Match.query.filter_by(comp_id=comp.comp_id, date=selected_date).all()
            all_matches.append(matches)
    else:
        selected_date = str(datetime.date.today())
        for comp in all_comps:
            matches = Match.query.filter_by(comp_id=comp.comp_id, date=selected_date).all()
            all_matches.append(matches)
    for matches in all_matches:
        for match in matches:
            home_team = Team.query.filter_by(team_id=match.home_id).first()
            away_team = Team.query.filter_by(team_id=match.away_id).first()
            match.home_crest = home_team.crest
            match.away_crest = away_team.crest
            match.location = home_team.venue
    return render_template('today.html', all_comps=all_comps, all_matches=all_matches, selected_date=selected_date)

@app.route('/standings', methods=['GET', 'POST'])
def standings():
    all_standings = []
    for comp in all_comps:
        standings = Standing.query.filter_by(comp_id=comp.comp_id, season_id=comp.season_id).all()
        all_standings.append(standings)
    if request.method == 'POST':
        selected_comp = int(request.form['competition'])
    else:
        selected_comp = 0
    return render_template('standings.html', all_comps=all_comps, all_standings=all_standings, selected_comp=selected_comp)

if __name__ == '__main__':
    app.run()
