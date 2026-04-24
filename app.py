import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import requests
import time

# ==========================================
# CẤU HÌNH TRANG
# ==========================================
st.set_page_config(page_title="Báo cáo Nghiên cứu Python & AI", page_icon="✨", layout="wide")

# ==========================================
# CÁC HÀM HIỂN THỊ NỘI DUNG TỪNG TRANG
# ==========================================

def page_home():
    st.title("✨ Cổng Thông Tin & Báo Cáo Tương Tác")
    st.markdown("### 🎓 Ứng dụng Python trong Khoa học Dữ liệu & AI")
    st.divider()
    
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("""
        Chào mừng bạn đến với **Cổng thông tin báo cáo tương tác thế hệ mới**. 
        Dự án này được thiết kế đột phá, chuyển đổi các văn bản báo cáo truyền thống thành một trang web giáo dục có thể **thực thi mã nguồn và tương tác trực tiếp**.
        
        #### 🔍 Nội dung chính bao gồm:
        1. **Thư viện Khoa học Dữ liệu (Data Stack):** NumPy, Pandas, Matplotlib, Seaborn.
        2. **Thư viện Lõi & Học Máy (Core & ML):** Scikit-Learn, Requests.
        3. **Kiến trúc Trí tuệ Nhân tạo (Advanced AI):** Giao thức kết nối MCP và Hệ thống Đa tác nhân (A2A).
        """)
        st.info("👉 **Hướng dẫn sử dụng:** Hãy sử dụng thanh Menu bên trái để chuyển đổi giữa các bài học. Trong mỗi bài học, hãy chuyển qua lại giữa Tab **Báo cáo Lý thuyết** và Tab **Chương trình Demo** để trải nghiệm.")
        
    with col2:
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80", use_container_width=True)

def page_numpy():
    st.title("1. Thư viện NumPy (Numerical Python)")
    tab1, tab2 = st.tabs(["📖 Báo cáo Lý thuyết", "⚙️ Chương trình Demo"])
    
    with tab1:
        st.markdown("""
        **NumPy** là thư viện toán học nền tảng, được coi là trái tim của hệ sinh thái Khoa học dữ liệu trong Python.
        *   **Cấu trúc cốt lõi (`ndarray`):** Là mảng N-chiều được tối ưu hóa siêu cấp. Các phần tử được lưu trữ liền kề nhau trên RAM và được xử lý bằng ngôn ngữ C bên dưới, giúp tốc độ siêu nhanh.
        *   **Vectorization (Véc-tơ hóa):** Khả năng thực hiện tính toán trên toàn bộ mảng cùng một lúc, loại bỏ hoàn toàn việc sử dụng các vòng lặp `for` chậm chạp của Python.
        *   **Broadcasting:** Cơ chế thông minh tự động mở rộng và cân bằng kích thước giữa các mảng khác nhau để thực hiện phép toán.
        """)
        st.code("import numpy as np\narr = np.array([1, 2, 3])\n# Vectorization: Nhân toàn bộ mảng cho 10\nprint(arr * 10)", language="python")

    with tab2:
        st.markdown("### 🎯 Trải nghiệm Vectorization")
        st.write("Sinh ra một ma trận dữ liệu ngẫu nhiên và áp dụng phép tính véc-tơ siêu tốc (nhân toàn bộ cho 10).")
        col1, col2 = st.columns(2)
        with col1:
            rows = st.number_input("Chọn số dòng (Rows):", 1, 10, 3)
        with col2:
            cols = st.number_input("Chọn số cột (Columns):", 1, 10, 3)
            
        if st.button("🚀 Khởi tạo & Tính toán Ma trận", type="primary"):
            matrix = np.random.randint(1, 10, size=(rows, cols))
            c1, c2 = st.columns(2)
            with c1:
                st.success("1. Ma trận gốc (A):")
                st.dataframe(matrix, use_container_width=True)
            with c2:
                st.info("2. Ma trận kết quả (A × 10):")
                st.dataframe(matrix * 10, use_container_width=True)

