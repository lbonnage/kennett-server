#!/bin/sh
now=$(date)
echo "$now Starting autoshutdown"
SERVICE='server.jar'
if ps ax | grep -v grep | grep $SERVICE > /dev/null; then
    echo "In the for loop"
    PLAYERSEMPTY=" There are 0"
	$(screen -S minecraft -p 0 -X stuff "list^M")
	sleep 5
	$(screen -S minecraft -p 0 -X stuff "list^M")
	sleep 5
	echo "About to get player list"
	SERVERPATH=$(sudo tail -n 1 /home/ubuntu/serverpath.txt)
	echo "Using serverpath ${SERVERPATH}"

	PLAYERSLIST=$(sudo perl -ne '$l=$_ if /There are/; END{print $l}' /home/ubuntu/${SERVERPATH}/logs/latest.log | cut -f2 -d"/" | cut -f2 -d ":")
    echo "Retrieved player list:"
    echo $PLAYERSLIST
	if [ "$PLAYERSLIST" = "$PLAYERSEMPTY" ]
	then
		echo "Waiting for players to come back in 12m, otherwise shutdown"
		sleep 12m
		$(screen -S minecraft -p 0 -X stuff "list^M")
		sleep 5
		$(screen -S minecraft -p 0 -X stuff "list^M")
		sleep 5
		PLAYERSLIST=$(sudo perl -ne '$l=$_ if /There are/; END{print $l}' /home/ubuntu/${SERVERPATH}/logs/latest.log | cut -f2 -d"/" | cut -f2 -d ":")
        echo "Retrieved final chance player list:"
        echo $PLAYERSLIST		
        if [ "$PLAYERSLIST" = "$PLAYERSEMPTY" ]
		then
			$(sudo /sbin/shutdown -P +1)
		fi
	fi
else
	echo "Screen does not exist, briefly waiting before trying again"
	sleep 10m
	if ! ps ax | grep -v grep | grep $SERVICE > /dev/null; then
		echo "Screen does not exist, shutting down"
		$(sudo /sbin/shutdown -P +1)
	fi
fi
