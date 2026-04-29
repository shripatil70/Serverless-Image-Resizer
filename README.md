# 📸 Serverless Image Resizer using AWS Lambda & S3

## 🚀 Project Overview

This project implements a **serverless image processing system** that automatically resizes images when they are uploaded to an Amazon S3 bucket. It leverages AWS services to eliminate the need for server management while ensuring scalability and efficiency.

---

## 🎯 Objective

* Automatically resize images upon upload
* Store processed images in a separate S3 bucket
* Build a scalable and cost-efficient serverless architecture

---

## 🧰 Technologies & Services Used

* **AWS Lambda** – For image processing logic
* **Amazon S3** – For storing original and resized images
* **Python (Pillow Library)** – For image resizing
* **IAM Roles & Policies** – For secure service access

---

## 🏗️ Architecture

1. User uploads an image to the **source S3 bucket**
2. S3 triggers a **Lambda function**
3. Lambda:

   * Downloads the image
   * Resizes it using Pillow
   * Uploads the resized image to the **destination S3 bucket**
4. Output image is stored and accessible

---

## ⚙️ Workflow

* Upload → S3 Bucket
* Trigger → Lambda Function
* Process → Resize Image
* Store → Output S3 Bucket

---

## 📂 Project Structure

```
serverless-image-resizer/
│── lambda_function.py
│── requirements.txt
│── README.md
```

---

## 🔐 IAM Permissions Required

* `s3:GetObject`
* `s3:PutObject`
* `logs:CreateLogGroup`
* `logs:CreateLogStream`
* `logs:PutLogEvents`

---

## 📌 Key Features

* Fully serverless architecture
* Auto-triggered processing
* Scalable and cost-efficient
* No manual intervention required

---

## ⚠️ Challenges Faced

* Handling large image sizes in Lambda
* Managing IAM permissions correctly
* Debugging S3 trigger configurations

---

## 💡 Future Enhancements

* Support multiple image sizes (thumbnail, medium, large)
* Add CloudFront for faster delivery
* Integrate API Gateway for external upload
* Add watermarking functionality

---

## 🧠 Learnings

* Hands-on experience with AWS Lambda triggers
* Event-driven architecture design
* Efficient image processing using Python
* Cloud security using IAM roles

---

## 📌 Conclusion

This project demonstrates how to build a **scalable, event-driven, serverless application** using AWS services, eliminating infrastructure management while ensuring high performance.

---

## 🔗 Author

**Dhanashri Patil**
