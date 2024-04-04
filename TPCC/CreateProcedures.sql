use tpcc;


DELIMITER //
CREATE PROCEDURE generate_warehouse_rows()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 2 DO
        INSERT INTO `tpcc`.`WAREHOUSE` (`W_ID`, `W_NAME`, `W_STREET_1`, `W_STREET_2`, `W_CITY`, `W_STATE`, `W_ZIP`, `W_TAX`, `W_YTD`)
        VALUES (i, CONCAT('Warehouse ', i), CONCAT('Street ', i), CONCAT('Street ', i+1), CONCAT('City ', i), 'IL', '123456789', 0.05, 3000.00);
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE generate_district_rows()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 20 DO
        INSERT INTO `tpcc`.`DISTRICT` (`D_ID`, `D_W_ID`, `D_NAME`, `D_STREET_1`, `D_STREET_2`, `D_CITY`, `D_STATE`, `D_ZIP`, `D_TAX`, `D_YTD`, `D_NEXT_O_ID`)
        VALUES (i, i, CONCAT('District ', i), CONCAT('Street ', i), CONCAT('Street ', i+1), CONCAT('City ', i), 'IL', '123456789', 0.05, 3000.00, i);
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE generate_customer_rows()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 60000 DO
        INSERT INTO `tpcc`.`CUSTOMER` (`C_ID`, `C_D_ID`, `C_W_ID`, `C_FIRST`, `C_MIDDLE`, `C_LAST`, `C_STREET_1`, `C_STREET_2`, `C_CITY`, `C_STATE`, `C_ZIP`, `C_PHONE`, `C_SINCE`, `C_CREDIT`, `C_CREDIT_LIM`, `C_DISCOUNT`, `C_BALANCE`, `C_YTD_PAYMENT`, `C_PAYMENT_CNT`, `C_DELIVERY_CNT`, `C_DATA`)
        VALUES (i, i, i, CONCAT('First', i), 'OE', CONCAT('Last', i), CONCAT('Street ', i), CONCAT('Street ', i+1), CONCAT('City ', i), 'IL', '123456789', '1234567890123456', NOW(), 'GC', 50000.00, 0.05, 10.00, 10.00, 1, 0, CONCAT('Data ', i));
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE generate_history_rows()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 60000 DO
        INSERT INTO `tpcc`.`HISTORY` (`H_C_ID`, `H_C_D_ID`, `H_C_W_ID`, `H_D_ID`, `H_W_ID`, `H_DATE`, `H_AMOUNT`, `H_DATA`)
        VALUES (i, i, i, i, i, NOW(), 10.00, CONCAT('Data ', i));
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE generate_item_rows()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 100000 DO
        INSERT INTO `tpcc`.`ITEM` (`I_ID`, `I_IM_ID`, `I_NAME`, `I_PRICE`, `I_DATA`)
        VALUES (i, i, CONCAT('Item ', i), 10.00, CONCAT('Data ', i));
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE generate_order_rows()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 60000 DO
        INSERT INTO `tpcc`.`ORDER_DB` (`O_ID`, `O_D_ID`, `O_W_ID`, `O_C_ID`, `O_ENTRY_D`, `O_CARRIER_ID`, `O_OL_CNT`, `O_ALL_LOCAL`)
        VALUES (i, i, i, i, NOW(), i, 5, 1);
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE generate_new_order_rows()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 18000 DO
        INSERT INTO `tpcc`.`NEW_ORDER` (`NO_O_ID`, `NO_D_ID`, `NO_W_ID`)
        VALUES (i, i, i);
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE generate_stock_rows()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 200000 DO
        INSERT INTO `tpcc`.`STOCK` (`S_I_ID`, `S_W_ID`, `S_QUANTITY`, `S_DIST_01`, `S_DIST_02`, `S_DIST_03`, `S_DIST_04`, `S_DIST_05`, `S_DIST_06`, `S_DIST_07`, `S_DIST_08`, `S_DIST_09`, `S_DIST_10`, `S_YTD`, `S_ORDER_CNT`, `S_REMOTE_CNT`, `S_DATA`)
        VALUES (i, i, 100, CONCAT('Dist01_', i), CONCAT('Dist02_', i), CONCAT('Dist03_', i), CONCAT('Dist04_', i), CONCAT('Dist05_', i), CONCAT('Dist06_', i), CONCAT('Dist07_', i), CONCAT('Dist08_', i), CONCAT('Dist09_', i), CONCAT('Dist10_', i), 0, 0, 0, CONCAT('Data ', i));
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE generate_order_line_rows()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 600000 DO
        INSERT INTO `tpcc`.`ORDER_LINE` (`OL_O_ID`, `OL_D_ID`, `OL_W_ID`, `OL_NUMBER`, `OL_I_ID`, `OL_SUPPLY_W_ID`, `OL_DELIVERY_D`, `OL_QUANTITY`, `OL_AMOUNT`, `OL_DIST_INFO`)
        VALUES (i, i, i, i, i, i, NOW(), 5, 10.00, CONCAT('DistInfo_', i));
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;
