bootstrap-mac:
	brew install mpg321
	virtualenv venv
	. venv/bin/activate && pip install trollius

bootstrap-raspberry:
	sudo apt-get install mpg321
	virtualenv venv
	. venv/bin/activate && pip install trollius
