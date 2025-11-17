import sqlite3
import os

Vulnerability 4: Deserialization of Untrusted Data (CWE-502)
def load_data(data):
    import pickle
    return pickle.loads(data)  # Unsafe deserialization

Vulnerability 5: Exposed Secret in Code

AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
