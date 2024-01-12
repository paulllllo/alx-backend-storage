#!/usr/bin/env python3
"""ALX SE"""

def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection based on kwargs"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
    