from app import create_app

@create_app.route('/')
def home():
   return "hello world!"