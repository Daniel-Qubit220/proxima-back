### Technologies Used:

1. **FastAPI**:
   - *Description:* FastAPI is a modern, high-performance web framework for building APIs with Python. It utilizes Python type hints for automatic data validation and offers high performance through Starlette and Pydantic.

2. **SQLAlchemy**:
   - *Description:* SQLAlchemy is an ORM (Object-Relational Mapping) library for Python. It simplifies database interactions by providing an abstraction over relational databases, allowing developers to work with Python objects instead of SQL queries directly.

3. **Swagger**:
   - *Description:* Swagger is a set of tools for documenting RESTful APIs. It provides a specification and interactive documentation for APIs, helping developers understand endpoints, request/response formats, and other details.

4. **Docker**:
   - *Description:* Docker is a containerization platform that packages applications and their dependencies into containers. It ensures consistent environments across systems, simplifying deployment and ensuring portability.

5. **Python-dotenv**:
   - *Description:* Python-dotenv is a Python library managing environment variables by reading them from a `.env` file. It simplifies handling sensitive information or configuration settings separate from the codebase.

6. **uvicorn**:
   - *Description:* Uvicorn is a lightning-fast ASGI server implementation used for running Python asynchronous web applications. It's commonly used with FastAPI to serve web applications.

## Structure
The project is structured following "Screaming Architecture" approach. The structure is the following:

```
└── 📁app
    └── .env-example
    └── database.py
    └── main.py
    └── models.py
    └── requirements.txt
```

## Getting Started

First, install the requirements:

```bash
 pip install -r requirements.txt
```

Do not forget create `.env` file

```bash
DB_CONNECTION=postgresql://<user>:<password>@<host>/<dbName>
```

Run the server:

```bash
 uvicorn app.main:app
```



Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.
