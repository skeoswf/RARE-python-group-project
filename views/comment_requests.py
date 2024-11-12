import sqlite3
from models import Comment

def get_all_comments():
  with sqlite3.connect("./db.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
        m.id,
        m.content,
        u.id authorId,
        p.id postId

    From Comments m
    LEFT JOIN Users u
        ON m.author_id = u.id
    LEFT JOIN Posts p
        ON m.post_id = p.id      
    """)

    comments = []
    
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      
      comment = Comment(row['id'], row['authorId'], row['postId'], row['content'])
      
      comments.append(comment.__dict__)
      
  return comments


def get_single_comment(id):
  with sqlite3.connect("./db.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
        m.id,
        m.content,
        u.id authorId,
        p.id postId

    From Comments m
    LEFT JOIN Users u
        ON m.author_id = u.id
    LEFT JOIN Posts p
        ON m.post_id = p.id   
    WHERE p.id = ?
    """, ( id, ))
    
    data = db_cursor.fetchone()
    
    comment = Comment(data['id'], data['authorId'], data['postId'], data['content'])
    
  return comment.__dict__

def create_comment(new_comment):
  with sqlite3.connect("./db.sqlite3") as conn:
    
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
      INSERT INTO Comments
        ( author_id, post_id, content)
      VALUES
        ( ?, ?, ? )
    """, (new_comment['author_id'], new_comment['post_id'], new_comment['content']))

    id = db_cursor.lastrowid
    
    new_comment['id'] = id
    
  return new_comment

def delete_comment(id):
  with sqlite3.connect("./db.sqlite3") as conn:
    
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
      DELETE FROM Comments
      WHERE id = ?
    """, ( id, ))

def update_comment(id, new_comment):
  with sqlite3.connect("./db.sqlite3") as conn:
    
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    UPDATE Comments
      SET
        author_id = ?,
        post_id = ?,
        content = ?
    WHERE id = ?
    """, (new_comment['author_id'], new_comment['post_id'], new_comment['content'], id, ))

    rows_affected = db_cursor.rowcount
    
  if rows_affected == 0:
    return False
  else:
    return True

def get_comment_by_user(authorId):
  with sqlite3.connect("./db.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
        m.id,
        m.content,
        u.id authorId,
        p.id postId

    From Comments m
    LEFT JOIN Users u
        ON m.author_id = u.id
    LEFT JOIN Posts p
        ON m.post_id = p.id   
    WHERE m.author_id = ?
    """, ( authorId, ))

    comments = []
    
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      
      comment = Comment(row['id'], row['authorId'], row['postId'], row['content'])
      
      comments.append(comment.__dict__)
      
  return comments

def get_comment_by_post(postId):
  with sqlite3.connect("./db.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
        m.id,
        m.content,
        u.id authorId,
        p.id postId

    From Comments m
    LEFT JOIN Users u
        ON m.author_id = u.id
    LEFT JOIN Posts p
        ON m.post_id = p.id   
    WHERE m.post_id = ?
    """, ( postId, ))

    comments = []
    
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      
      comment = Comment(row['id'], row['authorId'], row['postId'], row['content'])
      
      comments.append(comment.__dict__)
      
  return comments
