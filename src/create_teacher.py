import getpass
import json
import os
from pathlib import Path

from teacher_auth import hash_password


credentials_file = Path(__file__).with_name("teachers.json")


def main():
    username = input("Teacher username: ").strip()
    if not username:
        raise SystemExit("Username cannot be empty")

    password = getpass.getpass("Teacher password: ")
    confirmation = getpass.getpass("Confirm password: ")
    if not password:
        raise SystemExit("Password cannot be empty")
    if password != confirmation:
        raise SystemExit("Passwords do not match")

    if credentials_file.exists():
        data = json.loads(credentials_file.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("teachers"), dict):
            raise SystemExit("teachers.json must contain a teachers object")
    else:
        data = {"teachers": {}}

    data["teachers"][username] = hash_password(password)
    credentials_file.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    os.chmod(credentials_file, 0o600)
    print(f"Teacher {username!r} added to {credentials_file.name}.")


if __name__ == "__main__":
    main()