@echo off
echo Seleccione el comando que desea ejecutar:
echo 1. Listar paquetes instalados
echo 2. Guardar lista de paquetes en requirements.txt
echo 3. Instalar paquetes desde requirements.txt
echo 4. Ejecutar proyecto
echo 5. python manage.py makemigrations
echo 6. python manage.py migrate

set /p opcion="Ingrese el número del comando: "

if "%opcion%"=="1" (
    pip list
) else if "%opcion%"=="2" (
    pip freeze > requirements.txt
) else if "%opcion%"=="3" (
    pip install -r requirements.txt
) else if "%opcion%"=="4" (
    python manage.py runserver
) else if "%opcion%"=="5" (
    python manage.py makemigrations
) else if "%opcion%"=="6" (
    python manage.py migrate
) else (
    echo Comando no reconocido
)