def page_pandas():
    st.title("2. Thư viện Pandas")
    tab1, tab2 = st.tabs(["📖 Báo cáo Lý thuyết", "⚙️ Chương trình Demo"])
    
    with tab1:
        st.markdown("""
        Nếu NumPy làm việc với mảng số học, **Pandas** là công cụ "cứu cánh" chuyên trị dữ liệu thực tế, được mệnh danh là "Excel của lập trình viên".
        *   **Cấu trúc dữ liệu:** `Series` (Mảng 1 chiều có gắn index) và `DataFrame` (Bảng 2 chiều, tương tự bảng CSDL hay Excel).
        *   **Nhiệm vụ chính:**
            *   *Data Cleaning (Làm sạch):* Xử lý cực tốt các ô trống, giá trị lỗi (`fillna()`, `dropna()`).
            *   *Data Wrangling (Nhào nặn):* Gom nhóm thống kê (`groupby()`), Gộp nhiều bảng lại với nhau (`merge()`, `join`), Tạo báo cáo đa chiều (`pivot_table()`).
        """)
        st.code("import pandas as pd\n# Gom nhóm dữ liệu và tính tổng doanh thu theo khu vực\nbao_cao = df.groupby('Khu vực')['Doanh thu'].sum()", language="python")

    with tab2:
        st.markdown("### 🎯 Trải nghiệm Data Cleaning & Grouping")
        st.write("Dưới đây là tập dữ liệu kinh doanh thô đang bị lỗi (bị thiếu dữ liệu - `NaN`). Hãy chạy Data Pipeline để Pandas tự động dọn dẹp và báo cáo.")
        
        df_raw = pd.DataFrame({
            'Khu_Vực': ['Miền Bắc', 'Miền Nam', 'Miền Bắc', 'Miền Nam', 'Miền Trung'],
            'Doanh_Thu_Triệu': [120, 250, np.nan, 310, 150]
        })
        st.warning("📉 **Dữ liệu thô ban đầu (Lỗi NaN ở dòng 2):**")
        st.dataframe(df_raw, use_container_width=True)
        
        if st.button("🚀 Thực thi Data Pipeline", type="primary"):
            with st.spinner("Đang chạy thuật toán làm sạch và gom nhóm..."):
                time.sleep(0.5)
                # Thuật toán điền NaN bằng giá trị trung bình
                mean_val = df_raw['Doanh_Thu_Triệu'].mean()
                df_clean = df_raw.copy()
                df_clean['Doanh_Thu_Triệu'] = df_clean['Doanh_Thu_Triệu'].fillna(mean_val)
                
                # Thuật toán gom nhóm
                summary = df_clean.groupby('Khu_Vực').sum().reset_index()
                
                c1, c2 = st.columns(2)
                with c1:
                    st.success("✅ Dữ liệu đã được làm sạch:")
                    st.dataframe(df_clean, use_container_width=True)
                with c2:
                    st.info("📊 Báo cáo Gom nhóm (Groupby):")
                    st.dataframe(summary, use_container_width=True)

def page_visualization():
    st.title("3. Trực quan hóa: Matplotlib & Seaborn")
    tab1, tab2 = st.tabs(["📖 Báo cáo Lý thuyết", "⚙️ Chương trình Demo"])
    
    with tab1:
        st.markdown("""
        Số liệu sẽ rất khô khan nếu không được vẽ thành biểu đồ. Chúng ta có 2 công cụ đắc lực:
        *   **Matplotlib:** Gốc rễ của trực quan hóa trong Python. Cho phép bạn can thiệp vào từng pixel, vẽ mọi loại biểu đồ nhưng cú pháp khá dài và phức tạp.
        *   **Seaborn:** Nâng cấp từ Matplotlib. Cung cấp các giao diện (themes) tuyệt đẹp và khả năng vẽ các biểu đồ thống kê phức tạp (ví dụ: Heatmap, Violin plot) chỉ với 1 dòng code duy nhất.
        """)
        st.code('import seaborn as sns\nimport matplotlib.pyplot as plt\n\n# Vẽ biểu đồ phân phối với đường cong mật độ (KDE)\nsns.histplot(data, kde=True)\nplt.show()', language="python")

    with tab2:
        st.markdown("### 🎯 Trải nghiệm Đồ họa Thống kê")
        st.write("Tạo một tập dữ liệu phân phối ngẫu nhiên và dùng Seaborn để vẽ biểu đồ mật độ chuẩn.")
        if st.button("🚀 Khởi tạo Dữ liệu & Vẽ Biểu đồ", type="primary"):
            with st.spinner("Đang render Engine đồ họa..."):
                data = np.random.randn(1000)
                sns.set_style("darkgrid") # Tương thích tốt với cả giao diện tối/sáng
                fig, ax = plt.subplots(figsize=(8, 4))
                
                # Vẽ biểu đồ với Seaborn
                sns.histplot(data, kde=True, ax=ax, color="#3B82F6", edgecolor="white")
                ax.set_title("Biểu đồ Phân phối Chuẩn (Normal Distribution)", fontweight="bold", pad=15)
                ax.set_xlabel("Giá trị ngẫu nhiên")
                ax.set_ylabel("Tần suất xuất hiện")
                sns.despine() # Làm sạch viền thừa
                
                st.pyplot(fig)

