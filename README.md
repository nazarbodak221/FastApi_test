# Python Test Assignment

## Overview
This project demonstrates a FastAPI-based application for test task.

## Getting Started

### Prerequisites
Ensure you have Python 3.10+.

### Installation

Follow these steps to install and run the application on Windows and macOS.

1. **Clone the Repository**
   ```bash
   git clone https://github.com/nazarbodak221/FastApi_test
   ```
   Open terminal
   ```bash
   cd FastApi_test
   ```

2. **Create a Virtual Environment**
    In the first terminal enter
   ```bash
   #Windows
   python -m venv venv
   venv\Scripts\activate
   
   #MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```


3. **Install Dependencies**
    In the terminal:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**
   Create a `.env` file in backend folder in the project root and add your `SECRET_KEY`:
   ```plaintext
   SECRET_KEY=<your_secret_key>
   DATABASE_URL=<your_sql_db_configuration>
   ```
   DATABASE_URL should look like ```DATABASE_URL=mysql+pymysql://root:mypassword@localhost:3306/mydatabase```

5. **Apply Migrations**
   Apply the generated migration to create the database schema in first terminal:
   ```bash
   alembic upgrade head
   ```

6. **Run the Application**
    In the terminal run:
   ```bash
   uvicorn app.main:app --port=8000 --reload
   ```


7. **Access API Documentation**
   Open your browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the API endpoints.
   In register endpooint register user and then login.
   You will get ```access_token```, and click on Authorize button and insert it. This authomatically send access token in 
    headers of HTTP requests.
---

### Notes

- Ensure you have `Python 3.10` or newer installed on your system.
- To stop the application, press `Ctrl+C` in the terminal where the server is running.
