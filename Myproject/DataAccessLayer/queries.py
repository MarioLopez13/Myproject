from .database_connection import get_connection

def get_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 10 BusinessEntityID, JobTitle FROM HumanResources.Employee")
    results = cursor.fetchall()
    conn.close()
    return results





