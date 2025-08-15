run:
source workout-api/workoutapi/Scripts/Activate
	@uvicorn workoutapi.main:app --reload	

create-migrations:
	alembic --config "C:\Projetos\Bootcamp Python - DIO\workout-api\workoutapi\alembic.ini" revision --autogenerate -m "init_db"

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head