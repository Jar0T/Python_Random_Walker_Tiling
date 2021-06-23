# Python Random Walker Tiling

Purpose of random walker is to completley tile given space. Result of running algorithm is tiled space where every tile is visited exactly one time.
The algorithm is using backtracking.

During execution actor is choosing one of avaliable directions and moving in this direction. If actor can't move at any given point it checks if whole space has been tiled. If yes algorithm ends, else actor is taking step back and checking other avaliable routes.
