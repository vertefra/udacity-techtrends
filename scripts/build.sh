set -x

export TAG='techtrend:0.0.1'
echo "Image tag: " $TAG
docker build -t=$TAG .