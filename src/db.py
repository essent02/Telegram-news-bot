import sqlite3

# Define a class named 'DATABASE'.
class DATABASE:
    # Constructor for the DATABASE class.
    def __init__(self) -> None:
        # Connect to a SQLite database named 'database.db'. If it doesn't exist, it will be created.
        self.db = sqlite3.connect('database.db')

        # Create a cursor object to interact with the database.
        self.c = self.db.cursor()

    # Asynchronous method 'select' to query the database for a specific URL.
    async def select(self, url):
        # Execute a SQL query to select records from the 'news' table where the URL matches.
        self.c.execute("SELECT * FROM news WHERE url=?", (url, ))

        # Return the first row of the result set or None if no match is found.
        return self.c.fetchone()

    # Asynchronous method 'insert' to add a new URL to the database.
    async def insert(self, url):
        # Check if the URL already exists in the database; if not, proceed to insert.
        if await self.select(url) is None:
            # Execute a SQL command to insert the new URL into the 'news' table.
            self.c.execute("INSERT INTO news (url) VALUES (?)", (url, ))

            # Commit the changes to the database.
            self.db.commit()
