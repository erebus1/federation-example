build:
	cd integration_tests && docker-compose build

run:
	cd integration_tests && docker-compose down && docker-compose up
