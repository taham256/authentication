# OTP Login System

This is a simple One-Time Password (OTP) login system implemented in Python. It allows users to sign in using a username and email, where an OTP is sent to their email address for verification.

## Features

- **OTP Generation**: Generates a random 4-digit OTP for user verification.
- **Email Sending**: Sends OTP via email using SMTP with Gmail.
- **OTP Expiration**: OTPs expire after 5 minutes for added security.
- **Error Handling**: Manages errors during email sending and provides feedback.

## Requirements

- Python 3.x
- `smtplib` (built-in)
- Environment variables for email configuration:
  - `OFFICIAL_EMAIL`: Your Gmail address to send OTPs.
  - `SMTP_PASSWORD`: Your Gmail account password (may require generating an app password if 2-Step Verification is enabled).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/taham256/authentication.git
   cd otp-login-system
   
## set up environment variables on machine:
•On Linux/Mac:
   export OFFICIAL_EMAIL='your_email@gmail.com'
   export SMTP_PASSWORD='your_password'
•On Windows:
   set OFFICIAL_EMAIL='your_email@gmail.com'
   set SMTP_PASSWORD='your_password'
