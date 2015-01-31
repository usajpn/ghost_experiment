for i in `seq 1 10`
do
	java -jar ghostclient.jar $1 $2 $3 $i &
done
