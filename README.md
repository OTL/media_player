movie_player
============

Linux ROS movie_player node.
This controls movie by totem. You needs totem.

movie_player.py
================

Published Topics
----------
- None

Subscribed Topics
----------
- /movie/play (movie_player/Play)   play movies by totem program
- /movie/control (movie_player/Control)   control totem by ROS topic


movie_player/PlayList message
-----------------
- string[] paths:   full path of movie to be played

movie_player/Control message
-----------------
- byte type: type of control (Play:0, Pause:1, Quit:2, Next:3, Previsou:4)

volume_controller.py
================
controls linux system volume using amixer.

Subscribed Topics
----------
- /audio_volume (movie_player/Volume)   set system audio volume by volume percentage

Parameters
-----------
- ~max_value (default: 255) : max of value to set
- ~card_id (default: 0) : id of sound card
- ~control (defalut: PCM) : this must be Master if you want to control all volumes.

movie_player/Volume message
----------
- byte percentage : percentage of system volume


License
------------
BSD

Author
------------
Takashi Ogura
