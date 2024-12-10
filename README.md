Here’s a **formal and styled README.md** file for the first part of your assignment, detailing the **Library Management API**.

---

# **Library Management API**

## **Overview**
The Library Management API is a RESTful service for managing a collection of books. It allows users to perform CRUD operations and filter books based on specific criteria. The API is designed to be simple, robust, and scalable, and is dockerized for easy deployment.

---

## **Features**
The API supports the following operations:
1. **Add a New Book**:
   - Add a book with details like title, author, published year, ISBN, and genre.
   - Example: `POST /books`
2. **List All Books**:
   - Retrieve a list of all available books.
   - Example: `GET /books`
3. **Search for Books**:
   - Filter books by author, published year, or genre.
   - Example: `GET /books/search?author=John`
4. **Delete a Book by ISBN**:
   - Remove a book using its unique ISBN.
   - Example: `DELETE /books/{isbn}`
5. **Update Book Details by ISBN**:
   - Update one or more details of a book.
   - Example: `PUT /books/{isbn}`

---

## **Setup Instructions**

### **1. Clone the Repository**
Clone the project to your local machine:
```bash
git clone https://github.com/MrFr0g-X/library-management-api.git
cd library-management-api
```

### **2. Install Dependencies**
Install Python dependencies:
```bash
pip install -r requirements.txt
```

### **3. Run the Application**
Run the Flask application locally:
```bash
python app.py
```

Access the API at [http://localhost:5000](http://localhost:5000).

---

## **Docker Deployment**

### **1. Build the Docker Image**
Build the Docker image using the provided Dockerfile:
```bash
docker build -t library-api .
```

### **2. Run the Docker Container**
Run the container:
```bash
docker run -p 5000:5000 library-api
```

The API will be accessible at [http://localhost:5000](http://localhost:5000).

---

## **Swagger Documentation**
Interactive API documentation is available using Swagger UI:
1. Run the application.
2. Visit [http://localhost:5000/api-docs](http://localhost:5000/api-docs) in your browser.
3. Test and explore the API endpoints interactively.

---

## **Postman Collection**
A Postman collection containing all API endpoints is included in the project. You can import the collection directly into Postman:
- File: `postman/LibraryAPI.postman_collection.json`

---

## **Folder Structure**
```
.
├── .github/
│   └── workflows/                 # GitHub Actions workflows
│       ├── component-build.yml    # Workflow for building and testing backend changes
│       ├── deployment.yml         # Workflow for deployment to Azure
│       └── pre-merge.yml          # Workflow for validating pull requests
├── postman/                       # Postman collection for testing the API
│   └── LibraryAPI.postman_collection.json
├── swagger/                       # Swagger API documentation
│   └── swagger.yaml
├── app.py                         # Main application file
├── books_data.json                # JSON file storing book data
├── Dockerfile                     # Docker configuration for containerizing the API
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies

```

---

## **Testing the API**
Use **Postman** or **Swagger UI** to test the API endpoints. Below are some example requests:

### **1. Add a New Book**
- **Request**: `POST /books`
- **Body**:
  ```json
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_year": 1925,
    "isbn": "1234567890",
    "genre": "Fiction"
  }
  ```
- **Response**:
  ```json
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_year": 1925,
    "isbn": "1234567890",
    "genre": "Fiction"
  }
  ```

### **2. List All Books**
- **Request**: `GET /books`
- **Response**:
  ```json
  [
    {
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "published_year": 1925,
      "isbn": "1234567890",
      "genre": "Fiction"
    }
  ]
  ```

### **3. Search for Books**
- **Request**: `GET /books/search?author=F.+Scott+Fitzgerald`
- **Response**:
  ```json
  [
    {
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "published_year": 1925,
      "isbn": "1234567890",
      "genre": "Fiction"
    }
  ]
  ```

### **4. Delete a Book**
- **Request**: `DELETE /books/1234567890`
- **Response**:
  ```json
  {
    "message": "Book deleted"
  }
  ```

### **5. Update Book Details**
- **Request**: `PUT /books/1234567890`
- **Body**:
  ```json
  {
    "title": "The Greatest Gatsby"
  }
  ```
- **Response**:
  ```json
  {
    "title": "The Greatest Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_year": 1925,
    "isbn": "1234567890",
    "genre": "Fiction"
  }
  ```

---

## **Deployment on Azure**
The Library Management API is also deployed on Azure. You can access it using the provided Azure Web App URL:
- URL: [https://my-library-app.azurewebsites.net/](https://my-library-app.azurewebsites.net/)

---

