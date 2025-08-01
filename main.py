import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('CCI Estate for Opendata.db')

# Create a cursor object
cursor = conn.cursor()

# Create the table
create_table_query = '''
CREATE TABLE IF NOT EXISTS ConstituentEstates (
    c_estate TEXT NOT NULL,               -- Estate Name (Chinese)
    e_estate TEXT NOT NULL,               -- Estate Name (English)
    pc_addr TEXT NOT NULL,                -- Estate Address (English)
    scp_mktc TEXT NOT NULL,               -- Region of Hong Kong (Chinese)
    scp_mkte TEXT NOT NULL,               -- Region of Hong Kong (English)
    ml_opk INTEGER NOT NULL,               -- Latest Occupation Permit Year
    max_update INTEGER NOT NULL,          -- Latest Occupation Permit Year
    blgcount INTEGER NOT NULL,            -- Number of Blocks
    pc_dev TEXT NOT NULL,                 -- Developer Name (Chinese)
    e_dev TEXT NOT NULL,                  -- Developer Name (English)
    facilities_c TEXT,                    -- Facilities (Chinese)
    facilities_e TEXT,                    -- Facilities (English)
    facilities_e_kown TEXT,               -- Facilities (Existing)
    url TEXT NOT NULL                     -- Estate Transaction URL
);
'''

# Execute the create table query
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")