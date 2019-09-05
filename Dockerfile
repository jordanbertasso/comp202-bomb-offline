FROM ubuntu

RUN apt-get update
RUN apt-get install vim wget netcat gdb tmux net-tools iputils-ping python3 sudo -y

WORKDIR /

COPY docker-entrypoint.sh reply-to-bomb.py ./

ENTRYPOINT ["./docker-entrypoint.sh"]
