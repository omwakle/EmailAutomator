import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from string import Template
import time
import os
from dotenv import load_dotenv

def load_hr_data(file_path):
    """
    Load HR contact data from CSV/Excel file
    """
    try:
        df = pd.read_csv("CompanyWise HR contact (1) (1).csv")
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

def create_email_template():
    """
    Returns a template for the email content
    """
    return Template("""
Dear $name,

I hope this email finds you well. I am reaching out regarding potential opportunities at $company.

I am a final-year student with experience in AI/ML development. My projects and internships demonstrate my ability to create innovative tools and solutions.

I’d love to explore any opportunities at $company where my skills could contribute. Please let me know if there are any openings or ways I can collaborate with your team.

Thank you for your time!

I would greatly appreciate the opportunity to discuss this further.

Best regards,
[Your Name]
resume: [Your Resume Link]
LinkedIn: [Your LinkedIn Profile]
    """)

def setup_email_server(sender_email, password):
    """
    Setup and return SMTP server connection
    """
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Detailed error handling for login
        try:
            server.login(sender_email, password)
            print("Successfully logged into email server!")
            return server
        except smtplib.SMTPAuthenticationError:
            print("Authentication failed! Please check:")
            print("1. Your email address is correct")
            print("2. You're using an App Password (not your regular password)")
            print("3. 2-Step Verification is enabled on your Google Account")
            print("\nTo get an App Password:")
            print("1. Go to Google Account > Security")
            print("2. Enable 2-Step Verification if not enabled")
            print("3. Go to App passwords")
            print("4. Generate a new app password for 'Mail'")
            return None
        
    except Exception as e:
        print(f"Error setting up email server: {e}")
        return None

def send_personalized_email(server, template, sender_email, recipient_data):
    """
    Send personalized email to a single recipient
    """
    msg = MIMEMultipart()
    
    # Personalize the email content
    email_content = template.substitute(
        name=recipient_data['Name'],
        company=recipient_data['Company']
    )
    
    # Setup email headers
    msg['From'] = sender_email
    msg['To'] = recipient_data['Email']
    msg['Subject'] = f"Inquiry About Opportunities at {recipient_data['Company']}"
    
    # Add email body
    msg.attach(MIMEText(email_content, 'plain'))
    
    try:
        server.send_message(msg)
        print(f"Successfully sent email to {recipient_data['Name']} at {recipient_data['Company']}")
        return True
    except Exception as e:
        print(f"Error sending email to {recipient_data['Email']}: {e}")
        return False

def main():
    # Load environment variables
    load_dotenv()
    
    # Get credentials from environment variables
    SENDER_EMAIL = os.getenv('EMAIL')
    EMAIL_PASSWORD = os.getenv('EMAIL_APP_PASSWORD')
    DATA_FILE = "hr_contacts.csv"
    
    if not SENDER_EMAIL or not EMAIL_PASSWORD:
        print("Error: Email credentials not found in environment variables!")
        print("Please create a .env file with your credentials:")
        print("EMAIL=your.email@gmail.com")
        print("EMAIL_APP_PASSWORD=your-16-character-app-password")
        return
    
    # Load HR contact data
    df = load_hr_data(DATA_FILE)
    if df is None:
        return
    
    # Create email template
    template = create_email_template()
    
    # Setup email server
    server = setup_email_server(SENDER_EMAIL, EMAIL_PASSWORD)
    if not server:
        return
    
    try:
        # Send emails to each recipient
        for _, row in df.iterrows():
            success = send_personalized_email(
                server,
                template,
                SENDER_EMAIL,
                {
                    'Name': row['Name'],
                    'Email': row['Email'],
                    'Company': row['Company']
                }
            )
            
            # Add delay between emails to avoid triggering spam filters
            if success:
                time.sleep(5)  # 5 second delay between emails
        
    finally:
        # Close the server connection
        if server:
            server.quit()

if __name__ == "__main__":
    main()