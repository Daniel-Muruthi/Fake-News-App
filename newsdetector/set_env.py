import os

def set_database_url():
    database_url = "postgres://Muruthi:muruthi1995@127.0.0.1/fakenews"
    os.environ.setdefault("DATABASE_URL", database_url)

if __name__ == "__main__":
    set_database_url()
