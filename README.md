# accounts-manager

A small Python/Tkinter desktop app that appends account details to a local CSV file.

> **Security:** Passwords are stored in plaintext, not encrypted. The masked password field only hides typing on screen. Use dummy data for learning, not real credentials, and never commit the generated CSV file.

## Requirements

- Python 3 with Tkinter and a graphical desktop session.
- No third-party Python packages are required.
- On Ubuntu/Debian, install Tkinter if needed: `sudo apt install python3-tk`.

## Run

From the repository directory:

```bash
python3 "accounts manager.py"
```

Keep `paypal1.png` and `github-logo.png` in the working directory; the app loads them at startup.

## Usage

1. Fill in the website, username, password, email, phone number, and extra information.
2. Click **Submit** to append a row to `one.csv` in the current working directory. The file is created if it does not exist.
3. Open the CSV separately to inspect saved entries. The app does not provide search, editing, or deletion.

Column order is website, username, password, email, phone, and extra information. Headers are not added automatically; the UI suggests entering column names as the first submission if you want a header row.

This is a simple learning project with no input validation or encrypted storage. It can be extended for experimentation, but is not a secure password manager.

## Support

[Donate via PayPal](https://paypal.me/progahmad?locale.x=ar_EG).

## License

See [LICENSE](LICENSE).
