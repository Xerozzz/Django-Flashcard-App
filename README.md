# Flashcards App Using Django
This is a flashcards application built using Python, Django and SQLite. Mini-project that is used similarly to Anki. Meant to help studying using flashcards memorization through spaced repetition.

Meant for python 3.9 (most other versions work too) and Django 4.0.4

## Running It
1. `git clone` this repository
2. Create a virtualenv if you want
3. Install dependencies using `pip install -r requirements.txt`
4. Migrate the database using `py manage.py migrate`
4. Run the server using `py manage.py runserver`
5. Use the application as you wish


## Development
Not sure if there will be anymore development on this but some future features are:

- Creating sets of flashcards for different subjects/topics
- Track the last time a card was checked
- Show success messages when creating new cards or when checking cards
- Archiving unwanted cards