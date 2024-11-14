IMAGE_NAME = hello_world

build:
	docker build -t $(IMAGE_NAME) .

run: build
	docker run -d -p 8000:8000 --name $(IMAGE_NAME)_container $(IMAGE_NAME)

stop:
	docker stop $(IMAGE_NAME)_container || true
	docker rm $(IMAGE_NAME)_container || true

clean: stop
	docker rmi $(IMAGE_NAME) || true

logs:
	docker logs -f $(IMAGE_NAME)_container

migrate:
	docker exec -it $(IMAGE_NAME)_container python manage.py migrate

shell:
	docker exec -it $(IMAGE_NAME)_container sh

rebuild: stop clean build run