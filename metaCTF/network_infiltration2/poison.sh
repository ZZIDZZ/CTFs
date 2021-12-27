i=1
for i in $(seq 0 90);
do
	ifconfig eth0 192.168.0.$i
	arping -c 1 -U -s 192.168.0.$i 192.168.0.255
	i=$(($i+1))
done
