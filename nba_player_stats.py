import numpy as np
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from sklearn.tree import DecisionTreeRegressor
from flask import Flask, request, render_template

app = Flask(__name__)

def get_player_id(player_name):
    player_list = players.get_players()
    for player in player_list:
        if player['full_name'] == player_name:
            return player['id']
    return None

def get_player_info(player_name):
    player_id = get_player_id(player_name)
    if player_id is not None:
        response = playergamelog.PlayerGameLog(player_id=player_id)
        return response.get_data_frames()[0]
    else:
        raise ValueError(f"Player '{player_name}' not found.")

def collect_player_stats(player_name):
    try:
        player_info = get_player_info(player_name)
        if not player_info.empty:
            last_5_games_data = player_info.iloc[-5:]  # Get the last 5 games' data
            player_data = {
                'minutes_played': float(last_5_games_data['MIN'].mean()),
                'points_per_game': float(last_5_games_data['PTS'].mean()),
                'shooting_percentage': "{:.3f}".format(float(last_5_games_data['FG_PCT'].mean()))
            }
            return player_data
        else:
            return None
    except ValueError:
        return None

def select_and_train_model(player_data):
    X = np.array(player_data['shooting_percentage']).reshape(-1, 1)
    y = np.array(player_data['points_per_game']).reshape(-1, 1)
    model = DecisionTreeRegressor()
    model.fit(X, y)
    return model

def predict_points(player_data):
    model = select_and_train_model(player_data)
    shooting_percentage = player_data['shooting_percentage']
    predicted_points = model.predict([[shooting_percentage]])
    return predicted_points[0]

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        player_name = request.form['player_name']
        player_data = collect_player_stats(player_name)
        if player_data is not None:
            prediction = predict_points(player_data)
            return render_template('index.html', player_name=player_name, player_data=player_data, prediction=prediction)
        else:
            return render_template('index.html', error_message=f"Player '{player_name}' not found.")
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
