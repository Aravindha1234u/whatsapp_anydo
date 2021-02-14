# Current API entry point
SERVER_API_URL = 'https://sm-prod2.any.do'

# API endpoints
CONSTANTS = {
    'SERVER_API_URL': SERVER_API_URL,
    'LOGIN_URL'     : SERVER_API_URL + '/j_spring_security_check',
    'ME_URL'        : SERVER_API_URL + '/me',
    'USER_URL'      : SERVER_API_URL + '/user',
    'TASKS_URL'     : SERVER_API_URL + '/me/tasks',
    'CATEGORIES_URL': SERVER_API_URL + '/me/categories'
}

# Possible task statuses
TASK_STATUSES = ('CHECKED', 'UNCHECKED', 'DONE', 'DELETED')