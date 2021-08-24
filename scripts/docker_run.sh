export TAG='techtrend:0.0.1'
export HOST_PORT='7111'
export DOCKER_PORT='3111'
export DEBUG=true

docker run --name techtrends -v $(pwd)/:/app -p $HOST_PORT:$DOCKER_PORT  $TAG  