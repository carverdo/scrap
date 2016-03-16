web: gunicorn run:app
init: python db_create_migrate.py db init
migrate: python db_create_migrate.py db migrate
upgrade: python db_create_migrate.py db upgrade
populate: python db_init_data.py