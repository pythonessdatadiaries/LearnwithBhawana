# Python Project 7: Email Calendar Reminder (.ics)

This Python project helps you create a calendar reminder and send it via email using a `.ics` file. The recipient can easily import the file into their calendar app (Google Calendar, Outlook, etc.).

---

## Features

- Creates a `.ics` calendar event (for doctor appointment, meetings, etc.)
- Sends the event as an email attachment
- Can be used on phone/laptop to automate reminders

---

## How It Works

1. A calendar event is created using the `ics` library.
2. It is saved as a `.ics` file locally.
3. The `.ics` file is attached to an email.
4. The email is sent using Gmail’s SMTP server.

---

## Libraries Used

- `ics` – for creating calendar events
- `smtplib` – for sending emails via SMTP
- `email.message` – for creating MIME email with attachment
- `datetime` – to handle event timing

---

## Gmail App Password Setup

To send emails via Gmail:

1. Turn on **2-Step Verification** in your Google Account.
2. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
3. Choose app as "Mail" and device as "Other" (like "PythonApp")
4. Generate and copy the 16-character password
5. Use it in place of your regular password in the Python script

---

## Output

After running the script:
- A `.ics` file is created and emailed
- The receiver can tap the file to import it into their phone or Gmail calendar

---

## Use Case Examples

- Sending reminders to yourself or your family
- Automating invites for events
- Personal assistant bots

---

## Sample Output
