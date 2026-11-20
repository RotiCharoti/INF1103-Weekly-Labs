# Smart Inventory Auditor - INF1103 Lab 9

Built from the original Week 11 upload, preserving the original Display/Add/Update/Search/Save inventory operations and the Physical/Digital product selection submenu. The original six-option menu is unchanged. CSV loading is implemented in csv_loader.py and tested separately; it is not a menu option.

## Run locally
`python app.py`

## Run tests
`python -m unittest discover -s tests -v`

## Docker
`docker build -t smart-inventory-auditor .`
`docker run -it --rm smart-inventory-auditor`
`docker run --rm smart-inventory-auditor python -m unittest discover -s tests -v`

## Git screenshots to capture yourself
`git status`, `git add .`, `git commit -m "Complete Lab 9"`, `git push`, `git log --oneline`

## Included
Python source, tests, original inventory.json, required products.csv, Predict First notes, UML PNG and editable DOT source.

## CSV notes
The lab's CSV has no weight or download-size columns; imported physical and digital products use 0 for the missing subtype-specific value. Invalid rows are skipped.

## Test CSV loading separately
Run `python -m unittest discover -s tests -v` to exercise the CSV loader without changing the main menu.
