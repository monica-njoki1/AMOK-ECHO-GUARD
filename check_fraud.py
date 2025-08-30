from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean, func
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine


Base = declarative_base()


engine = create_engine("sqlite:///company.db", echo=True)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    transactions = relationship("Transaction", back_populates="user")


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float, nullable=False)
    code = Column(String(100), unique=True, nullable=False)
    timestamp = Column(DateTime, server_default=func.now())
    status = Column(String(50), default="pending")  
    user = relationship("User", back_populates="transactions")
    fraud_patterns = relationship("FraudPattern", back_populates="transaction")


class FraudPattern(Base):
    __tablename__ = "fraud_patterns"
    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(Integer, ForeignKey("transactions.id"))
    alert_type = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    is_resolved = Column(Boolean, default=False)
    transaction = relationship("Transaction", back_populates="fraud_patterns")


