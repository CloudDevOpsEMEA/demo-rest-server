IMAGE = boeboe/demo-rest-server
TAG = 1.0.0

default: build push

build:
	docker build --pull -t ${IMAGE}:${TAG} --build-arg VERSION=${TAG} .
	docker tag ${IMAGE}:${TAG} ${IMAGE}:${TAG}
	docker tag ${IMAGE}:${TAG} ${IMAGE}:latest

build-clean:
	docker build --pull --no-cache -t ${IMAGE}:${TAG} --build-arg VERSION=${TAG} .
	docker tag ${IMAGE}:${TAG} ${IMAGE}:${TAG}
	docker tag ${IMAGE}:${TAG} ${IMAGE}:latest

push:
	docker push ${IMAGE}:${TAG}
	docker push ${IMAGE}:latest

remove:
	docker rm demorestserver

kill:
	docker kill demorestserver

run_local:
	docker run --name demorestserver -p 8000:8000 ${IMAGE}

run_remote:
	docker run --name demorestserver -p 8000:8000 ${IMAGE}:${TAG}
