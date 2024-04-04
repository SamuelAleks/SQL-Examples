import mysql.connector
import random
import string
import datetime
# Connect to the MySQL server
mydb = mysql.connector.connect(
    host="31.220.63.125",
    user="user",
    password="Barbecue-Unexpired-Swarm7",
    database="mydb"
)

# Define the cursor
mycursor = mydb.cursor()
# Generate and insert data into WAREHOUSE table

WAREHOUSE_COUNT = 2

mycursor.execute("SELECT COUNT(*) FROM WAREHOUSE")
result = mycursor.fetchone()
if result[0] == 0:
    # Generate and insert data into WAREHOUSE table
    mycursor.execute("SET GLOBAL max_allowed_packet=2048*1024*1024;")
    WAREHOUSE_COUNT = 2
    for i in range(1, WAREHOUSE_COUNT+1):
        w_id = i
        w_name = ''.join(random.choices(string.ascii_uppercase, k=10))
        w_street_1 = ''.join(random.choices(string.ascii_uppercase, k=20))
        w_city = ''.join(random.choices(string.ascii_uppercase, k=20))
        w_state = ''.join(random.choices(string.ascii_uppercase, k=2))
        w_zip = ''.join(random.choices(string.digits, k=9))
        w_tax = round(random.uniform(0.0001, 0.9999), 4)
        w_ytd = round(random.uniform(100000.00, 1000000.00), 2)

        sql = "INSERT INTO WAREHOUSE (W_ID, W_NAME, W_STREET_1, W_CITY, W_STATE, W_ZIP, W_TAX, W_YTD) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (w_id, w_name, w_street_1, w_city, w_state, w_zip, w_tax, w_ytd)
        mycursor.execute(sql, val)

    mydb.commit()
    print("Warehouse DONE")
else:
    print("Warehouse table is not empty, skipping insert")


# Generate and insert data into ITEM table
# Check if the ITEM table is empty
sql = "SELECT COUNT(*) FROM ITEM"
mycursor.execute(sql)
result = mycursor.fetchone()

if result[0] == 0:
    # Generate and insert data into ITEM table
    values = []
    for i in range(1, 100001):
        i_id = i
        i_im_id = random.randint(1, 100)
        i_name = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=24))
        i_price = round(random.uniform(1.00, 100.00), 2)
        i_data = ''.join(random.choices([
            'ORIGINAL', 'GENERIC']))

        values.append((i_id, i_im_id, i_name, i_price, i_data))
        print("Item Iteration: ", i)

    sql = "INSERT INTO ITEM (I_ID, I_IM_ID, I_NAME, I_PRICE, I_DATA) VALUES (%s, %s, %s, %s, %s)"
    mycursor.executemany(sql, values)

    mydb.commit()
    print("Item DONE")
else:
    print("ITEM table is not empty")


# Check if the STOCK table is empty
mycursor.execute("SELECT COUNT(*) FROM STOCK")
result = mycursor.fetchone()
count = result[0]

# If the table is empty, execute the INSERT statement
if count == 0:
    sql = "INSERT INTO STOCK (S_I_ID, S_W_ID, S_QUANTITY, S_DIST_01, S_DIST_02, S_DIST_03, S_DIST_04, S_DIST_05, S_DIST_06, S_DIST_07, S_DIST_08, S_DIST_09, S_DIST_10, S_YTD, S_ORDER_CNT, S_REMOTE_CNT, S_DATA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = []
    for j in range(1, WAREHOUSE_COUNT+1):
        for i in range(1, 100001):
            # Generate random values for the columns
            s_i_id = i
            s_w_id = j
            s_quantity = random.randint(0, 100)
            s_dist_01 = ''.join(random.choices(
                string.ascii_letters + string.digits, k=24))
            s_dist_02 = ''.join(random.choices(
                string.ascii_letters + string.digits, k=24))
            s_dist_03 = ''.join(random.choices(
                string.ascii_letters + string.digits, k=24))
            s_dist_04 = ''.join(random.choices(
                string.ascii_letters + string.digits, k=24))
            s_dist_05 = ''.join(random.choices(
                string.ascii_letters + string.digits, k=24))
            s_dist_06 = ''.join(random.choices(
                string.ascii_letters + string.digits, k=24))
            s_dist_07 = ''.join(random.choices(
                string.ascii_letters + string.digits, k=24))
            s_dist_08 = ''.join(random.choices(
                string.ascii_letters + string.digits, k=24))
            s_dist_09 = ''.join(random.choices(
                string.ascii_letters + string.digits, k=24))
            s_dist_10 = random.randint(0, 100)
            s_ytd = random.randint(0, 1000000)
            s_order_cnt = 0
            s_remote_cnt = 0
            s_data = ''.join(random.choices(
                string.ascii_letters + string.digits, k=50))

            values.append((s_i_id, s_w_id, s_quantity, s_dist_01, s_dist_02, s_dist_03, s_dist_04, s_dist_05,
                           s_dist_06, s_dist_07, s_dist_08, s_dist_09, s_dist_10, s_ytd, s_order_cnt, s_remote_cnt, s_data))

            if len(values) == 25000:
                mycursor.executemany(sql, values)
                mydb.commit()
                values = []

            print("Stock Iteration: ", j, i)

    if values:
        mycursor.executemany(sql, values)
        mydb.commit()
    print("Stock DONE")
