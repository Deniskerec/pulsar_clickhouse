from clickhouse_driver import Client

def create_database_and_schema():

  # docker clichouse does not have username/pw by default

    clickhouse_host = 'your_clickhouse_host'
    clickhouse_port = '9000'  
    #clickhouse_user = 'your_clickhouse_user'
    #clickhouse_password = 'your_clickhouse_password'

    # Create a Client instance without specifying the database
    client = Client(host=clickhouse_host, 
                    port=clickhouse_port)
                    #user=clickhouse_user, 
                    #password=clickhouse_password)

    client.execute(f"CREATE DATABASE IF NOT EXISTS hafil_dev_afc")


    client = Client(host=clickhouse_host, 
                    port=clickhouse_port, 
                    #user=clickhouse_user, 
                    #password=clickhouse_password, 
                    database='hafil_dev_afc')

    # fact_table: afct_financial_table
    client.execute('''
        CREATE TABLE IF NOT EXISTS afct_financial_table (
            "timestamp" DateTime,
            driver_name String,
            route_destination String,
            route_external_id String,
            route_name String,
            activity_type String,
            route_variant String,
            route_version String,
            stop_code String,
            stop_name String,
            vehicle_ref String,
            cumulative_fare_or_product_price Float32,
            currency_code String,
            device_id String,
            device_transaction_counter UInt32,
            device_type String,
            fare_item_category String,
            fare_item_external_id UInt32,
            fare_item_name String,
            fare_item_type String,
            location_name String,
            location_external_id String,
            operator_ref String,
            operator_type_external_id UInt32,
            vat Float32,  -- calculated field, ensure the logic is applied during data insertion
            operator_type_name String,
            organization_name String,
            paying_rider_type_name String,
            payment_instrument String,
            payment_method String,
            validation_status String,
            trip_id String,
            trip_start_timestamp DateTime,
            terminal_id UInt64,
            fare_item_issued_number String,
            payment_instrument_transaction_id String,
            total_payment_in_cents UInt32,
            file_name String,
            fare_item_product_type String,
            booking_reference String,
            e_ticket_reference String,
            reservation_seat String
        ) ENGINE = MergeTree() ORDER BY (fare_item_issued_number, "timestamp");
    ''')

    # dimension_table: afct_ticket_record
    client.execute('''
        CREATE TABLE IF NOT EXISTS afct_ticket_record (
            id UInt32,
            transaction_id UInt32,
            issued_alighting_stop_code String,
            issued_boarding_stop_code String
        ) ENGINE = MergeTree() ORDER BY id;
    ''')

    # dimension_table: afc_stop
    client.execute('''
        CREATE TABLE IF NOT EXISTS afc_stop (
            stop_name String,
            stop_code String,
            is_active UInt8
        ) ENGINE = MergeTree() ORDER BY stop_code;
    ''')

    # dimension_table: afc_booking_( worst logic i have ever seen)
    client.execute('''
        CREATE TABLE IF NOT EXISTS afc_booking (
            fare_item_issued_number String,
            reference String,
            e_ticket_reference String,
            first_name String,
            middle_name String,
            last_name String,
            document_reference String,
            document_type String,
            date_of_birth Date,
            email_address String,
            phone_number String,
            country_code String
        ) ENGINE = MergeTree() ORDER BY fare_item_issued_number;
    ''')

    print("Schema creation completed.")

if __name__ == "__main__":
    create_schema()
