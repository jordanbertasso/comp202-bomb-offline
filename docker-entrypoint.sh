#!/bin/bash
./reply-to-bomb.py &>/dev/null &
echo "127.0.0.1 comp202-len2.science.mq.edu.au" >> /etc/hosts
cd /bomb

echo Your Student ID:
read SID
useradd -rUm -s /bin/bash $SID
su $SID