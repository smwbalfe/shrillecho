git submodule update --remote --force
python set_env.py prod
docker-compose down
docker-compose up --build