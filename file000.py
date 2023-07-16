CREATE OR REPLACE PROCEDURE extract_data_to_csv (
    p_table_name    IN VARCHAR2,
    p_report_date   IN VARCHAR2,
    p_output_file   IN VARCHAR2
) AS
    l_cursor_id         INTEGER;
    l_column_count      INTEGER;
    l_column_desc       DBMS_SQL.DESC_TAB2;
    l_csv_file          UTL_FILE.FILE_TYPE;
    l_output_dir        VARCHAR2(100) := 'YOUR_OUTPUT_DIRECTORY';
    l_csv_file_name     VARCHAR2(100);
    l_csv_row           VARCHAR2(32767);
    l_col_value         VARCHAR2(4000);
    l_column_separator  CONSTANT VARCHAR2(1) := ',';
BEGIN
    -- Generate the CSV file name based on the input parameters
    l_csv_file_name := p_table_name || '_' || p_report_date || '.csv';

    -- Open the CSV file for writing
    l_csv_file := UTL_FILE.FOPEN(l_output_dir, l_csv_file_name, 'w', 32767);

    -- Create a dynamic cursor using DBMS_SQL
    l_cursor_id := DBMS_SQL.OPEN_CURSOR;

    -- Parse the SQL statement to select all columns from the specified table
    DBMS_SQL.PARSE(l_cursor_id, 'SELECT * FROM ' || p_table_name, DBMS_SQL.NATIVE);

    -- Define the column count
    l_column_count := DBMS_SQL.EXECUTE(l_cursor_id);

    -- Describe the columns of the result set
    FOR i IN 1..l_column_count LOOP
        DBMS_SQL.DESCRIBE_COLUMNS2(l_cursor_id, i, l_column_desc(i));
    END LOOP;

    -- Fetch and write the column headers to the CSV file
    FOR i IN 1..l_column_count LOOP
        l_csv_row := l_csv_row || l_column_desc(i).col_name || l_column_separator;
    END LOOP;
    UTL_FILE.PUT_LINE(l_csv_file, RTRIM(l_csv_row, l_column_separator));

    -- Fetch and write the data rows to the CSV file
    WHILE DBMS_SQL.FETCH_ROWS(l_cursor_id) > 0 LOOP
        l_csv_row := '';

        FOR i IN 1..l_column_count LOOP
            -- Fetch the column value
            DBMS_SQL.COLUMN_VALUE(l_cursor_id, i, l_col_value);
            l_csv_row := l_csv_row || l_col_value || l_column_separator;
        END LOOP;

        -- Write the row to the CSV file
        UTL_FILE.PUT_LINE(l_csv_file, RTRIM(l_csv_row, l_column_separator));
    END LOOP;

    -- Close the cursor
    DBMS_SQL.CLOSE_CURSOR(l_cursor_id);

    -- Close the CSV file
    UTL_FILE.FCLOSE(l_csv_file);

EXCEPTION
    WHEN OTHERS THEN
        -- Close the cursor if an exception occurs
        IF DBMS_SQL.IS_OPEN(l_cursor_id) THEN
            DBMS_SQL.CLOSE_CURSOR(l_cursor_id);
        END IF;

        -- Close the CSV file if an exception occurs
        IF UTL_FILE.IS_OPEN(l_csv_file) THEN
            UTL_FILE.FCLOSE(l_csv_file);
        END IF;

        -- Propagate the exception
        RAISE;
END;
/