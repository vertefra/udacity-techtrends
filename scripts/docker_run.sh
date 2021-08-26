export HOST_PORT='7111'
export DOCKER_PORT='3111'
export DEBUG=true
export CONTAINER=techtrends

if [[ ! $IMAGE_NAME ]]; then
    IMAGE_NAME='vertefra/techtrends'
fi

if [[ ! $TAG ]]; then
    TAG='latest'
fi

# stopping and removing containers if running
./scripts/docker_stop.sh

docker run --name $CONTAINER -d -v $(pwd)/:/app -p $HOST_PORT:$DOCKER_PORT $IMAGE_NAME:$TAG