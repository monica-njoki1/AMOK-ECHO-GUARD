# lib/helpers.
import re
from models import SessionLocal
from check_fraud import Transaction, FraudPattern

def helper_1():
    models = SessionLocal()
    """Run fraud check on a transaction"""
    code = input("Enter transaction code: ")
    amount = float(input("Enter transaction amount: "))
    user_id = int(input("Enter user ID: "))

    if not re.match(r"^[A-Za-z0-9]+$", code) or len(code) < 5:
        status = "fraud"
    else:
        status = "safe"

    
    patterns = models.query(FraudPattern).all()
    for p in patterns:
        if re.search(p.description, code):
            status = "fraud"
            break

    tx = Transaction(user_id=user_id, amount=amount, code=code, status=status)
    models.add(tx)
    models.commit()


    print(f"Results: {status.upper()}")
    print("\n--- Transaction History---")
    for t in models.query(Transaction).all():
        print(f"[{t.id}] {t.code} - {t.status} ({t.timestamp})")

    models.close()
        


def exit_program():
    print("Goodbye!")
    exit(0)


    
