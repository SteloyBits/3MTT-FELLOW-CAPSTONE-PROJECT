# 3MTT-FELLOW-CAPSTONE-PROJECT
Capstone Project for Fellow with ID - FE/23/30230239

# PROJECT STRUCTURE

e-commerce-app/
├── docker-compose.yml
├── product-service/
│   ├── Dockerfile
│   ├── product_service.py
│   └── requirements.txt
├── order-service/
│   ├── Dockerfile
│   ├── order_service.py
│   └── requirements.txt
└── user-service/
    ├── Dockerfile
    ├── user_service.py
    └── requirements.txt

# BUILD AND RUN THE CONTAINERS

docker-compose build
docker-compose up

Verify each service by accessing `http://localhost:500X` where X is the service number.
