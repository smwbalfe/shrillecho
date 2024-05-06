git submodule update --remote --force
python set_env.py prod
docker-compose up --build
echo test