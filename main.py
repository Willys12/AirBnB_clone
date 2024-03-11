#!/usr/bin/env python3
"""
Entry point for the Airbnb clone application.
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


def main():
    """
    Main function to run the application.
    """
    # Initialize the FileStorage
    storage = FileStorage()
    storage.reload()

    # Example: Create a new instance of a model
    new_model = BaseModel()
    new_model.name = "Example Model"
    print(f"Created new model: {new_model}")

    # Save the new model instance
    new_model.save()
    print("Model saved.")

    # Reload the storage to demonstrate persistence
    storage.reload()
    reloaded_model = (
        storage.all().get(
            f"{new_model.__class__.__name__}.{new_model.id}"
            )
        )
    if reloaded_model:
        print(f"Reloaded model: {reloaded_model}")
    else:
        print("Model not found after reload.")


if __name__ == "__main__":
    main()
