#!/bin/bash

#Populate products data
cd ~/environment/microservices/backend/utils/create_products
python create_products.py
python ~/environment/microservices/backend/utils/s3/create_images_bucket.py

#Populate order data
cd ~/environment/microservices/backend/utils/create_orders
python create_orders.py
