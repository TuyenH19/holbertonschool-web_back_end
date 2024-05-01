#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
    """Provides stats about Nginx logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['logs']
    collection = db['nginx']
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{collection.count_documents({})} logs")
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    print(collection.count_documents({"method": "GET", "path": "/status"}),
          "status check")

    client.close()
