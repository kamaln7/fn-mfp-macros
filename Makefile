.PHONY: up

up:
	faas-cli up --build-arg ADDITIONAL_PACKAGE="libxml2-dev libxslt-dev libc-dev python-dev build-base"
