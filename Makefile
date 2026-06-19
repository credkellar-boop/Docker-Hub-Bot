.PHONY: build sync audit clean

build:
	docker compose build

up:
	docker compose up -d

sync:
	python cli.py --sync

audit:
	python cli.py --audit $(IMAGE)

provision:
	python cli.py --provision "$(QUERY)"

clean:
	rm -rf data/repos/
	rm -f generated_infrastructure.yaml
