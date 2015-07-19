uwsgi --http :9090 --module falcon_app.app:app --disable-logging --master --processes 2 --threads 2