def page_sklearn():
    st.title("4. Học máy: Scikit-Learn")
    tab1, tab2 = st.tabs(["📖 Báo cáo Lý thuyết", "⚙️ Chương trình Demo"])
    
    with tab1:
        st.markdown("""
        **Scikit-Learn** là "trường học" của mọi kỹ sư AI, thư viện nền tảng số một cho Machine Learning truyền thống.
        *   **Thuật toán phong phú:** Từ Hồi quy (Linear Regression), Phân loại (Random Forest, SVM) cho đến Gom cụm (K-Means).
        *   **Tiền xử lý & Đánh giá:** Cung cấp đầy đủ công cụ chuẩn hóa dữ liệu (StandardScaler) và tính toán độ chính xác.
        *   **Tính nhất quán tuyệt vời:** Dù thuật toán có phức tạp đến đâu, bạn cũng chỉ cần gọi 2 hàm quen thuộc là `model.fit()` (Học dữ liệu) và `model.predict()` (Dự đoán).
        """)
        st.code("from sklearn.linear_model import LinearRegression\nmodel = LinearRegression()\nmodel.fit(X_train, y_train) # Bắt đầu học\nprediction = model.predict(X_new) # Dự đoán", language="python")

    with tab2:
        st.markdown("### 🎯 Huấn luyện Trí tuệ Nhân tạo (AI)")
        st.write("Sử dụng thuật toán Hồi quy tuyến tính (Linear Regression) để AI học cách định giá nhà đất dựa trên diện tích.")
        
        area = st.slider("📐 Hãy chọn diện tích căn nhà (m²):", 30, 200, 75)
        
        if st.button("🚀 Chạy Mô hình AI & Dự đoán", type="primary"):
            with st.spinner("AI đang học từ dữ liệu lịch sử..."):
                time.sleep(0.5)
                # Dữ liệu đào tạo giả lập
                X = np.array([30, 50, 70, 90, 110, 150]).reshape(-1, 1)
                y = np.array([1.2, 2.0, 2.9, 3.8, 4.5, 6.0]) # Tỷ VNĐ
                
                # Khởi tạo và huấn luyện
                model = LinearRegression()
                model.fit(X, y)
                
                # Dự đoán kết quả mới
                pred = model.predict([[area]])[0]
                
                st.metric(label="🏠 Giá nhà định giá bởi AI", value=f"{pred:.2f} Tỷ VNĐ", delta="Độ tin cậy cao")
                st.info("💡 **Giải thích:** AI đã nội suy được rằng hệ số giá nhà tăng đều theo diện tích và đưa ra kết quả tương ứng cho con số bạn chọn.")

