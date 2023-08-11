# NBA Points Predictor

    The NBA Points Predictor is a web application that uses a machine learning model to predict the points a specific NBA player might score in an upcoming game based on their recent performance statistics. This application was developed by Jahquan Thomas as an individual project.

## Table of Contents

    - [Overview](#overview)
    - [Project Structure](#project-structure)
    - [Requirements](#requirements)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Contributions](#contributions)
    - [License](#license)

## Overview

    The NBA Points Predictor leverages the Flask web framework and the NBA API to provide users with point predictions for NBA players. Users input a player's name, and the application returns a prediction based on the player's recent game statistics and a Decision Tree Regression model.

## Project Structure

    The project is structured as follows:

        - `nba_player_stats.py`: The main Flask application file that handles routing, data processing, and prediction logic.
        - `templates/index.html`: The HTML template for the user interface.
        - `static/styles/styles.css`: The CSS file for styling the UI.
        - `venv/`: The virtual environment directory (if applicable).

## Requirements

    - Python 3.7+
    - Flask
    - numpy
    - scikit-learn
    - nba_api
    - requests

## Installation

    1. Clone this repository to your local machine:

        git clone <https://github.com/jthomas0521/nba-points-predictor.git>

    2. Navigate to the project directory:

        cd nba-points-predictor

    3. Create a virtual environment (optional but recommended):

        python -m venv venv
        source venv/bin/activate # On Windows, use: venv\Scripts\activate

    4. Install the required packages:

        pip install -r requirements.txt

## Usage

    1. Run the Flask application:

        python -u nba_player_stats.py

    2. Open a web browser and go to: <http://localhost:5000>

    3. Enter the name of an NBA player in the input field and click the "Predict Points for Next Game" button.

    4. The predicted points for the player's next game will be displayed.

## Contributions

    This project was developed by Jahquan Thomas. Contributions are welcome and can be submitted via pull requests.

## License

    This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.
