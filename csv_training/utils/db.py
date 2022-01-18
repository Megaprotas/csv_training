games_file = 'games.txt'


def crate_games_db():
    with open(games_file, 'w') as csv_file:
        pass #must be called in app.py


def add_game_db(name, studio):
    with open(games_file, 'a') as csv_file:
        csv_file.write(f'{name},{studio},0\n') # 0 = not played, 1 = played


def games_list():
    with open(games_file, 'r') as csv_file:
        lines = [line.strip().split(',') for line in csv_file.readlines()] # strip() removes /n and whitespace

        games = [
            {'name': line[0], 'studio': line[1], 'played': line[2]}
            for line in lines
        ]
        return games


def mark_as_played_in_db(name):
    games = games_list()
    for game in games:
        if game['name'] == name:
            game['played'] = '1'
    _save_all_games(games)


def _save_all_games(games):
    with open(games_file, 'w') as csv_file:
        for game in games:
            csv_file.write(f"{game['name']},{game['studio']},{game['played']}\n")


def delete_game_from_db(name):
    games = games_list()
    games = [game for game in games if game['name'] != name]
    _save_all_games(games)



