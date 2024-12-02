# 3MTT-FELLOW-CAPSTONE-PROJECT
Capstone Project for <strong>Cloud Computing Fellow </strong> with ID - FE/23/30230239

# PROJECT DETAILS
E-Commerce micro-services application for small business with item purchase and order functionality. Deployment Using Docker and Google Cloud Platform (GCP).

# PROJECT STRUCTURE

e-commerce-app/ <br>
├── docker-compose.yml <br>
├── requirements.txt <br>
├── product-service/ <br>
│   ├── Dockerfile <br>
│   ├── product_service.py <br>
├── order-service/ <br>
│   ├── Dockerfile <br>
│   ├── order_service.py <br>
└── user-service/ <br>
    ├── Dockerfile <br>
    ├── user_service.py <br>

# BUILD AND RUN THE CONTAINERS

`docker-compose build` <br>
`docker-compose up`

Verify each service by accessing `http://localhost:500X` where X is the service number.
