# Environment variables and paths
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
SCRIPT = "src/Script CVM.py"

.PHONY: setup run clean

setup:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) $(SCRIPT)

clean:
	rm -rf $(VENV)
	rm -rf __pycache__
	rm -rf src/__pycache__