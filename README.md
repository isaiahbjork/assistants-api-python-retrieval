# Readme for OpenAI Retrieval Assistant Script

[YouTube Tutorial](https://youtu.be/isB1qKi1oRA): Watch the detailed walkthrough of this code and its functionalities.

## Overview
This script demonstrates the creation and interaction with a custom OpenAI Retrieval Assistant, specifically designed for "Bean There Café." It showcases how to upload a file, create an assistant, start a thread, send messages, run the assistant, retrieve results, check messages, and modify the assistant.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.8 or later.
- `openai` Python package.
- `python-dotenv` package for environment variable management.

## Installation
1. Clone this repository.
2. Install the required Python packages:
   ```bash
   pip install openai python-dotenv
   ```

## Setting Up
1. Create a `.env` file in your project's root directory.
2. Add your OpenAI API key to the `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage
The script is divided into several steps, each performing a distinct function:
1. **Upload File**: Uploads a PDF file to be used by the assistant.
2. **Create Assistant**: Creates a new assistant with specific instructions and tools.
3. **Create Thread**: Starts a new thread for communication.
4. **Create Message**: Sends a query to the thread.
5. **Run the Assistant**: Processes the query using the assistant.
6. **Retrieve the Run**: Fetches the result of the assistant's processing.
7. **Check the Messages**: Retrieves and prints all messages in a thread.
8. **Modify the Assistant**: Updates the assistant with additional capabilities.

To run the script, execute:
```python
python main.py
```

## Customizing Your Assistant
You can customize the assistant by changing the file upload, the instructions, the query, and the tools as per your requirements.

## Prompts
1. What are the items on the menu?
2. Could 'Bean There Café' benefit from adopting RFID technology for inventory management, and how would this align with its operational and financial plans?
3. What's the total monthly revenue supposed to be and the startup cost?
4. How long will it take us to be profitable at our current monthly revenue if it stays consistent and how long will it take to make back the startup costs?

## Additional Resources
- [OpenAI API Documentation](https://platform.openai.com/docs/): Provides more in-depth details and advanced features.

## Feedback and Contributions
Your feedback is valuable! If you have suggestions or modifications, feel free to create an issue or a pull request. For specific queries related to the tutorial, drop a comment on the YouTube video.