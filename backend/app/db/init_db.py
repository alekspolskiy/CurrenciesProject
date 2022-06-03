import app

from sqlalchemy.orm import Session
from app.db import base  # noqa: F401


# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28
from app.models import ScriptWorker
from os import listdir
from os.path import isfile, join

SCRIPTS = [f for f in listdir('app/scripts') if isfile(join('app/scripts', f))]
SCRIPTS.remove("__init__.py")


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    scripts_handler(db)


def scripts_handler(db: Session):
    script_workers = db.query(ScriptWorker).filter(ScriptWorker.script.in_(SCRIPTS)).all()
    if script_workers:
        for script_worker in script_workers:
            SCRIPTS.remove(script_worker.script) if script_worker.script in SCRIPTS else None
    for script in SCRIPTS:
        try:
            getattr(app.scripts, script.split('.')[0])(db)
            script_worker = ScriptWorker(script=script)
            db.add(script_worker)
            db.commit()
        except Exception as err:
            print(f"The script {script} ran with an error {err}")
            raise err
