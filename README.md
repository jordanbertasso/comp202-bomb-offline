# Usage
You can either run it directly from Docker Hub with
```
$ BOMB_DIR=<The directory of your bomb executable>
$ docker run -it --security-opt seccomp=unconfined -h ash -v $BOMB_DIR:/bomb jordanbertasso/comp202-bomb-offline
```

# Build from source

## Step 1
### Build the docker image
```
$ docker build -t comp202/bomb .
```

## Step 2
### Run the docker image
```
$ BOMB_DIR=<The directory of your bomb executable>
$ docker run -it --security-opt seccomp=unconfined -h ash -v $BOMB_DIR:/bomb comp202/bomb
```
