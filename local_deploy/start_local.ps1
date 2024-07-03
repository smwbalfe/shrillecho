docker stop redis
docker rm redis
docker run --name redis -p 6379:6379 -d redis




