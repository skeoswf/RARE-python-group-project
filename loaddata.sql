CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);
SELECT* FROM Categories
INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');

INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content') VALUES (1, 1, 'Test', '2024-11-04', 'https://www.test.com/test', 'Test')

INSERT INTO Users (first_name, last_name, email, bio, username, password, profile_image_url, created_on, active) VALUES ('Cody', 'Keener', 'codymkeener@gmail.com', 'Wow', 'ckeener', 'test', 'https://www.test.com/test-image', '2024-11-04', 1)

INSERT INTO Tags ('label') VALUES ('Test Tag');

INSERT INTO PostTags ('post_id', 'tag_id') VALUES (1, 1)
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (1, 3)
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (1, 5)

INSERT INTO Posts ('author_id', 'post_id', 'content') 

SELECT * FROM PostTags

SELECT * FROM Tags

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
    From Posts p
    LEFT JOIN Categories c
        ON p.category_id = c.id
    LEFT JOIN Users u
        ON p.user_id = u.id

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
    WHERE p.id = 1

SELECT
      t.id,
      t.label,
      pt.post_id,
      pt.tag_id
    FROM Tags t
    JOIN PostTags pt
      ON t.id = pt.tag_id
    WHERE pt.post_id = 1

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
        u.active,
        pt.id,
        pt.post_id,
        pt.tag_id,
        t.id,
        t.label
    FROM Posts p
    LEFT JOIN Categories c
        ON p.category_id = c.id
    LEFT JOIN Users u
        ON p.user_id = u.id
    LEFT JOIN PostTags pt
      ON  pt.post_id = p.id
    LEFT JOIN Tags t
      ON t.id = pt.tag_id

SELECT * FROM PostTags

DELETE FROM PostTags
WHERE tag_id = 4
