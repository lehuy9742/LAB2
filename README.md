
# 🤖 Mina Chatbot - AI Summarizer (BART Model)

Dự án này là hệ thống Chatbot tóm tắt văn bản được xây dựng dựa trên kiến trúc tách biệt Frontend và Backend.
## 👨‍🎓 Thông tin sinh viên
* **Họ và tên:** Lê Nguyễn Gia Huy
* **Mã số sinh viên (MSSV):** 24120061
* **Trường:** Đại học Khoa học Tự nhiên TP.HCM (VNU-HCMUS)
* **Khoa:** Công nghệ Thông tin
* **Lớp:** 24CTT3

## 📂 Cấu trúc dự án
*   **backend/**: Chứa mã nguồn xử lý logic, xác thực Firebase và API tóm tắt.
*   **frontend/**: Giao diện người dùng xây dựng bằng Streamlit.
*   **requirements.txt**: Danh sách các thư viện cần thiết.

## 🛠️ Tính năng chính
*   **Xác thực**: Đăng nhập bằng Google thông qua Firebase Authentication.
*   **AI Summarization**: Sử dụng mô hình **facebook/bart-large-cnn** để tóm tắt văn bản tự động.
*   **Database**: Lưu trữ lịch sử hội thoại vào Google Firestore.

## ⚙️ Hướng dẫn cài đặt

1.  **Tạo môi trường ảo:**
    
```bash
    python -m venv venv
    source venv/bin/activate  # Trên Windows: venv\Scripts\activate
    ```

2.  **Cài đặt thư viện:**
    
```bash
    pip install -r requirements.txt
    ```

## 🚀 Cách chạy ứng dụng

Ứng dụng yêu cầu khởi động 3 thành phần theo thứ tự:

1.  **Khởi động Microservice AI (Tóm tắt):**
    
```bash
    uvicorn backend.app.sumarize_bot.main:app --port 8001
    ```
    *(Mô hình BART sẽ được tải tự động trong lần chạy đầu tiên)*

2.  **Khởi động Main Backend:**
    
```bash
    uvicorn backend.app.main:app --port 8000
    ```

3.  **Khởi động Frontend:**
    ```bash
    streamlit run frontend/app.py
    ```

## 🎥 Video Demo[cite: 3]
*   **Link Video**: [Dán link Youtube/Google Drive của bạn vào đây]


https://github.com/user-attachments/assets/85084957-6c9c-4e38-917c-0f7e09619703


---

**Lưu ý quan trọng:** Để ứng dụng hoạt động, bạn cần cấu hình đầy đủ các thông tin Firebase và Google Client ID trong file `.streamlit/secrets.toml`.

---
