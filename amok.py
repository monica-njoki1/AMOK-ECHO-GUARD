from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from check_fraud import Base, User, Transaction, FraudPattern


engine = create_engine("sqlite:///checkfraud.db")
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

Base.metadata.create_all(bind=engine)

email = ""

existing = session.query(User).filter_by(email=email).first()
if not existing:
    user1 = User(name="Monica Njoki", email="monica@gmail.com")
    user2 = User(name="John Abdul", email="john@gmail.com")
    user3 = User(name="Mary Atieno", email="mary@gmail.com")
    user4 = User(name="Henry Mwambonu", email="henry@gmail.com")
    print("Users added.")
else:
    print("Users already exist.")
    session.close()
    exit()  


session.add_all([user1, user2, user3, user4])
session.commit()


existing_tx = models.query(Transaction).filter_by(code=code).first()
if existing_tx:
    print(f"Transaction with code {code} already exists!")
    models.close()
    return


transaction1 = Transaction(user_id=user1.id, amount=5000.00, code="12345", status="completed")
transaction2 = Transaction(user_id=user2.id, amount=1500.00, code="46345", status="pending")
transaction3 = Transaction(user_id=user1.id, amount=2000.00, code="12555", status="completed")
transaction4 = Transaction(user_id=user1.id, amount=500.00, code="78335", status="completed")


session.add_all([transaction1, transaction2, transaction3, transaction4])
session.commit()


fraud_pattern1 = FraudPattern(transaction_id=transaction2.id, alert_type="suspicious_amount", description="High amount flagged")
session.add(fraud_pattern1)
session.commit()


print("Data seeded successfully.")