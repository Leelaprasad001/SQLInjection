# SQL Injection Detection

## Overview

This project aims to detect SQL injection attacks using various machine learning models. SQL injection is a type of cyber attack where malicious SQL statements are inserted into an entry field for execution. Detecting and preventing SQL injection attacks are crucial for ensuring the security of web applications.

## Models Used

- XLNet
- DistilBERT
- 2D-CNN + Bi-LSTM

## Dataset

The dataset used for training and evaluation contains labeled SQL queries, with each query labeled as either "0" or "1".

## Usage

To use the trained models for SQL injection detection:

1. Install the required dependencies.
2. Load the trained model of your choice.
3. Preprocess the incoming SQL queries.
4. Feed the preprocessed queries into the model for prediction.
5. Analyze the model's predictions to determine if the query is legitimate or malicious.
