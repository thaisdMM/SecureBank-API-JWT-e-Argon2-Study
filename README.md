# SecureBank API - JWT & Authentication Study

This project was developed as part of the **Python Learning Path** from **Rocketseat**, a technology education platform. It focuses on implementing secure authentication flows using **JSON Web Tokens (JWT)** and password hashing.

> **Note:** While based on the Rocketseat curriculum, this version includes custom adaptations such as the implementation of **Argon2** for password hashing (replacing the original bcrypt) and automated database initialization scripts.

## 🛠 Technologies and Libraries

- **Python 3.13+**
- **Flask**: Micro-framework for web development.
- **PyJWT**: Library for generating and validating JWTs.
- **Argon2-cffi**: Advanced password hashing (winner of the Password Hashing Competition).
- **SQLite**: Relational database for persistence.
- **Pytest**: Framework for automated testing.
- **Python-dotenv**: Management of environment variables.

## 🏗 Project Structure

The project follows a modular structure based on Clean Architecture principles to ensure scalability and testability:

- `init/`: Contains the `schema.sql` file to initialize the database structure.
- `src/configs/`: Configuration for environment variables and JWT settings.
- `src/controllers/`: Business logic, interfaces, and unit tests for core features.
- `src/drivers/`: Encapsulation of external libraries (JWT Handler and Password Handler).
- `src/errors/`: Standardized HTTP error handling and custom error types.
- `src/main/`: Application entry point, including composers, middlewares, routes, and server setup.
- `src/models/`: Data layer, including SQL repositories and database connection handlers.
- `src/views/`: HTTP request/response handling and input validation.

## 🔐 Implemented Security Features

1. **Password Hashing**: Uses `Argon2` to ensure that user passwords are never stored in plain text, protecting against rainbow table attacks.
2. **Stateless Authentication**: Implements JWT to allow the server to verify user identity without storing session state.
3. **Cross-Validation (UID Check)**: A security middleware ensures that the `user_id` inside the token matches the `uid` provided in the request headers, preventing ID spoofing.

## 🚀 How to Run

### 1. Requirements

Ensure you have Python installed and a virtual environment active.

### 2. Installation

```bash
pip install -r requirements.txt

```

### 3. Environment Configuration (.env)

Create a `.env` file in the root directory:

```env
KEY="your_secret_key_with_at_least_32_characters"
ALGORITHM="HS256"
JWT_HOURS="1"

```

### 4. Database Initialization

The application is configured to automatically detect if `storage.db` exists. If not, it will be created using the schema in `init/schema.sql` upon running the server.

Alternatively, you can initialize it manually:

```bash
sqlite3 storage.db < init/schema.sql

```

### 5. Start the Server

```bash
python run.py

```

The API will be available at `http://0.0.0.0:3000`.

## 🧪 Testing

To run the automated test suite and check the security handlers:

```bash
pytest -s -v

```

---

Developed as a study project during the **Rocketseat Python Bootcamp**.
