web: uvicorn --host 0.0.0.0 --port $PORT asgi:application

web: uvicorn --host 0.0.0.0 --port $PORT asgi:app
release: python release.py


release: (cd superproject && python manage.py migrate)