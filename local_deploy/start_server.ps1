cd ..\shrillecho-fastapi

pip install uv
uv venv
.venv/scripts/activate
uv pip install --upgrade -r requirements.txt
uv pip install -e ../.. 

uvicorn server:app --proxy-headers --host "localhost" --port 8001 --reload
