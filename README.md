# SWIFTBUY
# 🛒 SwiftBuy - Modern E-Commerce Platform

SwiftBuy is a full-stack e-commerce application built with **Django** and **Bootstrap 5**. It features a sleek, mobile-responsive design with a focus on high-performance UI components, such as native horizontal product sliders.

---

## ✨ Key Features

* **Custom Product Sliders:** Smooth, touch-friendly horizontal scrolling for "Favorite Collections" using CSS Scroll Snap (no bulky JS libraries).
* **Dynamic Catalog:** Real-time rendering of products including T-shirts, Hoodies, Suits, and Accessories.
* **Responsive Design:** Fully optimized for mobile, tablet, and desktop views.
* **Django Backend:** Secure product management, URL routing, and template inheritance.
* **Modern UI:** Clean aesthetic with light-grey product framing and elegant typography.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.x, Django 5.x |
| **Frontend** | HTML5, CSS3, JavaScript (ES6+) |
| **Styling** | Bootstrap 5.3, Bootstrap Icons |
| **Database** | SQLite (Development) |
| **Images** | Unsplash API / Transparent PNGs |


##  Getting Started

### 1. Clone the repository
git clone [https://github.com/YOUR_USERNAME/SwiftBuy.git](https://github.com/YOUR_USERNAME/SwiftBuy.git)
cd SwiftBuy

### 2. Create and Activate Virtual Environment
python -m venv venv
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

### 3. Install Dependencies
pip install django

### 4. Run Migrations & Start Server
python manage.py migrate
python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.

Project Preview
Note: Add a screenshot of your "Favorite Collection" section here to show off that smooth horizontal scroll!


**Project Structure**
SwiftBuy/ - Project configuration
products/ - App handling the clothing logic and templates
static/ - Custom CSS and images
templates/ - HTML files including the navigation and sliders

