#!/usr/bin/python3
"""
Content:
    * Create a unique FileStorage instance for your application.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
