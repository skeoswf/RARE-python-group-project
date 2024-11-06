from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

from views import create_user, login_user, create_post, get_all_posts, get_single_post, get_post_by_category, get_posts_by_user, update_post, delete_post, get_all_tags, get_single_tag, get_tags_by_post


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""
    # I can't figure out how to make this work, so I'm switching to the parse_url from kennels
    # def parse_url(self):
    #     """Parse the url into the resource and id"""
    #     path_params = self.path.split('/')
    #     resource = path_params[1]
    #     if '?' in resource:
    #         param = resource.split('?')[1]
    #         resource = resource.split('?')[0]
    #         pair = param.split('=')
    #         key = pair[0]
    #         value = pair[1]
    #         return (resource, key, value)
    #     else:
    #         id = None
    #         try:
    #             id = int(path_params[2])
    #         except (IndexError, ValueError):
    #             pass
    #         return (resource, id)
    
    # parse_url from kennels
    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')  # ['', 'animals', 1]
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        self._set_headers(200)
        
        response = {}
        
        parsed = self.parse_url(self.path)
        
        if '?' not in self.path:
            ( resource, id ) = parsed
            
            if resource == 'posts':
                if id is not None:
                    response = get_single_post(id)
                else:
                    response = get_all_posts()
                
            if resource == 'tags':
                if id is not None:
                    response = get_single_tag(id)
                else:
                    response = get_all_tags()
                    
        else:
            (resource, query) = parsed
            
            if resource == 'posts' and query.get('category_id'):
                response = get_post_by_category(query['category_id'][0])
                
            if resource == 'posts' and query.get('user_id'):
                response = get_posts_by_user(query['user_id'][0])
                
            if resource == 'tags' and query.get('post_id'):
                response = get_tags_by_post(query['post_id'][0])
                
        self.wfile.write(json.dumps(response).encode())
                


    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        resource, _ = self.parse_url(self.path)

        if resource == 'login':
            response = login_user(post_body)
        if resource == 'register':
            response = create_user(post_body)
            
        if resource == 'posts':
            response = create_post(post_body)

        self.wfile.write(json.dumps(response).encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        
        (resource, id) = self.parse_url(self.path)
        
        success = False
        
        if resource == "posts":
            success = update_post(id, post_body)
            
        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)
            
        self.wfile.write("".encode())

    def do_DELETE(self):
        """Handle DELETE Requests"""
        self._set_headers(204)
        
        (resource, id) = self.parse_url(self.path)
        
        if resource == "posts":
            delete_post(id)
            
        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
