import sqlite3
from models import Tag

def get_all_tags():
  with sqlite3.connect("./rare.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
      t.id,
      t.label
    FROM Tags t
    """)
    
    tags = []
    
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      
      tag = Tag(row['id'], row['label'])
      
      tags.append(tag.__dict__)
      
  return tags

def get_single_tag(id):
  with sqlite3.connect("./rare.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
      t.id,
      t.label
    FROM Tags t
    WHERE t.id = ?
    """, (id, ))
    
    data = db_cursor.fetchone()
      
    tag = Tag(data['id'], data['label'])
      
  return tag.__dict__

def get_tags_by_post(id):
  with sqlite3.connect("./rare.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
      t.id,
      t.label,
      pt.post_id,
      pt.tag_id
    FROM Tags t
    JOIN PostTags pt
      ON t.id = pt.tag_id
    WHERE pt.post_id = ?
    """, (id, ))
    
    tags = []
    
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      tag = Tag(row['id'], row['label'])
      
      tags.append(tag.__dict__)
      
  return tags

def create_tag(new_tag):
  with sqlite3.connect("./rare.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    INSERT INTO Tags
      ( label )
    VALUES
      ( ? )
    """, (new_tag['label'], ))
    
    id = db_cursor.lastrowid
    
    new_tag['id'] = id
    
  return new_tag

def update_tag(id, new_tag):
  with sqlite3.connect("./rare.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    UPDATE Tags
      SET
        label = ?
    WHERE id = ?
    """, (new_tag['label'], id, ))
    
    rows_affected = db_cursor.rowcount
    
  if rows_affected == 0:
    return False
  else:
    return True

def delete_tag(id):
  with sqlite3.connect("./rare.sqlite3") as conn:
    
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    DELETE FROM Tags
    WHERE id = ?
    """, (id, ))
