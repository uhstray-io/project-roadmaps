# Create the local Sqlite database and define the initial data, credentials and schema

# Import Libraries and Connect to the Database
import sqlite3
connection = sqlite3.connect("project-roadmaps.db")

# Table Schema Definitions for the Application
class table_schemas:
    roadmaps = """
    CREATE TABLE IF NOT EXISTS roadmaps (
        name text, 
        description text, 
        project_status text,
        releases table,
        versions table,
        features table
    );
    """

    releases = """
    CREATE TABLE IF NOT EXISTS releases (
        release_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        release_number float, 
        project_owner text,
        project_maintainers text,
        project_contributors text, 
        release_start datetime(YYYY-MM-DD),
        release_end datetime(YYYY-MM-DD),
        release_status text
    );
    """

    versions = """
    CREATE TABLE IF NOT EXISTS versions (
        version_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        version_number float, 
        version_start datetime(YYYY-MM-DD),
        version_end datetime(YYYY-MM-DD),
        version_status text
    );
    """

    features = """
    CREATE TABLE features (
        feature_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        feature_name text NOT NULL, 
        feature_description varchar(2048), 
        feature_status text
    );
    """

def initalize_tables():
    # If the table does not exist, create it
    cur = connection.cursor()
    if cur.execute(table_schemas.roadmaps):
        print("Roadmaps table created")

    if cur.execute(table_schemas.releases):
        print("Releases table created")

    if cur.execute(table_schemas.versions):
        print("Versions table created")

    if cur.execute(table_schemas.features):
        print("Features table created")

    cur.close()
    connection.commit()
    


# Test the Database by Inserting Test Data
def test_database():
    
    cur = connection.cursor()
    
    # Insert test data into the tables
    cur.execute("INSERT INTO roadmaps VALUES ('Project A', 'Project A Description', 'In Progress', '1', '1', '1')")
    cur.execute("INSERT INTO releases VALUES (1, 1.0, 'John Doe', 'Jane Doe', 'John Smith', '2022-01-01', '2022-01-31', 'In Progress')")
    cur.execute("INSERT INTO versions VALUES (1, 1.0, '2022-01-01', '2022-01-31', 'In Progress')")
    cur.execute("INSERT INTO features VALUES (1, 'Feature 1', 'Feature 1 Description', 'In Progress')")

    # Query the database to test the data
    test_query = """
    SELECT * FROM 
    roadmaps , 
    R.release_number, 
    R.project_owner, 
    R.project_maintainers, 
    R.project_contributors, 
    R.release_start, 
    R.release_end, 
    R.release_status, 
    V.version_number, 
    V.version_start, 
    V.version_end, 
    V.version_status, 
    F.feature_name, 
    F.feature_description, 
    F.feature_status
    JOIN (SELECT * FROM releases) as R ON roadmaps.releases = R.release_id
    JOIN (SELECT * FROM versions) as V ON roadmaps.versions = V.version_id
    JOIN (SELECT * FROM features) as F ON roadmaps.features = F.feature_id
    ORDER BY versions.version_number DESC;
    """

    cur.execute(test_query)
    test_results = cur.fetchall()
    print(test_results)
    cur.close()

def main():
    initalize_tables()
    test_database()
    connection.close()

main()




    
