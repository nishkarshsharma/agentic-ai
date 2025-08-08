from google.adk import Agent
from ...auth import gmail_auth
import base64
from email.mime.text import MIMEText

def create_draft(to: str, subject: str, message_text: str, sender: str = "me"):
    """This tool is used to create and insert a draft email"""
    try:
        if not message_text:
            raise Exception("message_text is empty")
        if not sender:
            raise Exception("Sender is empty")
        if not subject:
            raise Exception("subject is empty")
        if not to:
            raise Exception("Recipient's email('to') is empty")
        
        service = gmail_auth.main()
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        message_body = {'message': {'raw': raw}}
        
        draft = service.users().drafts().create(userId=sender, body=message_body).execute()
        return draft
    except Exception as error:
        raise Exception (f'An error occurred: {error}')

draft_email_agent = Agent(
    name = "draft_email_agent",
    global_instruction= """You are a helpful virtual assistant for a company. Always respond politely.""",
    description=    """
    This agent create and insert a draft email. Returns: Draft object, including draft id and message meta data.
    """,
    instruction= """You are a specialized agent designed to draft email from the information provided by the user. 
    You have access to following Tools:
    - create_draft

    From the input provided by the user extract the following information and use it 
    as the parameter for tool
    - sender: The sender'-s email address.
    - to: The recipient
    -subject: subject of the email
    -message_body: the context which is the body of the email
    
    Ensure that you handle any potential errors gracefully and report the information back to the main agent.
    """,
    # model=model_id,
    tools=[create_draft]
    )