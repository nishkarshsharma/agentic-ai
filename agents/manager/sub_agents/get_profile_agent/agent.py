from google.adk import Agent
from ...auth import gmail_auth


#tool
def get_profile() -> dict:
    """
    Retrieves the user's Gmail labels.
    Returns a dictionary containing a list of label names.
    """
    service = gmail_auth.main()
    results = service.users().labels().list(userId="me").execute()
    labels = results.get("labels", [])
    if not labels:
        return {"status": "failed", "labels": "No labels found."}

    label_names = [label["name"] for label in labels]
    return {"status": "success", "labels": label_names}


#Create the get_profile agent
get_profile_agent = Agent(
    name = "get_profile_agent",
    global_instruction= """You are a helpful virtual assistant for a company. Always respond politely.""",
    description=    """
    This agent retrieves the user's Gmail profile information, including a list of their Gmail labels.
    """,
    instruction= """You are a specialized agent designed to retrieve a user's Gmail profile information. 
    When you are called, use the 'get_profile' tool to access the Gmail API and retrieve the 
    user's profile details, specifically the list of labels associated with their Gmail account.
    Ensure that you handle any potential errors gracefully and report the information back to the main agent.
    """,
    # model=model_id,
    tools=[get_profile]
    )
