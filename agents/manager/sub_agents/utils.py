import base64
from email.mime.text import MIMEText

def create_message_body(to: str, subject: str, message_text: str, sender: str = "me") -> dict:
    """
    Creates a message body for the Gmail API.
    Validates inputs and returns a dictionary with the raw, base64-encoded message.
    """
    if not to:
        raise ValueError("Recipient's email ('to') is empty")
    if not subject:
        raise ValueError("Subject is empty")
    if not message_text:
        raise ValueError("Message text is empty")
    if not sender:
        raise ValueError("Sender is empty")

    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}
