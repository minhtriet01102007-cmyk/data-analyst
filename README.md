# Data Analyst Portfolio

## 1. Bối cảnh
Giả sử tôi là Data Analyst cho một doanh nghiệp bán lẻ thiết bị công nghệ. Công ty có dữ liệu đơn hàng trong năm 2025 và muốn biết:
- Doanh thu và lợi nhuận biến động như thế nào theo thời gian?
- Sản phẩm nào bán tốt?
- Kênh bán hàng nào hiệu quả?
- Khu vực nào đóng góp nhiều doanh thu?
- Danh mục nào có biên lợi nhuận tốt?
Dataset trong project là **dữ liệu mô phỏng** để phục vụ portfolio.
## 2. Tech stack
- SQL / PostgreSQL
- Python
- Pandas
- Matplotlib
- Excel
- Power BI (khuyến nghị dựng dashboard từ các file trong `data/processed`)
- Git & GitHub
## 3. Cấu trúc project
```text
tran-minh-triet-data-analyst/
├── data/
│   ├── raw/
│   │   └── sales_2025.csv
│   └── processed/
├── notebooks/
│   └── 01_sales_analysis.ipynb
├── src/
│   └── analyze_sales.py
├── sql/
│   ├── 01_schema.sql
│   └── 02_business_questions.sql
├── reports/
├── docs/
├── requirements.txt
└── README.md
```
## 4. Cách chạy
```bash
python -m venv .venv
```
Windows:
```bash
.venv\Scripts\activate
```
Cài thư viện:
```bash
pip install -r requirements.txt
```
Chạy phân tích:
```bash
python src/analyze_sales.py
```
Hoặc mở notebook:
```bash
jupyter notebook
```
## 5. Deliverables
Sau khi chạy script:
- `data/processed/kpi.csv`
- `data/processed/monthly_performance.csv`
- `data/processed/product_performance.csv`
- `data/processed/channel_performance.csv`
- `data/processed/city_performance.csv`
- `reports/monthly_revenue.png`
- `reports/top_products.png`
## 6. Dashboard Power BI
Nên tự xây một dashboard 1 trang với 4 KPI:
- Total Revenue
- Total Profit
- Orders
- Profit Margin
Biểu đồ:
1. Revenue by Month
2. Revenue by Category
3. Top 10 Products
4. Revenue by City
5. Revenue by Channel
Thêm slicer: `Year`, `Category`, `Channel`, `City`.
## 7. Kỹ năng thể hiện
Project này nhằm chứng minh khả năng:
- Làm sạch và kiểm tra dữ liệu
- SQL aggregation và GROUP BY
- Phân tích KPI
- Phân tích xu hướng
- Phân tích sản phẩm/kênh/khu vực
- Trực quan hóa dữ liệu
- Viết README và tổ chức GitHub repository
- Chuyển câu hỏi kinh doanh thành câu hỏi dữ liệu
## 8. Hướng phát triển
Nếu muốn nâng project lên mức ứng tuyển internship/junior:
- Thêm dữ liệu 2024 để YoY analysis
- Thêm bảng `customers`, `products`, `orders` theo mô hình star schema
- Viết thêm 15–20 business questions bằng SQL
- Làm dashboard Power BI hoàn chỉnh
- Viết một `data_dictionary.md`
- Viết phần Business Insights và Recommendations bằng lập luận của chính mình
---


Data Analyst Portfolio — 2026