def page_requests():
    st.title("5. Giao tiếp Mạng: Requests")
    tab1, tab2 = st.tabs(["📖 Báo cáo Lý thuyết", "⚙️ Chương trình Demo"])
    
    with tab1:
        st.markdown("""
        **Requests** được thế giới lập trình mệnh danh là *"HTTP for Humans"* (Giao thức HTTP làm ra dành cho con người).
        *   **Khái niệm:** Thư viện không thể thiếu giúp Python kết nối Internet, cào dữ liệu web (Web Scraping) hoặc tương tác với REST API.
        *   **Ưu điểm:** Khắc phục hoàn toàn sự phức tạp kinh khủng của thư viện `urllib` mặc định trong Python. Nó có khả năng tự động xử lý và chuyển đổi chuỗi mã hóa JSON thành định dạng Dictionary quen thuộc của Python.
        """)
        st.code("import requests\n# Lấy dữ liệu từ Github\nres = requests.get('https://api.github.com')\nprint(res.json())", language="python")

    with tab2:
        st.markdown("### 🎯 Gọi API Thời gian thực (Real-time)")
        st.write("Chương trình này sẽ gửi lệnh đến Server của sàn giao dịch tiền ảo thế giới để lấy tỷ giá mới nhất.")
        
        if st.button("🚀 Cập nhật Giá Bitcoin ngay lúc này", type="primary"):
            with st.spinner("Đang gửi HTTP GET request ra Internet..."):
                try:
                    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                    data = res.json() # Dịch ngược JSON tự động
                    
                    price = data['bpi']['USD']['rate']
                    time_updated = data['time']['updated']
                    
                    # Trình bày giao diện Dashboard
                    c1, c2 = st.columns(2)
                    c1.metric(label="💰 Tỷ giá Bitcoin (Theo USD)", value=f"${price}", delta="Live API")
                    c2.metric(label="⏱️ Dữ liệu chốt lúc", value=time_updated)
                    
                    st.success("Bóc tách dữ liệu JSON thành công từ API!")
                except Exception as e:
                    st.error("Lỗi khi kết nối mạng. Hãy đảm bảo bạn có Internet.")

def page_mcp():
    st.title("6. Giao thức MCP (Model Context Protocol)")
    tab1, tab2 = st.tabs(["📖 Báo cáo Lý thuyết", "⚙️ Chương trình Demo"])
    
    with tab1:
        st.markdown("""
        **MCP** là phát minh đột phá nhất năm 2024 của hãng Anthropic, được cộng đồng ví như *"Cổng USB-C của ngành Trí tuệ Nhân tạo"*.
        
        *   **Nỗi đau của lập trình viên:** Trước đây các AI (như ChatGPT) bị nhốt trong một hộp đen. Để AI đọc được file máy tính hay kết nối Github, lập trình viên phải viết code Custom riêng biệt rất cực khổ.
        *   **Kiến trúc Chuẩn hóa của MCP:** Cung cấp chuẩn giao tiếp **JSON-RPC** an toàn tuyệt đối.
            *   Máy chủ của bạn (Local) chạy một `MCP Server`.
            *   Mô hình AI đóng vai trò `MCP Client`.
        *   **3 Trụ cột MCP cung cấp cho AI:**
            1. **Resources:** Quyền đọc dữ liệu nội bộ (VD: Đọc file log hệ thống).
            2. **Tools:** Quyền hành động thực tế (VD: Chạy lệnh git, tạo file, truy vấn SQL).
            3. **Prompts:** Gợi ý lệnh được tinh chỉnh sẵn cho người dùng.
        """)

    with tab2:
        st.markdown("### 🎯 Mô phỏng Luồng Giao tiếp bảo mật")
        st.info("Kịch bản: LLM cần đếm số lượng người dùng trong Database nội bộ, nhưng nó không có quyền kết nối trực tiếp. Nó phải mượn tay MCP Server thông qua lệnh `tools/call`.")
        
        if st.button("🚀 Khởi chạy Luồng MCP Tool-Calling", type="primary"):
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("#### 📤 LLM Request (Client)")
                time.sleep(1)
                st.code('{\n  "method": "tools/call",\n  "params": {\n    "name": "query_db"\n  }\n}', language='json')
                
            with c2:
                st.markdown("#### 📥 MCP Server (Response)")
                time.sleep(1.5)
                st.write("*(Server thực thi an toàn trên máy Local và trả kết quả về)*")
                st.code('{\n  "result": {\n    "content": [\n      {"text": "Có 1054 User."}\n    ]\n  }\n}', language='json')
            st.success("✅ **Luồng an toàn:** LLM lấy được dữ liệu Private cục bộ mà không phá vỡ rào cản bảo mật nào.")

