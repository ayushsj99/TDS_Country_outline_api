# 🌍 Country Outline API for GlobalEdu
## This is a academic Project of TDS Subject. IIT-Madras

**Country Outline API** is a RESTful web service built for **GlobalEdu Platforms** to dynamically fetch and structure the content of any country's Wikipedia page. It extracts all headings (`<h1>` to `<h6>`) and returns them in a clean, Markdown-formatted outline — ready to be used in educational tools, apps, and websites.

---

## ✨ Features

- 📘 Accepts a country name as a query parameter  
- 🌐 Fetches the official Wikipedia page of that country  
- 🏗 Extracts all headings (H1 to H6) in order  
- 📄 Returns a **Markdown-formatted** outline  
- 🚀 Enables **CORS** for easy frontend integration  

---

## 🔗 Live Demo

```http
GET https://country-outline-api.onrender.com/api/outline?country=India
