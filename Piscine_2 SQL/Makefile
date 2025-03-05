.PHONY: clean

clean:
	@echo "Cleaning up..."
	@find . -name "*.pyc" -exec rm -f {} \;
	@find . -name "*.pyo" -exec rm -f {} \;
	@find . -name "__pycache__" -exec rm -rf {} \;
	@echo "Done."

clean_env:
	@echo "Cleaning up virtual environment..."
	@rm -rf django_env/
	@echo "Done."
