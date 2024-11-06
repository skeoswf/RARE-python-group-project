import sqlite3
from models import Post
# , Category, User

def get_all_posts():
  with sqlite3.connect("./rare.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
        p.id,
        p.user_id,
        p.category_id,
        p.title,
        p.publication_date,
        p.image_url,
        p.content,
        p.approved,
        c.id categoryId,
        c.label,
        u.id userId,
        u.first_name,
        u.last_name,
        u.email,
        u.bio,
        u.username,
        u.password,
        u.profile_image_url,
        u.created_on,
        u.active
    FROM Posts p
    LEFT JOIN Categories c
        ON p.category_id = c.id
    LEFT JOIN Users u
        ON p.user_id = u.id
    """)

    posts = []
    
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      
      post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])
      
      # category = Category(row['categoryId'], row['label'])
      
      # user = User(row['userId'], row['first_name'], row['last_name'], row['email'], row['bio'], row['username'], row['password'], row['profile_image_url'], row['created_on'], row['active'])
      
      # post.category = category.serialized()
      
      # post.user = user.serialized()
      
      posts.append(post.__dict__)
      
  return posts

def get_single_post(id):
  with sqlite3.connect("./rare.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
        p.id,
        p.user_id,
        p.category_id,
        p.title,
        p.publication_date,
        p.image_url,
        p.content,
        p.approved,
        c.id categoryId,
        c.label,
        u.id userId,
        u.first_name,
        u.last_name,
        u.email,
        u.bio,
        u.username,
        u.password,
        u.profile_image_url,
        u.created_on,
        u.active
    FROM Posts p
    LEFT JOIN Categories c
        ON p.category_id = c.id
    LEFT JOIN Users u
        ON p.user_id = u.id
    WHERE p.id = ?
    """, ( id, ))
    
    data = db_cursor.fetchone()
    
    post = Post(data['id'], data['user_id'], data['category_id'], data['title'], data['publication_date'], data['image_url'], data['content'], data['approved'])
      
    # category = Category(data['categoryId'], data['label'])
    
    # user = User(data['userId'], data['first_name'], data['last_name'], data['email'], data['bio'], data['username'], data['password'], data['profile_image_url'], data['created_on'], data['active'])
    
    # post.category = category.serialized()
    
    # post.user = user.serialized()
    
  return post.__dict__

def create_post(new_post):
  with sqlite3.connect("./rare.sqlite3") as conn:
    
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
      INSERT INTO Posts
        ( user_id, category_id, title, publication_date, image_url, content)
      VALUES
        ( ?, ?, ?, ?, ?, ? )
    """, (new_post['user_id'], new_post['category_id'], new_post['title'], new_post['publication_date'], new_post['image_url'], new_post['content']))

    id = db_cursor.lastrowid
    
    new_post['id'] = id
    
  return new_post

def delete_post(id):
  with sqlite3.connect("./rare.sqlite3") as conn:
    
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
      DELETE FROM Posts
      WHERE id = ?
    """, ( id, ))

def update_post(id, new_post):
  with sqlite3.connect("./rare.sqlite3") as conn:
    
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    UPDATE Posts
      SET
        user_id = ?,
        category_id = ?,
        title = ?,
        publication_date = ?,
        image_url = ?,
        content = ?,
        approved = ?
    WHERE id = ?
    """, (new_post['user_id'], new_post['category_id'], new_post['title'], new_post['publication_date'], new_post['image_url'], new_post['content'], new_post['approved'], id, ))

    rows_affected = db_cursor.rowcount
    
  if rows_affected == 0:
    return False
  else:
    return True

def get_post_by_category(categoryId):
  with sqlite3.connect("./rare.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
        p.id,
        p.user_id,
        p.category_id,
        p.title,
        p.publication_date,
        p.image_url,
        p.content,
        p.approved,
        c.id categoryId,
        c.label,
        u.id userId,
        u.first_name,
        u.last_name,
        u.email,
        u.bio,
        u.username,
        u.password,
        u.profile_image_url,
        u.created_on,
        u.active
    FROM Posts p
    LEFT JOIN Categories c
        ON p.category_id = c.id
    LEFT JOIN Users u
        ON p.user_id = u.id
    WHERE p.category_id = ?
    """, ( categoryId, ))

    posts = []
    
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      
      post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])
      
      # category = Category(row['categoryId'], row['label'])
      
      # user = User(row['userId'], row['first_name'], row['last_name'], row['email'], row['bio'], row['username'], row['password'], row['profile_image_url'], row['created_on'], row['active'])
      
      # post.category = category.serialized()
      
      # post.user = user.serialized()
      
      posts.append(post.__dict__)
      
  return posts

def get_posts_by_user(userId):
  with sqlite3.connect("./rare.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
        p.id,
        p.user_id,
        p.category_id,
        p.title,
        p.publication_date,
        p.image_url,
        p.content,
        p.approved,
        c.id categoryId,
        c.label,
        u.id userId,
        u.first_name,
        u.last_name,
        u.email,
        u.bio,
        u.username,
        u.password,
        u.profile_image_url,
        u.created_on,
        u.active
    FROM Posts p
    LEFT JOIN Categories c
        ON p.category_id = c.id
    LEFT JOIN Users u
        ON p.user_id = u.id
    WHERE p.user_id = ?
    """, ( userId, ))

    posts = []
    
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      
      post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])
      
      # category = Category(row['categoryId'], row['label'])
      
      # user = User(row['userId'], row['first_name'], row['last_name'], row['email'], row['bio'], row['username'], row['password'], row['profile_image_url'], row['created_on'], row['active'])
      
      # post.category = category.serialized()
      
      # post.user = user.serialized()
      
      posts.append(post.__dict__)
      
  return posts
