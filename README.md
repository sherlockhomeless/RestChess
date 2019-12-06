# RestChess: Minimal REST-ChessBoard

## Idea

RestChess-Board offers a uniform interface for different chess-computers to play against each other.
Rest-Endpoints:

GET /game => something like {round: <int>, players: [<player_obj>, <player_obj>], Winner: "None", gamestate: [
  [2,3,4,5,6,4,3,2], [1,1,1,1,1,1,1,1], [0,0,0,0,0,0,0],...,[-1,-1,-1,...]]}
  with 2 := black tower, 3 = black knight,... -1 = White Pawn,...
  
POST /move => {src = "a2", dest = "a3"}

GET /LOG => { <history of all moves>}

## Install

*requirements*:
* python3
* virtualenv

1. git clone git@github.com:sherlockhomeless/RestChess.git
2. virtualenv <somename>
3. source <somename>/bin/activate
4. pip install -r requirements.txt
5. done

## Run

1. export FLASK_APP=RestChess.py
2. flask run
3. check with "curl http://127.0.0.1:5000"
