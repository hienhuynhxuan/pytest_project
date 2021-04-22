import os


class EnvSetup:
    API = os.getenv('API', 'https://api.unsplash.com')
    TOKEN =os.getenv('TOKEN', 'g3046bBoDHSc4yNe2gMnXxAij41kUeYQKQw01H7kk5Q')