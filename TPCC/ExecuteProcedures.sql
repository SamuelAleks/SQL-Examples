use tpcc;

CALL generate_item_rows();
select * from `ITEM`;

CALL generate_warehouse_rows();
select * from `WAREHOUSE`;

CALL generate_district_rows();
select * from `DISTRICT`;

CALL generate_customer_rows();
select * from `CUSTOMER`;

CALL generate_history_rows();
select * from `HISTORY`;

CALL generate_order_rows();
select * from `ORDER_DB`;

CALL generate_new_order_rows();
select * from `NEW_ORDER`;

CALL generate_stock_rows();
select * from `STOCK`;

CALL generate_order_line_rows();
select * from `ORDER_LINE`;


