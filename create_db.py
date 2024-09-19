from app_sellio import db, app  # Import the db and app from your main file

def create_database():
    with app.app_context():
        
        db.create_all()  # Create all tables defined by the models

if __name__ == '__main__':
    create_database()  # Call the function to create the database
