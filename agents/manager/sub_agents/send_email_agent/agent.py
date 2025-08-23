from google.adk import Agent
from ...auth import gmail_auth
from ..utils import create_message_body

def send_email(to: str, subject: str, message_text: str, sender: str = "me"):
    """This tool is used to create and send email"""
    try:
        service = gmail_auth.main()
        message_raw = create_message_body(
            to=to, subject=subject, message_text=message_text, sender=sender
        )
        send_message = (service.users().messages().send(userId="me", body=message_raw).execute())
        return send_message
    except Exception as error:
        raise Exception (f'An error occurred while sending the email: {error}')

send_email_agent = Agent(
    name = "send_email_agent",
    model="gemini-2.0-flash",
    global_instruction= """You are a helpful virtual assistant for a company. Always respond politely.""",
    description="""This agent create and send an email. 
        Executes a sequence of email writing and sending email.
        Returns: essage object, including message id
    """,
    instruction= """You are a specialized agent designed to create and send email from the information provided by the user. 
    You have access to following Tools:
    - send_email
    From the input provided by the user extract the following information and use it 
    as the parameter for tool
    - sender: The sender'-s email address.
    - to: The recipient
    -subject: subject of the email
    -message_body: the context which is the body of the email
    
    Ensure that you handle any potential errors gracefully and report the information back to the main agent.
    """,
    tools=[send_email]
    )