# Gmail Voice Agent

An Agentic AI solution to manage your Gmail inbox.

## Features

*   **Read Emails:** Listen to your latest unread emails.
*   **Summarize Threads:** Get a quick summary of long email conversations.
*   **Voice Replies:** Dictate and send replies.
*   **Email Management:** Archive, delete, or mark emails as read/unread.
* 

## Setup and Installation

Follow these steps to get the project running on your local machine.

### Prerequisites

*   Python 3.8+
*   A Google Account

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nishkarshsharma/agentic-ai.git
    cd gmail-voice-agent
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration: Google API Credentials

This project requires OAuth 2.0 credentials to access the Gmail API securely.

1.  **Enable the Gmail API:**
    *   Go to the Google Cloud Console.
    *   Create a new project.
    *   Navigate to "APIs & Services" > "Library".
    *   Search for "Gmail API" and enable it for your project.

2.  **Create OAuth Credentials:**
    *   Go to "APIs & Services" > "Credentials".
    *   Click "Create Credentials" > "OAuth client ID".
    *   Configure the consent screen if you haven't already. Select "External" and provide the required app information. Add your Google account as a test user.
    *   Choose "Desktop app" as the Application type.
    *   Click "Create".

3.  **Download Credentials File:**
    *   After creating the client ID, click the "Download JSON" button.
    *   Rename the downloaded file to `credentials.json`.
    *   Place this `credentials.json` file in the required directory (e.g., the project root or `agents/manager/auth/`).

    **⚠️ Important:** The `credentials.json` file contains sensitive information. It has been added to `.gitignore` to prevent it from being committed to version control but a sample file are given for reference.

4.  **Generate Authentication Token:**
    *   After downloading `credentials.json` from Google Cloud, run the `gcp_authenticator.py` script to generate your `token.json` file.
        ```bash
        python gcp_authenticator.py
        ```
    *   This will prompt you to log in to your Google account in the browser to authorize the application.
    *   Once complete, move the newly created `token.json` file to the directory where `token sample.json` is present.

## Usage

To start the agent, go to the "manager" directory and run the following command:

```bash
adk web  
```

On the first run, you will be prompted to authorize the application by logging into your Google account through a browser window.