else:
    print("Stock table already has data.")


# Check if DISTRICT table is empty
cursor = mydb.cursor()
cursor.execute("SELECT COUNT(*) FROM DISTRICT")
result = cursor.fetchone()[0]

if result == 0:
    # Generate 10*W rows for DISTRICT
    data = []
    for j in range(1, WAREHOUSE_COUNT + 1):
        for i in range(1, 11):
            d_id = i
            d_w_id = j
            d_name = ''.join(random.choice(string.ascii_lowercase)
                             for i in range(40))
            d_street_1 = ''.join(random.choice(string.ascii_lowercase)
                                 for i in range(40))
            d_street_2 = ''.join(random.choice(string.ascii_lowercase)
                                 for i in range(40))
            d_city = ''.join(random.choice(string.ascii_lowercase)
                             for i in range(40))
            d_state = ''.join(random.choice(string.ascii_uppercase)
                              for i in range(2))
            d_zip = ''.join(random.choice(string.digits) for i in range(9))
            d_tax = random.uniform(0, 0.2)
            d_ytd = random.uniform(0, 1000000)
            d_next_o_id = 3001
            data.append((d_id, d_w_id, d_name, d_street_1, d_street_2,
                         d_city, d_state, d_zip, d_tax, d_ytd, d_next_o_id))
            print("Item Iteration: ", i)

    # Insert the rows in bulk
    cursor = mydb.cursor()
    sql = "INSERT INTO DISTRICT (D_ID, D_W_ID, D_NAME, D_STREET_1, D_STREET_2, D_CITY, D_STATE, D_ZIP, D_TAX, D_YTD, D_NEXT_O_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(sql, data)
    mydb.commit()

    print("District DONE")
else:
    print("DISTRICT table is not empty, skipping insert")


# Define function to generate random strings
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


mycursor = mydb.cursor()

values = []
# Check if CUSTOMER table is empty
mycursor.execute("SELECT COUNT(*) FROM CUSTOMER")
count = mycursor.fetchone()[0]

if count == 0:
    values = []
    sql = "INSERT INTO CUSTOMER (C_ID, C_D_ID, C_W_ID, C_FIRST, C_MIDDLE, C_LAST, C_STREET_1, C_STREET_2, C_CITY, C_STATE, C_ZIP, C_PHONE, C_SINCE, C_CREDIT, C_CREDIT_LIM, C_DISCOUNT, C_BALANCE, C_YTD_PAYMENT, C_PAYMENT_CNT, C_DELIVERY_CNT, C_DATA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    start_date = datetime.date(1995, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    for w in range(1, WAREHOUSE_COUNT+1):
        for d in range(1, 11):
            for i in range(1, 30001):
                c_id = i
                c_d_id = d
                c_w_id = w
                c_first = ''.join(random.choices(string.ascii_uppercase, k=10))
                c_middle = ''.join(random.choices(string.ascii_uppercase, k=2))
                c_last = ''.join(random.choices(string.ascii_uppercase, k=10))
                c_street_1 = ''.join(random.choices(
                    string.ascii_uppercase, k=20))
                c_street_2 = ''.join(random.choices(
                    string.ascii_uppercase, k=20))
                c_city = ''.join(random.choices(string.ascii_uppercase, k=10))
                c_state = ''.join(random.choices(string.ascii_uppercase, k=2))
                c_zip = ''.join(random.choices(string.digits, k=9))
                c_phone = ''.join(random.choice(string.digits)
                                  for i in range(10))
                c_since = start_date + \
                    datetime.timedelta(days=random.randint(
                        0, (end_date - start_date).days))
                c_credit = random.choice(['GC', 'BC'])
                c_credit_lim = round(random.uniform(100000.00, 1000000.00), 2)
                c_discount = round(random.uniform(0, .9999), 4)
                c_balance = round(random.uniform(100000.00, 1000000.00), 2)
                c_ytd_payment = round(random.uniform(100000.00, 1000000.00), 2)
                c_payment_cnt = 100
                c_delivery_cnt = 100
                c_data = ''.join(random.choices(string.ascii_uppercase, k=50))

                values.append((c_id, c_d_id, c_w_id, c_first, c_middle, c_last, c_street_1, c_street_2, c_city, c_state, c_zip, c_phone,
                               c_since, c_credit, c_credit_lim, c_discount, c_balance, c_ytd_payment, c_payment_cnt, c_delivery_cnt, c_data))
                print("Customer Iteration: ", i)

                if len(values) == 25000:
                    mycursor.executemany(sql, values)
                    mydb.commit()
                    values = []

                print("Customer Iteration: ", w, d)

    if values:
        mycursor.executemany(sql, values)
        mydb.commit()

    print("Customer DONE - Table was empty")
else:
    print("Customer Table already has rows")
