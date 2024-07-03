cd K:\dev\shrillecho\shrillecho-discord
./venv/scripts/activate
hypercorn dorito_server:app --bind 0.0.0.0:5000