import requests
from .constants import *

class Client(object):
    email = password = session = None
    data = None
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.session = self.login()
        
    def login(self):
        session = requests.Session()
        data = {
            'j_username': self.email,
            'j_password': self.password,
            '_spring_security_remember_me': 'on'
        }
        
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        
        response = session.post(
            url=CONSTANTS.get('LOGIN_URL'),
            headers=headers,
            data=data,
        )
        if int(response.status_code) == 401:
            print("UnauthorizedError: Either email or password is incorrect")
            exit(0)
        
        return session

    def get_user(self):
        session = self.session
        
        self.data = session.get(url=CONSTANTS.get('ME_URL')).json()
        
        return self.data
    
    def get_tasks(self):
        params = {
            'includeDeleted': "false",
            'includeDone': "false",
        }
        
        tasks_data = self.session.get(
            url=CONSTANTS.get('TASKS_URL'),
            params=params
        ).json()
        
        return tasks_data