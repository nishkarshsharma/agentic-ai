from google.adk import Agent
from .sub_agents.get_profile_agent.agent import get_profile_agent
from .sub_agents.draft_email_agent.agent import draft_email_agent
import json

with open('config.json', 'r') as file:
    config = json.load(file)

root_agent = Agent(
    name="manager",
    global_instruction= """You are a helpful virtual assistant for a company. Always respond politely.""",
    description="Manager agent that coordinates tasks and manages sub-agents.",
    instruction="""You are the main agent responsible for overseeing other agents.
    Your role is to understand commands, extract details, and delegate tasks to the appropriate sub-agent.
    IMPORTANT: Delegate any tasks related to user Gmail profile information to the 'get_profile_agent'.
    You have access to the following sub-agent:
    - get_profile_agent
    -draft_email_agent
    """,
    model=config["model_id"],
    sub_agents=[get_profile_agent, draft_email_agent], 
    tools=[],
)
