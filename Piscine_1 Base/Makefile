.PHONY: clean

clean:
	@echo "Cleaning up..."
	@if [ -d "d05/logs" ]; then rm -rf d05/logs; fi
	@if [ -d "d05/staticfiles" ]; then rm -rf d05/staticfiles; fi
	@if [ -f "d05/db.sqlite3" ]; then rm -f d05/db.sqlite3; fi
	@if [ -f "d05/logs/form_submissions.log" ]; then rm -f d05/logs/form_submissions.log; fi
	@find . -name "*.pyc" -exec rm -f {} \;
	@find . -name "__pycache__" -exec rm -rf {} \;
	@find . -name ".DS_Store" -exec rm -f {} \;
	@echo "Done."
