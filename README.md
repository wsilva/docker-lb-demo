# Docker Internal DNS round robin demo

This demo was made to demonstrate how the internal DNS from docker makes the round robin if there is more than one guy with tha same alias on the network.


Just run the stack

```
docker-compose up -d
```

Then scale 

```
docker-compose scale web=6
```

Test it with *curl*, *wget*, or refreshing the app with a browser

Credits:

 - Fernando @SmokeMachine Corrêa from telegram docker br channel for presenting it
 - Thread on docker forum: https://forums.docker.com/t/enabling-dns-round-robin/9156/2

PS:
Before it I was using Json Wilder awesome proxy container: https://github.com/jwilder/nginx-proxy .
