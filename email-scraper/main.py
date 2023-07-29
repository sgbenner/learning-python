import os
import email
from email import policy
from email.parser import BytesParser

EMAIL_DIR = os.environ.get("EMAIL_DIR")

def extract_attachments(msg):
    attachments = []
    for part in msg.walk():
        content_disposition = str(part.get("Content-Disposition", ""))
        if "attachment" in content_disposition:
            filename = part.get_filename()
            attachment_data = part.get_payload(decode=True)
            attachments.append({"filename": filename, "data": attachment_data})
    return attachments

def parse_email(raw_email):
    msg = BytesParser(policy=policy.default).parsebytes(raw_email)

    # Get From (Sender)
    sender = msg.get("From")

    # Get To (Recipients)
    recipients = msg.get_all("To", [])

    # Get Subject
    subject = msg.get("Subject", "")

    # Get Message Body
    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))

            # skip any text/plain (txt) attachments
            if ctype == 'text/plain' and 'attachment' not in cdispo:
                body = part.get_payload(decode=True)  # decode
                break
    # not multipart - i.e. plain text, no attachments, keeping fingers crossed
    else:
        body = msg.get_payload(decode=True)

    # Extract Attachments
    attachments = extract_attachments(msg)

    return {
        "From": sender,
        "To": recipients,
        "Subject": subject,
        "Body": body,
        "Attachments": attachments
    }

if __name__ == "__main__":
    if os.path.exists(EMAIL_DIR) and os.path.isdir(EMAIL_DIR):
        # Get a list of all files in the directory
        files_list = os.listdir(EMAIL_DIR)

        # Loop through each file in the directory
        for filename in files_list:
            if filename == ".DS_Store" or filename == "others":
                continue

            # Create the full file path by joining the directory path and filename
            file_path = os.path.join(EMAIL_DIR, filename)

            with open(file_path, "rb") as f:
                raw_email = f.read()

            email_info = parse_email(raw_email)

            print("From:", email_info["From"])
            print("To:", email_info["To"])
            print("Subject:", email_info["Subject"])
            print("Body:", email_info["Body"])

            print("Attachments:")
            for attachment in email_info["Attachments"]:
                print("Filename:", attachment["filename"])
                # The attachment's binary data can be accessed using attachment["data"]
