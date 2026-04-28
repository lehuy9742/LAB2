import streamlit as st
from collections import deque
import requests
import streamlit.components.v1 as components # Thêm dòng này


st.set_page_config(page_title="Mika Frontend", page_icon="💬")
st.write("Dữ liệu User hiện tại:", st.session_state.get("user"))


from api_client import signup, login, google_login, get_messages, send_chat



WELCOME = {"role": "assistant", "content": "Xin chào 👋! Tôi là Mika. Tôi có thể giúp gì cho bạn?"}

if "user" not in st.session_state:
    st.session_state.user = None

if "messages" not in st.session_state:
    st.session_state.messages = deque([WELCOME], maxlen=8)

if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

if "show_login" not in st.session_state:
    st.session_state.show_login = True


def load_history():
    if not st.session_state.user:
        return
    try:
        msgs = get_messages(st.session_state.user["idToken"], limit=8)
        st.session_state.messages = deque(msgs, maxlen=8)
    except Exception:
        st.session_state.messages = deque([WELCOME], maxlen=8)


def clear_google_query_params():
    try:
        st.query_params.clear()
    except Exception:
        pass


# Sửa lại hàm này trong file chatbot-page/frontend/app.py

def handle_google_login_callback():
    if st.session_state.user:
        return

    params = st.query_params
    # Cái id_token ở đây ĐÃ LÀ Firebase Token rồi (do cổng 8000 gửi về)
    token_from_url = params.get("id_token")

    if not token_from_url:
        return

    # Lấy chuỗi token ra khỏi list nếu cần
    final_token = token_from_url[0] if isinstance(token_from_url, list) else token_from_url

    try:
        # --- KHÔNG gọi google_login(id_token) nữa vì sẽ bị lỗi 401 ---
        # Thay vào đó, chúng ta dùng token này để gọi endpoint /me để lấy email và uid
        import requests
        from api_client import API_BASE
        # Chỉ hiện vài ký tự đầu để kiểm tra xem nó có bị dính dấu ngoặc [ ] hay không
        # Gọi thử lên Backend xem token này có "xịn" không
        resp = requests.get(
            f"{API_BASE}/auth/me", 
            headers={"Authorization": f"Bearer {final_token}"}
        )
        resp.raise_for_status()
        user_info = resp.json()

        # Nếu Backend xác nhận thẻ xịn, lưu vào session_state luôn
        st.session_state.user = {
            "email": user_info["email"],
            "uid": user_info["uid"],
            "idToken": final_token
        }
        
        load_history()
        clear_google_query_params()
        st.success("Đăng nhập Google thành công!")
        st.rerun()
        
    except Exception as e:
        st.error(f"Thẻ xác thực không hợp lệ: {e}")
        clear_google_query_params()

def login_form():
    st.subheader("Đăng nhập")

    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Mật khẩu", type="password")
        submitted = st.form_submit_button("Đăng nhập")
        goto_signup = st.form_submit_button("Chưa có tài khoản? Đăng ký")

    if goto_signup:
        st.session_state.show_signup = True
        st.session_state.show_login = False
        st.rerun()

    if submitted:
        try:
            user = login(email, password)
            st.session_state.user = user
            load_history()
            st.success("Đăng nhập thành công")
            st.rerun()
        except requests.HTTPError as e:
            st.error(f"Đăng nhập thất bại: {e}")
        except Exception as e:
            st.error(f"Lỗi đăng nhập: {e}")

    st.markdown("### Hoặc")

    google_login_url = dict(st.secrets["google-login"])["google-url"]

    if google_login_url:
        st.markdown(
        f'''
        <a href="{google_login_url}" target="_self" style="
            display: inline-block;
            width: 100%;
            text-align: center;
            padding: 0.6rem 1rem;
            background-color: white;
            color: black;
            text-decoration: none;
            border-radius: 0.5rem;
            border: 1px solid #ddd;
            font-weight: 600;
        ">
            Đăng nhập với Google
        </a>
        ''',
        unsafe_allow_html=True,
    )
    else:
        st.info(
            "Chưa cấu hình Google-login trong secrets. "
            "Hãy thêm URL đăng nhập Google để dùng tính năng này."
        )


def signup_form():
    st.subheader("Đăng ký")
    with st.form("signup_form"):
        email = st.text_input("Email")
        password = st.text_input("Mật khẩu", type="password")
        submitted = st.form_submit_button("Tạo tài khoản")
        goto_login = st.form_submit_button("Đã có tài khoản? Đăng nhập")

    if goto_login:
        st.session_state.show_signup = False
        st.session_state.show_login = True
        st.rerun()

    if submitted:
        try:
            signup(email, password)
            st.success("Tạo tài khoản thành công, hãy đăng nhập")
            st.session_state.show_signup = False
            st.session_state.show_login = True
            st.rerun()
        except requests.HTTPError as e:
            st.error(f"Đăng ký thất bại: {e}")
        except Exception as e:
            st.error(f"Lỗi đăng ký: {e}")


handle_google_login_callback()

st.title("Mika Chat")

if st.session_state.user:
    st.success(f"Đang đăng nhập: {st.session_state.user['email']}")
    if st.button("Đăng xuất"):
        st.session_state.user = None
        st.session_state.messages = deque([WELCOME], maxlen=8)
        clear_google_query_params()
        st.rerun()
else:
    if st.session_state.show_signup:
        signup_form()
    else:
        login_form()

st.divider()

if st.session_state.user:
    for msg in list(st.session_state.messages):
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt = st.chat_input("Nhập tin nhắn...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            res = send_chat(st.session_state.user["idToken"], prompt)
            reply = res["reply"]
        except Exception as e:
            reply = f"Lỗi backend: {e}"

        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()