# Business-Product-Management-API

# Objective
Developing a RESTful API to manage a business' product catalog, incorporating rate limiting to prevent abuse and ensure fair usage. Impementation of CRUD operations for products and manage product stock availability.


## 📌 Project Overview
This is a **FastAPI-based Product Management API** designed to handle CRUD operations for managing business products. The API includes:
- **Product creation, retrieval, update, and deletion**
- **Pagination and rate limiting** for optimized performance
- **Testing suite** to ensure reliability
- **Database integration using SQLite & SQLAlchemy**
- **Versioning for future enhancements**
- **Deployment on Render**

## 🛠️ Tech Stack
- **Backend**: FastAPI
- **Database**: SQLite (using SQLAlchemy ORM)
- **Testing**: Pytest
- **Deployment**: Render
- **Virtual Environment**: `venv`

## 🚀 Features
- **CRUD Operations**: Create, Read, Update, and Delete products
- **Pagination & Limits**: Control the number of products per request
- **Data Validation**: Using Pydantic models
- **Testing Suite**: Ensures API stability
- **CI/CD Pipeline**: GitHub Actions for automated testing

## 📂 Project Structure
```
Business-Product-Management-API/
│── storage/
│   ├── database.py  # Database setup
│   ├── models.py    # SQLAlchemy models
│── routes/
│   ├── products.py  # Product endpoints
│── tests/
│   ├── test_api.py  # Pytest test cases
│── main.py          # FastAPI entry point
│── requirements.txt # Dependencies
│── render.yaml      # Render deployment config
│── ci.yml           # CI/CD configuration
│── README.md        # Project documentation
```

## 📦 Installation & Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/Business-Product-Management-API.git
   cd Business-Product-Management-API
   ```

2. **Create a virtual environment & activate it**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```sh
   touch test.db
   python -c "from storage.database import Base, engine; Base.metadata.create_all(bind=engine)"
   ```

5. **Run the API locally**
   ```sh
   uvicorn main:app --reload
   ```

## 📌 API Endpoints
| Method | Endpoint        | Description             |
|--------|----------------|-------------------------|
| GET    | `/v1/products` | Get all products (paginated) |
| GET    | `/v1/products/{id}` | Get a single product by ID |
| POST   | `/v1/products` | Create a new product    |
| PUT    | `/v1/products/{id}` | Update an existing product |
| DELETE | `/v1/products/{id}` | Delete a product      |

## 🧪 Running Tests
```sh
pytest tests --maxfail=1 --disable-warnings --tb=short
```

   ```
**[Live link]([https://business-product-management-api.onrender.com])**


## 📌 Author
- **Sanele Skhosana**
- GitHub: [Your GitHub](https://github.com/sanzamcmillian)

## 📜 License
This project is licensed under the **MIT License**.

