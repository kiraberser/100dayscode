import requests
import logging

try:
    blogs_response = requests.get(url='https://api.npoint.io/3dc8f60cf2d3bec7fd6a')
    blogs_data = blogs_response.json() 
except Exception as e:
    logging.error(e)
    

class Post:
    #Atributos
    def __init__(self):
        self.data_blog = blogs_data
        self.title = ''
        self.subtitle = ''
        self.body = ''
        self.id = 0
        self.image = ''
    
    #Metodos
    def get_post(self, post_id):
        for post in self.data_blog:
            if post['id'] == post_id:
                self.title = post['title']
                self.subtitle = post['subtitle']
                self.body = post['body']
                self.id = post['id']
                self.image = post['image_url']