STATES := app tests
REPO := vovataras/lab5-examples

.PHONY: $(STATES)

$(STATES):
	@docker build -f Dockerfile.$(@) -t $(REPO):$(@) .

run:
	@docker network create --driver=bridge appnet \
	&& docker run --rm --name redis --net=appnet -d redis \
	&& docker run --rm --name app --net=appnet -p 5000:5000 -d $(REPO):app

test-app:
	@docker run --rm -it --name test --net=appnet $(REPO):tests

docker-prune:
	@docker rm $$(docker ps -a -q) --force || true \
	&& docker container prune --force \
	&& docker volume prune --force \
	&& docker network prune --force \
	&& docker image prune --force

push:
	@docker push $(REPO):app
	@docker push $(REPO):tests

rm-images:
	@docker rmi -f $$(docker images -q)

pull:
	@docker pull $(REPO):app
	@docker pull $(REPO):tests

run-back:
	@docker network create --driver=bridge appnet \
	&& docker run --rm --name redis --net=appnet -d redis \
	&& docker run --rm -it --name app --net=appnet -p 5000:5000 $(REPO):app &