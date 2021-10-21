web: cat ./replace.txt >> /app/.heroku/python/lib/python3.9/site-packages/flask_appbuilder/views.py && gunicorn manage:app --bind 0.0.0.0:${PORT}
