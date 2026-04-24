import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import requests
import time
import io

# ==========================================
# CẤU HÌNH TRANG
# ==========================================
st.set_page_config(page_title="Assignment - Program with Python", page_icon="📝", layout="wide")

# ==========================================
# CÁC HÀM HIỂN THỊ NỘI DUNG TỪNG TRANG
# ==========================================

def page_home():
    st.title("📝 Báo cáo Assignment Tương tác")
    st.markdown("### 🎓 Môn học: Program with Python")
    st.divider()
    
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("""
        Chào mừng Giảng viên đến với **Báo cáo Assignment tương tác** được xây dựng bằng framework Streamlit. 
        Dự án này được thực hiện nhằm mục đích tổng hợp lý thuyết và demo thực hành các kiến thức trọng tâm của môn học **Program with Python**.
        
        #### 🔍 Nội dung báo cáo bao gồm:
        1. **Thư viện Khoa học Dữ liệu cơ bản:** Xử lý và trực quan hóa dữ liệu với NumPy, Pandas, Matplotlib, Seaborn.
        2. **Ứng dụng nâng cao:** Xây dựng mô hình Học máy cơ bản (Scikit-Learn) và Giao tiếp mạng (Requests).
        3. **Nghiên cứu thêm (Advanced AI):** Tìm hiểu cấu trúc hoạt động của giao thức MCP và Hệ thống Đa tác nhân (A2A).
        """)
        st.info("👉 **Hướng dẫn chấm điểm:** Giảng viên có thể sử dụng thanh Menu bên trái để điều hướng. Tại mỗi phần, hệ thống được chia thành 2 Tab: **Báo cáo Lý thuyết** (Phân tích, code mẫu) và **Chương trình Demo** (Chạy thử nghiệm tương tác trực tiếp).")
        
    with col2:
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80", use_container_width=True)

