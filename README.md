
# 🤖 Mina Chatbot - AI Summarizer (BART Model)

Dự án này là hệ thống Chatbot tóm tắt văn bản được xây dựng dựa trên kiến trúc tách biệt Frontend và Backend[cite: 3].

## 📂 Cấu trúc dự án[cite: 3]
*   **backend/**: Chứa mã nguồn xử lý logic, xác thực Firebase và API tóm tắt[cite: 2].
*   **frontend/**: Giao diện người dùng xây dựng bằng Streamlit[cite: 2].
*   **requirements.txt**: Danh sách các thư viện cần thiết[cite: 3].

## 🛠️ Tính năng chính[cite: 3]
*   **Xác thực**: Đăng nhập bằng Google thông qua Firebase Authentication[cite: 2, 3].
*   **AI Summarization**: Sử dụng mô hình **facebook/bart-large-cnn** để tóm tắt văn bản tự động[cite: 2].
*   **Database**: Lưu trữ lịch sử hội thoại vào Google Firestore[cite: 2, 3].

## ⚙️ Hướng dẫn cài đặt[cite: 3]

1.  **Tạo môi trường ảo:**
    
```bash
    python -m venv venv
    source venv/bin/activate  # Trên Windows: venv\Scripts\activate
    ```

2.  **Cài đặt thư viện:**
    
```bash
    pip install -r requirements.txt
    ```

## 🚀 Cách chạy ứng dụng[cite: 3]

Ứng dụng yêu cầu khởi động 3 thành phần theo thứ tự:

1.  **Khởi động Microservice AI (Tóm tắt):**
    
```bash
    uvicorn backend.app.sumarize_bot.main:app --port 8001
    ```
    *(Mô hình BART sẽ được tải tự động trong lần chạy đầu tiên[cite: 2])*

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

---

**Lưu ý quan trọng:** Để ứng dụng hoạt động, bạn cần cấu hình đầy đủ các thông tin Firebase và Google Client ID trong file `.streamlit/secrets.toml`[cite: 2].

---

Huy nhớ dán cái link video demo bạn vừa quay vào mục tương ứng trong `README.md` nhé. Bạn đã chuẩn bị xong file `secrets.toml` để nộp kèm bài (nếu thầy yêu cầu) chưa?
