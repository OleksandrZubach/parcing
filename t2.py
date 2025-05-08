import requests
from requests.exceptions import HTTPError
from my_token import API_TOKEN

class Post:
    def __init__(self, post_id,user_id,title,body):
        self.post_id=post_id
        self.user_id = user_id
        self.title = title
        self.body = body

    def display_summary(self):
        return f'''Post_id is {self.post_id},
        
                User_id os {self.user_id},
                
                Post itle: {self.title}, 
                
                Main body is {self.body} 


'''

class Post_Manager:
    API_URL = 'https://jsonplaceholder.typicode.com/posts'

    @classmethod
    def fetch_posts(cls):
        responce=requests.get(cls.API_URL)
        if responce.status_code==200:
            return responce.json()
        else:
            raise Exception (f'Failed in fech posts {responce.status_code}')

    @staticmethod
    def parse_posts(post_data):
        return  [Post(post['id'], post['userId'], post['title'], post['body'])
                 for post in post_data]


if __name__ == '__main__':
    post_data=Post_Manager.fetch_posts()
    post = Post_Manager.parse_posts(post_data)
    for i in post[:5]:
       print(i.display_summary())