def page_numpy():
    st.title("1. Thư viện NumPy (Numerical Python)")
    tab1, tab2 = st.tabs(["📖 Báo cáo Lý thuyết", "⚙️ Chương trình Demo"])
    
    with tab1:
        st.markdown("""
        **NumPy** là thư viện cốt lõi hỗ trợ tính toán mảng và ma trận nhiều chiều trong Python.
        *   **Cấu trúc dữ liệu (`ndarray`):** Là mảng N-chiều tối ưu bộ nhớ. Do các phần tử được lưu trữ liền kề nhau và được xử lý bằng C/C++ ở tầng thấp, NumPy cho hiệu suất tính toán vượt trội so với list thông thường của Python.
        *   **Vectorization (Véc-tơ hóa):** Cho phép thực hiện phép toán trên toàn bộ mảng mà không cần sử dụng vòng lặp `for`, giúp code ngắn gọn và thực thi nhanh hơn.
        *   **Broadcasting:** Cơ chế cho phép thực hiện các phép toán giữa các mảng có kích thước (shape) khác nhau.
        """)
        st.code("import numpy as np\narr = np.array([1, 2, 3])\n# Vectorization: Nhân toàn bộ phần tử trong mảng cho 10\nprint(arr * 10)", language="python")

    with tab2:
        st.markdown("### 🎯 Demo: Tính toán Véc-tơ hóa (Vectorization)")
        st.write("Chương trình tạo ra một ma trận dữ liệu ngẫu nhiên dựa trên đầu vào và áp dụng phép nhân ma trận.")
        col1, col2 = st.columns(2)
        with col1:
            rows = st.number_input("Nhập số dòng (Rows):", 1, 10, 3)
        with col2:
            cols = st.number_input("Nhập số cột (Columns):", 1, 10, 3)
            
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
        **Pandas** là thư viện mạnh mẽ nhất để phân tích và thao tác với dữ liệu dạng bảng (tương tự SQL hoặc Excel).
        *   **Cấu trúc dữ liệu:** 
            *   `Series`: Mảng 1 chiều có gắn nhãn (index).
            *   `DataFrame`: Bảng 2 chiều có cấu trúc cột và dòng.
        *   **Tính năng chính:**
            *   *Làm sạch dữ liệu (Data Cleaning):* Xử lý các giá trị bị thiếu (`NaN`) bằng hàm `fillna()` hoặc `dropna()`.
            *   *Thao tác dữ liệu:* Lọc, gom nhóm (`groupby()`), kết hợp bảng (`merge()`, `join`).
        """)
        st.code("import pandas as pd\n# Gom nhóm dữ liệu và tính tổng doanh thu theo khu vực\nbao_cao = df.groupby('Khu vực')['Doanh thu'].sum()", language="python")

    with tab2:
        st.markdown("### 🎯 Demo 1: Làm sạch và Gom nhóm dữ liệu")
        st.write("Mô phỏng quá trình xử lý một tập dữ liệu kinh doanh bị lỗi (chứa giá trị `NaN`). Chương trình sẽ làm sạch dữ liệu và thống kê tổng doanh thu.")
        
        df_raw = pd.DataFrame({
            'Khu_Vực': ['Miền Bắc', 'Miền Nam', 'Miền Bắc', 'Miền Nam', 'Miền Trung'],
            'Doanh_Thu_Triệu': [120, 250, np.nan, 310, 150]
        })
        st.warning("📉 **Dữ liệu ban đầu (Cố tình tạo lỗi NaN ở dòng 2):**")
        st.dataframe(df_raw, use_container_width=True)
        
        if st.button("🚀 Chạy thuật toán xử lý dữ liệu", type="primary"):
            with st.spinner("Đang làm sạch và gom nhóm..."):
                time.sleep(0.5)
                # Xử lý NaN bằng cách lấy giá trị trung bình
                mean_val = df_raw['Doanh_Thu_Triệu'].mean()
                df_clean = df_raw.copy()
                df_clean['Doanh_Thu_Triệu'] = df_clean['Doanh_Thu_Triệu'].fillna(mean_val)
                
                # Thống kê bằng groupby
                summary = df_clean.groupby('Khu_Vực').sum().reset_index()
                
                c1, c2 = st.columns(2)
                with c1:
                    st.success("✅ Dữ liệu sau khi xử lý NaN:")
                    st.dataframe(df_clean, use_container_width=True)
                with c2:
                    st.info("📊 Báo cáo Gom nhóm (Groupby):")
                    st.dataframe(summary, use_container_width=True)
                    
        st.divider()
        
        st.markdown("### 🎯 Demo 2: Xử lý file Excel Thực tế")
        st.write("Giảng viên có thể tải lên một file Excel (`.xlsx`) hoặc CSV để thuật toán Pandas phân tích trực tiếp. Hoặc có thể tải file mẫu bên dưới để test.")
        
        # Nút tải file mẫu
        sample_data = pd.DataFrame({
            "Sản Phẩm": ["Laptop", "Chuột", "Bàn Phím", "Màn hình", "Tai nghe", "Loa Bluetooth", "Webcam"],
            "Doanh Số": [120, 500, 300, 80, 200, 150, 90],
            "Giá Bán": [15000000, 200000, 500000, 3000000, 800000, 600000, 400000]
        })
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            sample_data.to_excel(writer, index=False)
        
        st.download_button(
            label="⬇️ Tải file Excel Mẫu (Sample.xlsx)",
            data=buffer.getvalue(),
            file_name="Sample.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        
        # Upload file và xử lý
        uploaded_file = st.file_uploader("Upload file Excel/CSV để xử lý:", type=["xlsx", "csv"])
        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith('.csv'):
                    df_user = pd.read_csv(uploaded_file)
                else:
                    df_user = pd.read_excel(uploaded_file)
                
                st.success(f"Đọc file `{uploaded_file.name}` thành công!")
                
                # Tính toán thêm một cột mới
                if 'Doanh Số' in df_user.columns and 'Giá Bán' in df_user.columns:
                    df_user['Tổng Thu'] = df_user['Doanh Số'] * df_user['Giá Bán']
                    
                st.write("🔍 **Dữ liệu sau khi đọc (Có tự động tính thêm cột Tổng Thu nếu hợp lệ):**")
                st.dataframe(df_user, use_container_width=True)
                
                st.write("📊 **Thống kê mô tả (Descriptive Statistics) tự động:**")
                st.dataframe(df_user.describe(), use_container_width=True)
            except Exception as e:
                st.error(f"Lỗi khi xử lý file: {e}")

def page_visualization():
    st.title("3. Trực quan hóa: Matplotlib & Seaborn")
    tab1, tab2 = st.tabs(["📖 Báo cáo Lý thuyết", "⚙️ Chương trình Demo"])
    
    with tab1:
        st.markdown("""
        Trong Python, trực quan hóa dữ liệu thường sử dụng hai thư viện cơ bản và nâng cao:
        *   **Matplotlib:** Cung cấp các công cụ đồ họa mức thấp. Khả năng tùy biến cực cao, có thể vẽ biểu đồ đường (line), cột (bar), tròn (pie), phân tán (scatter), v.v.
        *   **Seaborn:** Được xây dựng dựa trên Matplotlib. Cung cấp API bậc cao hơn, tối ưu hóa để vẽ các biểu đồ thống kê phức tạp (ví dụ: Heatmap, Violin plot) với giao diện mặc định chuyên nghiệp hơn và code ngắn gọn hơn.
        """)
        st.code('import seaborn as sns\nimport matplotlib.pyplot as plt\n\n# Vẽ biểu đồ mật độ phân phối (KDE)\nsns.histplot(data, kde=True)\nplt.show()', language="python")

    with tab2:
        st.markdown("### 🎯 Demo: Vẽ biểu đồ phân phối chuẩn")
        st.write("Sử dụng thư viện Seaborn để trực quan hóa dữ liệu ngẫu nhiên (1000 phần tử) dưới dạng đồ thị Histogram kết hợp đường KDE.")
        if st.button("🚀 Khởi tạo Dữ liệu ngẫu nhiên & Vẽ đồ thị", type="primary"):
            with st.spinner("Đang khởi tạo đồ họa..."):
                data = np.random.randn(1000)
                sns.set_style("darkgrid")
                fig, ax = plt.subplots(figsize=(8, 4))
                
                # Vẽ biểu đồ
                sns.histplot(data, kde=True, ax=ax, color="#3B82F6", edgecolor="white")
                ax.set_title("Biểu đồ Phân phối Chuẩn (Normal Distribution)", fontweight="bold", pad=15)
                ax.set_xlabel("Giá trị")
                ax.set_ylabel("Tần suất")
                sns.despine() 
                
                st.pyplot(fig)

def page_sklearn():
    st.title("4. Học máy cơ bản: Scikit-Learn")
    tab1, tab2 = st.tabs(["📖 Báo cáo Lý thuyết", "⚙️ Chương trình Demo"])
    
    with tab1:
        st.markdown("""
        **Scikit-Learn** là thư viện tiêu chuẩn dùng cho Machine Learning (Học máy) trong Python.
        *   **Chức năng:** Cung cấp các thuật toán phân loại (Classification), hồi quy (Regression), gom cụm (Clustering) và giảm chiều dữ liệu (Dimensionality reduction).
        *   **Quy trình chuẩn hóa:** Scikit-Learn định nghĩa một quy trình nhất quán đối với mọi thuật toán:
            1. Khởi tạo mô hình (Ví dụ: `model = LinearRegression()`).
            2. Huấn luyện mô hình với dữ liệu bằng hàm `model.fit(X, y)`.
            3. Đưa ra dự đoán bằng hàm `model.predict(X_new)`.
        """)
        st.code("from sklearn.linear_model import LinearRegression\nmodel = LinearRegression()\nmodel.fit(X_train, y_train) # Huấn luyện\nprediction = model.predict(X_test) # Dự đoán", language="python")

    with tab2:
        st.markdown("### 🎯 Demo: Mô hình Hồi quy tuyến tính (Linear Regression)")
        st.write("Ứng dụng thuật toán Học máy để dự đoán giá nhà dựa trên diện tích. Mô hình sẽ được huấn luyện trực tiếp trên một tập dữ liệu giả lập (Mock data).")
        
        area = st.slider("📐 Nhập diện tích căn nhà cần dự đoán (m²):", 30, 200, 75)
        
        if st.button("🚀 Huấn luyện Mô hình & Dự đoán", type="primary"):
            with st.spinner("Đang huấn luyện mô hình (Training)..."):
                time.sleep(0.5)
                # Dữ liệu đào tạo giả lập
                X = np.array([30, 50, 70, 90, 110, 150]).reshape(-1, 1) # Diện tích
                y = np.array([1.2, 2.0, 2.9, 3.8, 4.5, 6.0]) # Giá trị (Tỷ VNĐ)
                
                # Khởi tạo và huấn luyện
                model = LinearRegression()
                model.fit(X, y)
                
                # Dự đoán
                pred = model.predict([[area]])[0]
                
                st.metric(label="🏠 Giá nhà mô hình định giá được", value=f"{pred:.2f} Tỷ VNĐ", delta="Dự đoán thành công")
                st.info("💡 **Giải thích:** Thuật toán Linear Regression đã tìm ra một đường thẳng phù hợp nhất đi qua các điểm dữ liệu mẫu để biểu diễn mối tương quan tuyến tính giữa diện tích và giá nhà.")

def page_requests():
    st.title("5. Giao tiếp Mạng: Requests")
    tab1, tab2 = st.tabs(["📖 Báo cáo Lý thuyết", "⚙️ Chương trình Demo"])
    
    with tab1:
        st.markdown("""
        **Requests** là thư viện Python được sử dụng rộng rãi để thực hiện các yêu cầu HTTP (HTTP Requests).
        *   **Vai trò:** Cho phép chương trình Python đóng vai trò như một Client, gửi dữ liệu đi hoặc lấy dữ liệu về từ các API trên Internet.
        *   **Ưu điểm so với `urllib` mặc định:** Cú pháp thân thiện, đơn giản hơn. Tích hợp sẵn bộ giải mã JSON (`response.json()`), tự động thêm các Headers thông dụng.
        """)
        st.code("import requests\n# Gửi GET request đến REST API\nresponse = requests.get('https://api.github.com')\n# Parse dữ liệu JSON\nprint(response.json())", language="python")

    with tab2:
        st.markdown("### 🎯 Demo: Gọi REST API Thực tế")
        st.write("Chương trình sẽ thực hiện HTTP GET Request tới Public API của sàn Coindesk để lấy dữ liệu tỷ giá Bitcoin mới nhất theo thời gian thực.")
        
        if st.button("🚀 Fetch API Tỷ giá Bitcoin", type="primary"):
            with st.spinner("Đang thực hiện Request..."):
                try:
                    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                    data = res.json() # Phân tích JSON
                    
                    price = data['bpi']['USD']['rate']
                    time_updated = data['time']['updated']
                    
                    c1, c2 = st.columns(2)
                    c1.metric(label="💰 Tỷ giá Bitcoin (USD)", value=f"${price}", delta="Dữ liệu Real-time")
                    c2.metric(label="⏱️ Cập nhật lúc", value=time_updated)
                    
                    st.success("HTTP Request trả về Status 200 OK. Đã parse JSON thành công.")
                except Exception as e:
                    st.error("Ngoại lệ xảy ra khi kết nối API. Vui lòng kiểm tra Internet.")

def page_mcp():
    st.title("6. Nghiên cứu: Giao thức MCP")
    tab1, tab2 = st.tabs(["📖 Báo cáo Lý thuyết", "⚙️ Chương trình Demo"])
    
    with tab1:
        st.markdown("""
        **MCP (Model Context Protocol)** là một tiêu chuẩn giao tiếp mã nguồn mở nhằm mục đích kết nối an toàn giữa các mô hình ngôn ngữ lớn (LLM) và các nguồn dữ liệu cục bộ.
        
        *   **Vấn đề giải quyết:** Theo mặc định, LLM bị cô lập và không có quyền truy cập vào hệ thống file hoặc cơ sở dữ liệu của người dùng.
        *   **Cơ chế hoạt động:** MCP thiết lập một kiến trúc Client-Server thông qua giao thức **JSON-RPC**.
            *   `MCP Server` được chạy trên máy người dùng, đóng vai trò cung cấp dữ liệu an toàn.
            *   `MCP Client` (ví dụ: Claude Desktop) sẽ giao tiếp và yêu cầu từ Server.
        *   **Thành phần chính:**
            1. **Resources:** Định nghĩa dữ liệu (File, Database) mà LLM có quyền đọc.
            2. **Tools:** Cung cấp các hàm (Function) để LLM có thể sử dụng (ví dụ: gọi API, truy vấn SQL) thông qua Tool-Calling.
        """)

    with tab2:
        st.markdown("### 🎯 Demo: Mô phỏng Tool-Calling trong MCP")
        st.info("Kịch bản: Người dùng yêu cầu LLM đếm số lượng bản ghi trong cơ sở dữ liệu. LLM sẽ gửi Request gọi hàm qua JSON-RPC thay vì tự động kết nối DB.")
        
        if st.button("🚀 Chạy Mô phỏng Giao tiếp RPC", type="primary"):
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("#### 📤 LLM Request (Client)")
                time.sleep(1)
                st.code('{\n  "method": "tools/call",\n  "params": {\n    "name": "query_db"\n  }\n}', language='json')
                
            with c2:
                st.markdown("#### 📥 MCP Server (Response)")
                time.sleep(1.5)
                st.write("*(Thực thi truy vấn cục bộ và trả kết quả dưới dạng văn bản an toàn)*")
                st.code('{\n  "result": {\n    "content": [\n      {"text": "Count: 1054 Users"}\n    ]\n  }\n}', language='json')
            st.success("✅ Mô phỏng hoàn tất: LLM nhận được thông tin thông qua Server trung gian mà không xâm phạm hệ thống.")

def page_a2a():
    st.title("7. Nghiên cứu: Kiến trúc Multi-Agent (A2A)")
    tab1, tab2 = st.tabs(["📖 Báo cáo Lý thuyết", "⚙️ Chương trình Demo"])
    
    with tab1:
        st.markdown("""
        **Kiến trúc Đa tác nhân (Multi-Agent System / A2A)** là một phương pháp thiết kế phần mềm AI, trong đó nhiều Đặc vụ (Agent) độc lập tương tác với nhau để giải quyết một bài toán phức tạp.
        
        *   **Khái niệm:** Thay vì sử dụng một mô hình LLM duy nhất xử lý toàn bộ Prompt, hệ thống chia nhỏ tác vụ. Mỗi Agent sẽ được gán một **Role** (Vai trò), một **Goal** (Mục tiêu) và các **Tools** (Công cụ) cụ thể để làm việc.
        *   **Đặc điểm nổi bật:**
            *   *Giảm tỷ lệ Hallucination (Ảo giác):* Do mỗi Agent chỉ xử lý một nhiệm vụ hẹp và chuyên biệt.
            *   *Quy trình làm việc (Workflow):* Các Agent có thể hoạt động theo chuỗi (Sequential) hoặc theo phân cấp (Hierarchical - có Quản lý và Nhân viên).
        *   **Framework phổ biến:** LangGraph, CrewAI, AutoGen.
        """)

    with tab2:
        st.markdown("### 🎯 Demo: Mô phỏng Luồng công việc Đa tác nhân")
        st.write("Mô phỏng kiến trúc Phân cấp (Hierarchical): Manager Agent nhận lệnh và phân chia công việc cho Analyst Agent và Designer Agent.")
        
        if st.button("🚀 Khởi chạy Luồng Multi-Agent", type="primary"):
            with st.status("📡 Đang thực thi Workflow...", expanded=True):
                st.write("👤 **Người dùng:** *'Hãy thống kê và vẽ biểu đồ doanh thu.'*")
                time.sleep(1)
                st.write("⚙️ **[Manager Agent]:** Phân tích yêu cầu. Khởi tạo tác vụ cho nhánh Data và nhánh Design.")
                time.sleep(1)
                st.markdown("---")
                st.write("📊 **[Analyst Agent]:** (Thực thi Python Script) -> Tính toán dữ liệu tăng trưởng hoàn tất (+15%).")
                time.sleep(1.5)
                st.write("🎨 **[Designer Agent]:** (Nhận dữ liệu) -> Khởi tạo biểu đồ bằng Matplotlib -> Xuất file báo cáo PDF.")
                time.sleep(1)
                st.markdown("---")
                st.write("⚙️ **[Manager Agent]:** Kiểm duyệt kết quả đầu ra. Trả File báo cáo cuối cùng cho người dùng.")
            st.success("✅ Output: Hệ thống Multi-Agent xử lý thành công yêu cầu phức tạp theo quy trình tự động.")

def main():
    st.sidebar.title("📑 Mục lục Assignment")
    st.sidebar.markdown("---")
    
    pages = {
        "🏠 Trang bìa & Tổng quan": page_home,
        "🔢 1. Thư viện NumPy": page_numpy,
        "🐼 2. Thư viện Pandas": page_pandas,
        "📊 3. Trực quan hóa (Matplotlib)": page_visualization,
        "🧠 4. Học máy (Scikit-Learn)": page_sklearn,
        "🌐 5. Giao tiếp mạng (Requests)": page_requests,
        "🔌 6. Nghiên cứu MCP": page_mcp,
        "🤖 7. Nghiên cứu Multi-Agent": page_a2a
    }
    
    selection = st.sidebar.radio("CHỌN PHẦN BÁO CÁO:", list(pages.keys()), label_visibility="collapsed")
    
    st.sidebar.markdown("---")
    st.sidebar.caption("👨‍🎓 *Sinh viên thực hiện: [Điền tên của bạn]*\n\n📚 *Môn: Program with Python*")
    
    pages[selection]()

if __name__ == "__main__":
    main()
