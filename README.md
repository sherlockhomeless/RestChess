# RestChess: Minimal REST-ChessBoard

## Idea

RestChess-Board offers a uniform interface for different chess-computers to play against each other.
Rest-Endpoints:

GET /game => something like {round: <int>, players: [<player_obj>, <player_obj>], Winner: "None", gamestate: [
  [2,3,4,5,6,4,3,2], [1,1,1,1,1,1,1,1], [0,0,0,0,0,0,0],...,[-1,-1,-1,...]]}
  with 2 := black tower, 3 = black bishop,... -1 = White Pawn,...
  
POST /move => {src = "a2", dest = "a3"}
  

