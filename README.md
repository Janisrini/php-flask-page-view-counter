# php-flask-page-view-counter
This project is a web-based page view counter that tracks total visits, unique visitors, and access timestamps using PHP, Flask, and MySQL. It also provides a dashboard to monitor page view details in real time.
Project Overview

This project implements a web-based page view tracking system using PHP (frontend), Flask (backend API), and MySQL (database). The system records every page visit along with the timestamp and visitor IP, allowing tracking of total page views and unique visitors. A dashboard provides a clear view of visit statistics, making it suitable for web analytics, academic projects, or beginner-friendly analytics applications.

🔹 Features

Track total page views in real-time.

Identify unique visitors using IP addresses.

Dashboard to view page visit statistics.

REST API endpoints for integration with other web applications.

Store timestamped records in MySQL for historical analysis.

Lightweight and easy to deploy using PHP and Flask.

🔹 Technology Stack

Frontend: PHP, HTML, CSS, JavaScript

Backend: Python Flask API

Database: MySQL

Tools: Postman (for API testing), Browser for dashboard access

🔹 Installation & Setup

Clone the repository:

git clone <repository-url>


Setup MySQL database and import the provided schema.

Update database credentials in the Flask backend and PHP files.

Run the Flask server:

python app.py


Access the PHP frontend through a local server (e.g., Apache or PHP built-in server).

🔹 Usage

Visit the webpage to increment page views.

Use the dashboard to analyze total visits and unique visitor trends.

Integrate API endpoints into other projects to track external page visits.

🔹 Future Enhancements

Add user authentication for dashboard access.

Generate graphs and charts for visual analytics.

Include geolocation tracking based on IP addresses.

Implement real-time notifications for high traffic.

Export data as CSV or Excel for offline analysis.

Add filter options (by date, time, or IP) for detailed reports.

🔹 Contributing

Fork the repository, make changes, and submit a pull request.

Report bugs or suggest features via GitHub issues.
