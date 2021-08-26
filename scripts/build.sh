set -x

if [[ ! $IMAGE_NAME ]]; then
    IMAGE_NAME='vertefra/techtrends'
fi

if [[ ! $TAG ]]; then
    TAG='latest'
fi

docker build -t=$IMAGE_NAME:$TAG .