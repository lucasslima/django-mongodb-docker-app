# Apply database migrations
# É necessário fazer a migração antes de iniciar a aplicação,
# portanto, criamos um entrepoint diferetente
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
