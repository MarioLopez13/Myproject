from BusinessLogicLayer.services import fetch_employees_data

def main():
    print("Fetching employee data...")
    employees = fetch_employees_data()
    for emp in employees:
        print(f"ID: {emp['ID']}, Job Title: {emp['JobTitle']}")

if __name__ == "__main__":
    main()


