# Docker commands used

**NOTE:**: docker commands can also be inspected in the `script/` folder

### Application building:
```bash
docker build -t=$IMAGE_NAME:$TAG .
```

### Application run
```bash
docker run -n techtrends -d -v $(pwd)/:/app -p $HOST_PORT:$DOCKER_PORT $TAG
```

## Docker commands used to get the application logs
```
docker container logs techtrends
```

## Logs from the container running the TechTrends application
```
INFO:app - - [24-Aug-2021 17:43:25] About us retrieved
INFO:werkzeug - - [24-Aug-2021 17:43:25] 172.17.0.1 - - [24/Aug/2021 17:43:25] "GET /about HTTP/1.1" 200 -
INFO:werkzeug - - [24-Aug-2021 17:43:27] 172.17.0.1 - - [24/Aug/2021 17:43:27] "GET / HTTP/1.1" 200 -
INFO:app - - [24-Aug-2021 17:43:28] Article title <CNCF Cloud Native Interactive Landscape> retrieved
INFO:werkzeug - - [24-Aug-2021 17:43:28] 172.17.0.1 - - [24/Aug/2021 17:43:28] "GET /4 HTTP/1.1" 200 -
INFO:app - - [24-Aug-2021 17:43:30] About us retrieved
INFO:werkzeug - - [24-Aug-2021 17:43:30] 172.17.0.1 - - [24/Aug/2021 17:43:30] "GET /about HTTP/1.1" 200 -
INFO:werkzeug - - [24-Aug-2021 17:43:30] 172.17.0.1 - - [24/Aug/2021 17:43:30] "GET /create HTTP/1.1" 200 -
INFO:app - - [24-Aug-2021 17:43:37] Article title<test title> created
INFO:werkzeug - - [24-Aug-2021 17:43:37] 172.17.0.1 - - [24/Aug/2021 17:43:37] "POST /create HTTP/1.1" 302 -
INFO:werkzeug - - [24-Aug-2021 17:43:37] 172.17.0.1 - - [24/Aug/2021 17:43:37] "GET / HTTP/1.1" 200 -
ERROR:app - - [24-Aug-2021 17:43:42] Article id <324234> does not exists
ERROR:app - - [24-Aug-2021 17:43:42] Article id <324234> does not exists
INFO:werkzeug - - [24-Aug-2021 17:43:42] 172.17.0.1 - - [24/Aug/2021 17:43:42] "GET /324234 HTTP/1.1" 404 -
```
