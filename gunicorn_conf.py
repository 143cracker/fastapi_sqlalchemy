#out side the project if project is fastapi_sqlalchemy then gunicorn_conf.py ouside

bind = "unix:/home/ubuntu/fastapi_sqlalchemy/gunicorn.sock"
workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 120
loglevel = "info"
accesslog = '/home/ubuntu/access_log'
errorlog =  '/home/ubuntu/error_log'
