# 3MTT-FELLOW-CAPSTONE-PROJECT
Capstone Project for Fellow with ID - FE/23/30230239

# PROJECT STRUCTURE

e-commerce-app/ <br>
├── docker-compose.yml <br>
├── product-service/ <br>
│   ├── Dockerfile <br>
│   ├── product_service.py <br>
│   └── requirements.txt <br>
├── order-service/ <br>
│   ├── Dockerfile <br>
│   ├── order_service.py <br>
│   └── requirements.txt <br>
└── user-service/ <br>
    ├── Dockerfile <br>
    ├── user_service.py <br>
    └── requirements.txt

# BUILD AND RUN THE CONTAINERS

docker-compose build
docker-compose up

Verify each service by accessing `http://localhost:500X` where X is the service number.
