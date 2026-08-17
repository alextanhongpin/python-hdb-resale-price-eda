marimo := uv run marimo
name := main.py
run:
	$(marimo) edit

publish:
	$(marimo) export html-wasm $(name) -o dist --mode run

serve:
	open http://localhost:3000
	uv run python -m http.server 3000

lint:
	uv format
	$(marimo) check --fix *.py
