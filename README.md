# EmailAutomator
# Automated Email Sender for HR Outreach

This Python script automates the process of sending personalized emails to HR contacts. It uses a CSV file containing contact details and sends customized emails using a template.

## Features

- Loads HR contact details (name, email, company) from a CSV file.
- Sends personalized emails to each contact.
- Uses an email template to standardize messages.
- Includes error handling for missing files, incorrect credentials, and email server issues.
- Adds delays between emails to avoid spam filters.

## Requirements

- Python 3.7 or higher
- Internet connection
- A Google account with App Passwords enabled for email sendin

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/email-sender
   cd email-sender
   ```

2. **Install dependencies**:
   Install the required Python packages using pip:
   ```bash
   pip install pandas python-dotenv
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project directory and add your email credentials:
   ```
   EMAIL=your.email@gmail.com
   EMAIL_APP_PASSWORD=your-16-character-app-password
   ```

   > **Note**: For security, use a Google App Password instead of your main email password. [Learn how to generate an App Password](https://support.google.com/accounts/answer/185833?hl=en).

4. **Prepare your contact data**:
   - Ensure your contact data is in a CSV file named `hr_contacts.csv`.
   - The file should include the following columns:
     - `Name`: Recipient's name
     - `Email`: Recipient's email address
     - `Company`: Recipient's company name

## Usage

Run the script using the following command:
```bash
python email_sender.py
```

### What Happens:
1. The script loads your contact data from `hr_contacts.csv`.
2. It connects to the Gmail SMTP server using your credentials.
3. For each contact, it sends a personalized email using the template.
4. The script adds a delay between emails to prevent being flagged as spam.

## Email Template

The email content can be customized by modifying the `create_email_template` function in `email_sender.py`. The default template is:

```
Dear $name,

I hope this email finds you well. I am reaching out regarding potential opportunities at $company.

I am a final-year student with experience in AI/ML development. My projects and internships demonstrate my ability to create innovative tools and solutions.

I’d love to explore any opportunities at $company where my skills could contribute. Please let me know if there are any openings or ways I can collaborate with your team.

Thank you for your time!

Best regards,  
[Your Name]  
Resume: [Your Resume Link]  
LinkedIn: [Your LinkedIn Profile]  
```

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for bug reports or feature requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

