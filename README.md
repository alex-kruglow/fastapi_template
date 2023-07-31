# FastAPI template
This one is available a clean template of FastAPI application.

* [Fastapi](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Alembic](https://alembic.sqlalchemy.org/en/latest/)

How to run:
```
python3 -m venv env;
source env/bin/activate;
git clone https://github.com/alex-kruglow/fastapi_template.git;
cd fastapi_template;
pip install -r requirements.txt;
gunicorn src.main:app -w 4 -b :8001 -k uvicorn.workers.UvicornWorker;
```