def page_a2a():
    st.title("7. Kiến trúc A2A (Agent-to-Agent)")
    tab1, tab2 = st.tabs(["📖 Báo cáo Lý thuyết", "⚙️ Chương trình Demo"])
    
    with tab1:
        st.markdown("""
        **Kiến trúc Đa tác nhân (Multi-Agent System)** biến AI từ một "Trợ lý ảo đơn độc" thành "Cả một tập đoàn ảo".
        
        *   **Khái niệm:** Một hệ thống chia bài toán lớn cho nhiều Agent (Đặc vụ AI). Mỗi Agent được thiết lập một `Role` (Vai trò) và cấp các `Tool` (Công cụ) riêng biệt.
        *   **Vì sao hiệu quả hơn 1 LLM siêu lớn?**
            *   *Giảm ảo giác:* Mỗi Agent tập trung làm 1 việc duy nhất (VD: Agent A chỉ chuyên viết code, Agent B chỉ chuyên kiểm lỗi).
            *   *Cơ chế tự sửa sai (Self-healing):* Các Agent có thể tranh luận, bắt lỗi chéo và phản biện lẫn nhau cho đến khi ra kết quả chính xác 100%.
        *   **Ứng dụng:** Các framework nổi tiếng như CrewAI, LangGraph, AutoGen đang cách mạng hóa ngành Software Engineering khi tạo ra các "công ty phần mềm" chỉ gồm AI.
        """)

    with tab2:
        st.markdown("### 🎯 Mô phỏng Hoạt động Phân cấp (Hierarchical)")
        st.write("Xem cách một Manager Agent điều động cấp dưới làm việc như con người.")
        
        if st.button("🚀 Khởi chạy Swarm Agent", type="primary"):
            with st.status("📡 Đang giám sát luồng giao tiếp Đa tác nhân...", expanded=True):
                st.write("👤 **User Task:** *'Hãy thống kê doanh thu và vẽ báo cáo.'*")
                time.sleep(1)
                st.write("🧠 **[Manager Agent]:** Đã nhận lệnh. Lập kế hoạch và điều động `Data Analyst` và `Designer`.")
                time.sleep(1)
                st.markdown("---")
                st.write("🧑‍💻 **[Analyst Agent]:** (Sử dụng Python Tool) Truy cập CSDL. Tổng hợp doanh thu tăng 15% so với năm ngoái.")
                time.sleep(1.5)
                st.write("🎨 **[Designer Agent]:** (Nhận data từ Analyst) Đang tạo bản nháp biểu đồ... Hoàn thiện và lưu thành PDF.")
                time.sleep(1)
                st.markdown("---")
                st.write("📢 **[Manager Agent]:** Đóng gói báo cáo PDF và trả về cho User.")
            st.success("✅ **Kết quả Workflow:** Phối hợp nhịp nhàng, tốc độ cao, không xảy ra ảo giác sai sót dữ liệu.")

def main():
    st.sidebar.title("📑 Danh mục Bài học")
    st.sidebar.markdown("---")
    
    pages = {
        "🏠 Trang chủ & Tổng quan": page_home,
        "🔢 1. Thư viện NumPy": page_numpy,
        "🐼 2. Thư viện Pandas": page_pandas,
        "📊 3. Matplotlib & Seaborn": page_visualization,
        "🧠 4. Scikit-Learn (AI)": page_sklearn,
        "🌐 5. Thư viện Requests": page_requests,
        "🔌 6. Giao thức MCP": page_mcp,
        "🤖 7. Kiến trúc A2A": page_a2a
    }
    
    selection = st.sidebar.radio("CHỌN BÀI HỌC:", list(pages.keys()), label_visibility="collapsed")
    
    st.sidebar.markdown("---")
    st.sidebar.caption("👨‍💻 *Built with Streamlit & AI*")
    
    pages[selection]()

if __name__ == "__main__":
    main()
