#!/usr/bin/env python3
# lib/debug.py

from models import SessionLocal
from check_fraud import User, Transaction, FraudPattern
import ipdb


models = SessionLocal()


users = session.query(User).all()
print("users in database:", users)


ipdb.set_trace()
