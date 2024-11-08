
from .user_requests import (
    create_user,
    login_user,
    get_all_users,
    get_single_user,
    update_user,
    delete_user
)

from .post_requests import (
    create_post,
    get_all_posts,
    get_single_post,
    get_post_by_category,
    get_posts_by_user,
    update_post,
    delete_post
)

from .tag_requests import (
   get_all_tags,
   get_single_tag,
   get_tags_by_post,
   create_tag,
   update_tag, 
   delete_tag
)

