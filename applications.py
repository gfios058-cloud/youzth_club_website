"""Application persistence for the YOUZTH CLUB landing page.

Replace ``save_application`` when a hosted submission destination is available.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import TypedDict


class Application(TypedDict):
    full_name: str
    age: int
    city: str
    email: str
    telegram: str
    interests: str
    has_project_idea: str
    message: str


DATABASE_PATH = Path(__file__).resolve().parent / "data" / "applications.sqlite3"


def save_application(application: Application, database_path: Path = DATABASE_PATH) -> None:
    """Save one application to a local SQLite database."""
    database_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(database_path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                submitted_at TEXT NOT NULL,
                full_name TEXT NOT NULL,
                age INTEGER NOT NULL,
                city TEXT NOT NULL,
                email TEXT NOT NULL,
                telegram TEXT NOT NULL,
                interests TEXT NOT NULL,
                has_project_idea TEXT NOT NULL,
                message TEXT NOT NULL
            )
            """
        )
        connection.execute(
            """
            INSERT INTO applications (
                submitted_at, full_name, age, city, email, telegram,
                interests, has_project_idea, message
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                datetime.now(timezone.utc).isoformat(),
                application["full_name"],
                application["age"],
                application["city"],
                application["email"],
                application["telegram"],
                application["interests"],
                application["has_project_idea"],
                application["message"],
            ),
        )
