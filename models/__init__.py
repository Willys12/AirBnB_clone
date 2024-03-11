#!/usr/bin/python3
"""
Initializes the FileStorage instance for the application.
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
