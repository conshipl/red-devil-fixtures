from app import db

WHERE_TO_WATCH = {
                2013: "Paramount+",
                2016: "ESPN+",
                2021: "NBC",
                2015: "beIN SPORTS",
                2002: "ESPN+",
                2019: "Paramount+",
                2003: "ESPN+",
                2017: "GolTV",
                2014: "ESPN+",
                }

class Competition(db.Model):
    __tablename__ = "competitions"

    comp_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    abbrev = db.Column(db.String())
    type = db.Column(db.String())
    country = db.Column(db.String())
    country_code = db.Column(db.String())
    crest = db.Column(db.String())
    watch = db.Column(db.String())
    season_id = db.Column(db.Integer)

    def __init__(self, competition):
        self.comp_id = competition["id"]
        self.name = competition["name"]
        self.abbrev = competition["code"]
        self.type = competition["type"]
        self.country = competition["area"]["name"]
        self.country_code = competition["area"]["code"]
        self.crest = competition["emblem"]
        self.watch = WHERE_TO_WATCH[self.comp_id]
        self.season_id = competition["currentSeason"]["id"]
        self.start_date = competition["currentSeason"]["startDate"]
        self.end_date = competition["currentSeason"]["endDate"]

class Season(db.Model):
    __tablename__ = "seasons"

    season_id = db.Column(db.Integer, primary_key = True)
    comp_id = db.Column(db.Integer)
    start_date = db.Column(db.String())
    end_date = db.Column(db.String())
    current_matchday = db.Column(db.Integer)
    winner = db.Column(db.String())

    def __init__(self, competition):
        self.season_id = competition["currentSeason"]["id"]
        self.comp_id = competition["id"]
        self.start_date = competition["currentSeason"]["startDate"]
        self.end_date = competition["currentSeason"]["endDate"]
        self.current_matchday = competition["currentSeason"]["currentMatchday"]
        self.winner = competition["currentSeason"]["winner"]

class Team(db.Model):
    __tablename__ = "teams"

    team_id = db.Column(db.Integer, primary_key = True)
    comp_id = db.Column(db.Integer)
    country = db.Column(db.String())
    name = db.Column(db.String())
    abbrev = db.Column(db.String())
    crest = db.Column(db.String())
    address = db.Column(db.String())
    website = db.Column(db.String())
    founded = db.Column(db.Integer)
    venue = db.Column(db.String())

    def __init__(self, team, comp_id):
        self.team_id = team["id"]
        self.comp_id = comp_id
        self.country = team["area"]["name"]
        self.name = team["name"]
        self.abbrev = team["tla"]
        self.crest = team["crest"]
        self.address = team["address"]
        self.website = team["website"]
        self.founded = team["founded"]
        self.venue = team["venue"]

class Match(db.Model):
    __tablename__ = "matches"

    match_id = db.Column(db.Integer, primary_key = True)
    matchday = db.Column(db.Integer)
    season_id = db.Column(db.Integer)
    comp_id = db.Column(db.Integer)
    home_id = db.Column(db.Integer)
    home_name = db.Column(db.String())
    home_score = db.Column(db.Integer)
    away_id = db.Column(db.Integer)
    away_name = db.Column(db.String())
    away_score = db.Column(db.Integer)
    date = db.Column(db.String())
    time = db.Column(db.String())
    watch = db.Column(db.String())
    status = db.Column(db.String())

    def __init__(self, match, comp_id, comp_watch):
        self.match_id = match["id"]
        self.matchday = match["matchday"]
        self.season_id = match["season"]["id"]
        self.comp_id = comp_id
        self.home_id = match["homeTeam"]["id"]
        self.home_name = match["homeTeam"]["name"]
        self.home_score = match["score"]["fullTime"]["home"]
        self.away_id = match["awayTeam"]["id"]
        self.away_name = match["awayTeam"]["name"]
        self.away_score = match["score"]["fullTime"]["away"]
        self.date = match["utcDate"].split("T")[0]
        self.time = match["utcDate"][11:19]
        self.watch = comp_watch
        self.status = match["status"]

class Standing(db.Model):
    __tablename__ = "standings"

    team_id = db.Column(db.Integer, primary_key = True)
    comp_id = db.Column(db.Integer, primary_key = True)
    season_id = db.Column(db.Integer)
    position = db.Column(db.Integer)
    name = db.Column(db.String())
    crest = db.Column(db.String())
    games_played = db.Column(db.Integer)
    form = db.Column(db.String())
    win = db.Column(db.Integer)
    draw = db.Column(db.Integer)
    loss = db.Column(db.Integer)
    points = db.Column(db.Integer)
    goals_for = db.Column(db.Integer)
    goals_against = db.Column(db.Integer)
    goal_difference = db.Column(db.Integer)

    def __init__(self, standing, comp_id, season_id):
        self.team_id = standing["team"]["id"]
        self.comp_id = comp_id
        self.season_id = season_id
        self.position = standing["position"]
        self.name = standing["team"]["name"]
        self.crest = standing["team"]["crest"]
        self.games_played = standing["playedGames"]
        self.form = standing["form"]
        self.win = standing["won"]
        self.draw = standing["draw"]
        self.loss = standing["lost"]
        self.points = standing["points"]
        self.goals_for = standing["goalsFor"]
        self.goals_against = standing["goalsAgainst"]
        self.goal_difference = standing["goalDifference"]
