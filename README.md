- https://rest-apis-flask.teclado.com/
- docker build -t rest-apis-flask-python
- docker run -d -p 5000:5000 rest-apis-flask-python
- docker compose:
  - docker compose up
  - docker compose up --build --force-recreate --no-deps web
- We'll be using a relational database for data storage, and there are many different options: SQLite, MySQL, PostgreSQL, and others. ORM, which can take Python objects and turn them into database rows.
- ORM library (SQLAlchemy) helps us with many potential issues with using SQL, such as:
  - Multi-threading support
  - Handling creating the tables and defining the rows
  - Database migrations (with help of another library, Alembic)
  - Like mentioned, it makes the code cleaner, simpler, and shorter
- What is Flask-SQLAlchemy?
  - SQLAlchemy is the ORM library, that helps map Python classes to database tables and columns, and turns Python objects of those classes into specific rows.
  - Flask-SQLAlchemy is a Flask extension which helps connect SQLAlchemy to Flask apps.
- What is Flask-Migrate:
  - Flask-Migrate is a Flask extension built on top of Alembic and SQLAlchemy. It simplifies the integration and use of Alembic within a Flask application by providing easy-to-use commands through Flask CLI.
- Initialize the database with Flask-Migrate

  - Activate your virtual environment and run this command: flask db init (This will create a migrations folder inside your project folder.)
  - Generate the first migration to set up the database:

    This will create the migration file.

    ```
    flask db migrate
    ```

    Now let's actually apply the migration:

    ```
    flask db upgrade
    ```

    This will create the data.db file. If you were using another RDBMS (like PostgreSQL or MySQL), this command would create the tables using the existing model definitions.
