from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Starting the application...")
    print("Please open your browser and go to: http://127.0.0.1:5000")
    app.run(debug=True) 