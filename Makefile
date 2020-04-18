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

run_local: kill remove
	docker run --name demorestserver ${IMAGE}

run_remote: kill remove
	docker run --name demorestserver ${IMAGE}:${TAG}
