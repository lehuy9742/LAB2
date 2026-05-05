# 🤖 Mina Chatbot - AI Summarizer (BART Model)

Dự án này là hệ thống Chatbot tóm tắt văn bản được xây dựng cho **Bài thực hành số 2** môn Tư duy tính toán. Ứng dụng tách biệt hoàn toàn giữa Frontend và Backend.

## 👤 Thông tin sinh viên
*   **Họ và tên:** Lê Nguyễn Gia Huy
*   **MSSV:** 24120061
*   **Trường:** ĐH Khoa học Tự nhiên (VNU-HCMUS)

---

## 📂 Cấu trúc dự án
*   **`backend/`**: Xử lý logic, xác thực Firebase và API.
*   **`frontend/`**: Giao diện người dùng Streamlit.
*   **`requirements.txt`**: Danh sách thư viện cần thiết.

---

## 🛠️ Công nghệ sử dụng
*   **Framework**: FastAPI & Streamlit.
*   **Authentication**: Firebase Authentication.
*   **AI Model**: BART (facebook/bart-large-cnn).

---

## ⚙️ Hướng dẫn cài đặt

1. **Tạo môi trường ảo:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Trên Windows: venv\Scripts\activate
   ```

2. **Cài đặt thư viện:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Hướng dẫn khởi chạy
Mở 3 Terminal riêng biệt và chạy theo thứ tự:

1. **Khởi động Microservice AI (Port 8001):**
   
```bash
   uvicorn backend.app.sumarize_bot.main:app --port 8001
   ```

2. **Khởi động Main Backend (Port 8000):**
   ```bash
   uvicorn backend.app.main:app --port 8000
   ```

3. **Khởi động Frontend (Port 8501):**
   ```bash
   streamlit run frontend/app.py
   ```

---

## 🎥 Video Demo
https://github.com/user-attachments/assets/85084957-6c9c-4e38-917c-0f7e09619703





---

**Lưu ý quan trọng:** Để ứng dụng hoạt động, bạn cần cấu hình đầy đủ các thông tin Firebase và Google Client ID trong file `.streamlit/secrets.toml`.

---
