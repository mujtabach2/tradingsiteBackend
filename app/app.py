from __init__ import create_app  # Import the create_app function instead of the app instance

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
