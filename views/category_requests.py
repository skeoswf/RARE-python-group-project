import sqlite3
import json
from models import Category

CATEGORIES = [
    {
        "id": 1,
        "label": "News",
    },
    {
        "id": 2,
        "label": "Lifestyles",
    },
    {
        "id": 3,
        "label": "Sports",
    },
    {
        "id": 4,
        "label": "Entertainment",
    }
]
def get_all_categories():
  with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM categories c
        """)

        categories = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            category = Category(row['id'], row['label'],)

            categories.append(category.__dict__) 

  return categories

def get_single_category(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM categories c
        """)

        data = db_cursor.fetchone()

        category = Category(data['id'], data['label'],)

        return category.__dict__
      
def create_category(new_category):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Category
            ( label )
        VALUES
            ( ? );
        """, (new_category['label'] ))

        id = db_cursor.lastrowid

        new_category['id'] = id

    return new_category
