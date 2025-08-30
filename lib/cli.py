# lib/cli.py

from lib.helpers import exit_program, helper_1
from models import SessionLocal
from check_fraud import FraudPattern, User


def menu():
    print("\n--- Fraud check CLI ---")
    print("1. Run Fraud check")
    print("2. Add Fraud pattern")
    print("3. List Fraud patterns")
    print("4. Add User")
    print("5. Exit")
    
def add_pattern():
    models = SessionLocal()
    patterns = input("Enter regex fraud pattern: ")
    desc = input("Enter description: ")
    alert_type = input("Enter alert type: ")
    fp = FraudPattern(alert_type=alert_type, description=desc)
    models.add(fp)
    models.commit()
    print("Fraud pattern added.")
    models.close()


def list_patterns():
    models = SessionLocal()
    patterns = models.query(FraudPattern).all()
    print("\n--- Fraud Patterns ---")
    for p in patterns:
        print(f"[{p.id}] {p.alert_type} - {p.description}")

    models.close()


def add_user():
    models = SessionLocal()
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name=name, email=email)
    models.add(user)
    models.commit()
    print("User added")


def main():
    while True:
        menu()
        choice = input("Enter choice: ")
        if choice == "1":
            helper_1()
        elif choice == "2":
            add_pattern()
        elif choice == "3":
            list_patterns()
        elif choice == "4":
            add_user()
        elif choice == "5":
            exit_program()
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
