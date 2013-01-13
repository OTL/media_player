movie_player
============

Linux ROS movie_player node.
This controls movie by totem. You needs totem.

Published Topics
----------
- None

Subscribed Topics
----------
- /movie/play (movie_player/Play)   play movies by totem program
- /movie/control (movie_player/Control)   control totem by ROS topic


movie_player/PlayList message
-----------------
string[] paths:   full path of movie to be played

movie_player/Control message
-----------------
byte type: type of control (Play:0, Pause:1, Quit:2, Next:3, Previsou:4)


License
------------
BSD

Author
------------
Takashi Ogura
