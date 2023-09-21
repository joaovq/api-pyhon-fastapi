## Create venv

``` bash
python -m venv .venv
```
Activate the virtual environment:
Linux/Mac OS X: `source ./.venv/bin/activate`
Windows (PowerShell): `.\.venv\Scripts\activate.ps1`.
Install dependencies in your virtualenv using pip and setup a git hook to run tests before committing code changes with pre-commit hooks, see [pre
Install dependencies in your virtualenv using pip or poetry, depending on which you prefer to use for development and testing of this project.
Install dependencies in your virtualenv with pipenv or poetry, and then install this package into editable mode using setuptools (`pip install --editable .`)

## Install fast api

``` bash
pip install "fastapi[all]" 
```

## Install pytest

``` bash
pip install pytest 

```

## Manage database SQL

``` bash

pip install sqlalchemy

```

### Import the SQLAlchemy parts 

``` python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

```


### Create a database URL for SQLAlchemy
- [Docs](https://fastapi.tiangolo.com/tutorial/sql-databases/)

``` python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

```

If you were using a PostgreSQL database instead, you would just have to uncomment the line:


``` python
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
```
## Run migrations with Alembic
Alembic is an open source tool that allows us to easily manage our database schema and make changes as we need them without having to worry about
Migrations for sqlalchemy
[Alembic Docs](https://alembic.sqlalchemy.org/en/latest/#installation)
``` bash
pip install alembic==1.4.3
python -m venv .venv # or use `virtualenv` if not installed on your system already
source ./.venv/bin/activate  # Linux shell (Bash, ZSH, etc.) only
(.venv) $ pip install alembic==1.4.3
(.venv) $ alembic init alembic
(.venv) $ cd alembic && touch env.py
```
Run first migrations
 - Create script for migration
```bash
alembic revision -m "message"
```
- Execute migration
```bash
alembic upgrade head
```

Run after migrations
 - Create script for migration
```bash
alembic revision -m "message"
```
- Execute migration
```bash
alembic upgrade head
```

## OAuth2 
- [Docs Security](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

## Install multipart
- [Multipart docs](https://github.com/encode/starlette-multipart)
```bash
pip install python-multipart
```

``` bash
pip install "python-jose[cryptography]"
```

## Password hashing¶
``` bash
pip install "passlib[bcrypt]"
```