# Data Dictionary — sales_2025.csv

| Column | Meaning |
|---|---|
| order_id | Mã đơn hàng |
| order_date | Ngày đặt hàng |
| product_id | Mã sản phẩm |
| product_name | Tên sản phẩm |
| category | Danh mục |
| brand | Thương hiệu |
| customer_id | Mã khách hàng |
| customer_name | Tên khách hàng |
| city | Thành phố |
| quantity | Số lượng |
| unit_price | Giá niêm yết |
| discount | Tỷ lệ giảm giá |
| revenue | Doanh thu sau giảm giá |
| cost | Giá vốn mô phỏng |
| channel | Kênh bán hàng |
| payment_method | Phương thức thanh toán |

## Derived metrics

`profit = revenue - cost`

`profit_margin = profit / revenue`
