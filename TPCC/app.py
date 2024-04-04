import mysql.connector
from flask import Flask, render_template, request
from datetime import datetime
import time


app = Flask(__name__)


def get_db_connection():
    host = '31.220.63.125'
    database = 'mydb'
    user = 'user'
    password = 'Barbecue-Unexpired-Swarm7'

    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    return connection


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def calculate():
    start_time = time.time()
    warehouse = int(request.form["warehouse"])
    district = int(request.form["district"])
    customer = int(request.form["customer"])
    ol_i_id_list = request.form.getlist('ol_i_id[]')
    ol_supply_w_id = request.form.getlist('ol_supply_w_id[]')
    ol_quantity = request.form.getlist('ol_quantity[]')
    ol_cnt = len(ol_i_id_list)

    connection = get_db_connection()
    cursor = connection.cursor()

    qty = []
    item_names = []
    item_prices = []
    stock_list = []
    brand_list = []
    try:
        # start a transaction
        connection.autocommit = False
        cursor.execute("START TRANSACTION")

        # retrieve W_TAX from the WAREHOUSE table
        cursor.execute(
            "SELECT W_TAX FROM WAREHOUSE WHERE W_ID = %s FOR UPDATE", (warehouse,))
        w_tax = cursor.fetchone()[0]

        # retrieve D_TAX, D_NEXT_O_ID, C_DISCOUNT, C_LAST, and C_CREDIT from the DISTRICT and CUSTOMER tables
        cursor.execute(
            "SELECT D_TAX, D_NEXT_O_ID, C_DISCOUNT, C_LAST, C_CREDIT FROM DISTRICT, CUSTOMER WHERE D_ID = %s AND D_W_ID = %s AND C_W_ID = %s AND C_D_ID = %s AND C_ID = %s FOR UPDATE",
            (district, warehouse, warehouse, district, customer,))
        row = cursor.fetchone()
        d_tax = row[0]
        d_next_o_id = row[1]
        c_discount = row[2]
        c_last = row[3]
        c_credit = row[4]

        # retrieve the current system date and time using the MySQL NOW() function
        cursor.execute("SELECT NOW()")
        order_date = cursor.fetchone()[0]

        # insert a new row into the NEW-ORDER table to reflect the creation of the new order
        # cursor.execute("INSERT INTO NEW_ORDER (NO_O_ID, NO_D_ID, NO_W_ID) VALUES (%s, %s, %s)",
        #               (d_next_o_id, district, warehouse,))

        # insert a new row into the ORDER table to reflect the creation of the new order
        if all(int(w_id) == warehouse for w_id in ol_supply_w_id):
            o_all_local = 1
        else:
            o_all_local = 0
        cursor.execute("SELECT MAX(O_ID) FROM `ORDER`;")
        o_id_next = cursor.fetchone()[0]
        o_id_next += 1

        cursor.execute("INSERT INTO `ORDER` (O_ID, O_D_ID, O_W_ID, O_C_ID, O_ENTRY_D, O_CARRIER_ID, O_OL_CNT, O_ALL_LOCAL) VALUES (%s, %s, %s, %s, %s,%s, %s, %s)",
                       (o_id_next, district, warehouse, customer, order_date, 1, ol_cnt, o_all_local,))

        d_next_o_id += 1
        # compute O_OL_CNT to match ol_cnt
        o_ol_cnt = ol_cnt

        # process each item on the order
        ol_amount = 0
        execution_status = "New Order Transaction Executed Successfully"
        for i in range(ol_cnt):
            ol_i_id = int(ol_i_id_list[i])
            ol_supply_w_id_i = int(ol_supply_w_id[i])
            ol_quantity_i = int(ol_quantity[i])

            # retrieve I_PRICE, I_NAME, and I_DATA from the ITEM table
            cursor.execute(
                "SELECT I_PRICE, I_NAME, I_DATA FROM ITEM WHERE I_ID = %s", (ol_i_id,))
            row = cursor.fetchone()
            if not row:
                raise Exception("not-found")
            i_price = row[0]
            i_name = row[1]
            i_data = row[2]
            item_prices.append(i_price)
            item_names.append(i_name)

            # format district as a zero-padded 2-digit integer
            district_formatted = '{:02d}'.format(district)
            # add formatted district to column name
            s_dist_col = 'S_DIST_{}'.format(district_formatted)
            cursor.execute(
                "SELECT S_QUANTITY, S_DIST_0%s FROM STOCK WHERE S_I_ID = %s AND S_W_ID = %s",
                (district, ol_i_id, 1))
            # (district, ol_i_id, ol_supply_w_id_i))

            s_quantity, s_dist_xx = cursor.fetchone()

            qty.append(int(s_quantity))

            stock_list.append(s_quantity)

            # decrement stock quantity
            if s_quantity >= ol_quantity_i + 10:
                s_quantity -= ol_quantity_i
            else:
                s_quantity = s_quantity - ol_quantity_i + 91

            # update stock information
            cursor.execute("UPDATE STOCK SET S_QUANTITY = %s, S_YTD = S_YTD + %s, S_ORDER_CNT = S_ORDER_CNT + 1, S_REMOTE_CNT = S_REMOTE_CNT + %s WHERE S_I_ID = %s AND S_W_ID = %s",
                           (qty[i], ol_quantity_i, 1 if ol_supply_w_id_i != warehouse else 0, ol_i_id, ol_supply_w_id_i))

            # compute order line amount
            ol_amount = ol_quantity_i * i_price

            # determine brand-generic field
            bg = 'B' if 'ORIGINAL' in i_data else 'G'
            brand_list.append(bg)
            # insert new row into ORDER_LINE table

            cursor.execute("SELECT MAX(OL_O_ID) FROM `ORDER_LINE`;")
            ol_id_next = cursor.fetchone()[0]
            ol_id_next += 1

            cursor.execute("INSERT INTO ORDER_LINE (OL_O_ID, OL_D_ID, OL_W_ID, OL_NUMBER, OL_I_ID, OL_SUPPLY_W_ID, OL_DELIVERY_D, OL_QUANTITY, OL_AMOUNT, OL_DIST_INFO) VALUES (%s, %s, %s, %s, %s, %s, NULL, %s, %s, %s)",
                           (ol_id_next, district, warehouse, i + 1, 1, 1, ol_quantity_i, 1, s_dist_xx))
            #               (d_next_o_id, district, warehouse, i + 1, ol_i_id, ol_supply_w_id_i, ol_quantity_i, 1, s_dist_xx))

        # compute the total-amount for the complete order
        query = "SELECT SUM(OL_AMOUNT * (1 - %s) * (1 + %s + %s)) " "FROM ORDER_LINE WHERE OL_W_ID = %s AND OL_D_ID = %s AND OL_O_ID = %s"
        cursor.execute(query, (1, 1,
                       d_tax, warehouse, district, d_next_o_id))

        total_amount = cursor.fetchone()[0]
        cursor.execute("SELECT MAX(O_ID) FROM `ORDER`")
        order_number = d_next_o_id
        # commit the transaction

        cursor.execute("COMMIT;")

        cursor.close()
        connection.close()

    except Exception as e:
        # rollback the transaction
        execution_status = "New Order Transaction Failed"
        connection.rollback()
        # close the database connection
        connection.close()
        # redirect the user to the input page with an error message
        return render_template("index.html", error=str(e))

    rows = [[ol_i_id, ol_supply_w_id, ol_quantity] for ol_i_id,
            ol_supply_w_id, ol_quantity in zip(ol_i_id_list, ol_supply_w_id, ol_quantity)]
    number_of_lines = len(rows)

    table_headers = ['supp_w', 'item_id', 'item_name',
                     'qty', 'stock', 'Brand/Generic', 'price', 'amount']
    table_rows = []
    i = 0
    for row in rows:
        amount = float(stock_list[i]) * float(item_prices[i])
        amount = round(amount, 2)  # Round to 2 decimal places
        table_rows.append([row[1], row[0], item_names[i], row[2], stock_list[i], brand_list[i],
                          item_prices[i], amount])
        i += 1

    total = 0
    for row in table_rows:
        total += row[7]

    end_time = time.time()
    execution_time = end_time - start_time
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('result.html', order_number=order_number, ol_cnt=ol_cnt, item_names=item_names, item_prices=item_prices, number_of_lines=number_of_lines, district_tax=d_tax, warehouse_tax=w_tax, discount=c_discount, customer_credit=c_credit, names=ol_i_id_list, rows1=rows, warehouse=warehouse, district=district, customer=customer, date=date, customer_name=c_last, headers=table_headers, rows=table_rows, execution_status=execution_status, total=total, processing_time=execution_time)


if __name__ == "__main__":
    app.run(debug=True)
