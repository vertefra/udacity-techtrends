if [[ ! $CONTAINER ]]; then
    CONTAINER=techtrends
fi

docker container stop techtrends && \
    docker container rm techtrends