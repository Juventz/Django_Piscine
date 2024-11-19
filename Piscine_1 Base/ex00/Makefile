IMAGE_NAME = ex00

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -d -p 8000:8000 --name $(IMAGE_NAME)_container $(IMAGE_NAME)

stop:
	docker stop $(IMAGE_NAME)_container

clean: stop
	docker rm $(IMAGE_NAME)_container
	docker rmi $(IMAGE_NAME)

logs:
	docker logs $(IMAGE_NAME)_container

migrate:
	docker exec -it $(IMAGE_NAME)_container python manage.py migrate

shell:
	docker exec -it $(IMAGE_NAME)_container sh

rebuild: stop clean build run