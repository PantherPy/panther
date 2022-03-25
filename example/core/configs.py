"""
Generated by Panther
"""

from pathlib import Path
from dotenv import dotenv_values


DEBUG = True  # DEBUG default is False
BASE_DIR = Path(__name__).resolve().parent
env = dotenv_values(BASE_DIR / '.env')

# Load Env Variables

DB_NAME = env['DB_NAME']
DB_HOST = env['DB_HOST']
DB_PORT = env['DB_PORT']
SECRET_KEY = env['SECRET_KEY']
DB_USERNAME = env['DB_USERNAME']
DB_PASSWORD = env['DB_PASSWORD']


# # Go To https://framework.org/Middlewares For More Options
Middlewares = [
    # TODO: change middleware
    # Go To https://framework.org/SupportedDatabase For More Options
    ('panther/middlewares/db.py', {'url': f'sqlite:///{BASE_DIR}/{DB_NAME}.db'}),
    # ('panther/middlewares/db.py', f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}') # Example
    ('panther/middlewares/redis.py', {}),
]

# # Go To https://framework.org/Authentications For More Options
# Authentication = JWTAuthentication
#
# # Only If Authentication Set To JWT
# JWTConfig = {
#     'Algorithm': 'HSA256',
#     'TokenLifeTime': timedelta(days=2),
#     'Key': SECRET_KEY
# }


URLs = 'core/urls.py'
