# Create a Retrieval Assistant
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

# Step 1. Upload the file
file = client.files.create(file=open("bean-there-cafe.pdf", "rb"), purpose="assistants")

# Step 2. Create the Assistant
assistant = client.beta.assistants.create(
    instructions="You are a chatbot for Bean There Café, and you have access to files to answer questions about the company.",
    name="Bean There Café Bot",
    tools=[{"type": "retrieval"}],
    model="gpt-4-1106-preview",
    file_ids=[file.id],
)
print(assistant)

# Step 3. Create a Thread
thread = client.beta.threads.create()

# Step 4. Create a message
message = client.beta.threads.messages.create(
  thread_id='',
  role="user",
  content="How long will it take us to be profitable at our current monthly revenue if it stays consistent and how long will it take to make back the startup costs?",
)
print(message)

# Step 5. Run the Assistant
run = client.beta.threads.runs.create(
    thread_id="", assistant_id=""
)
print(run)

# Step 6. Retrieve the run
run = client.beta.threads.runs.retrieve(
        thread_id="",
        run_id=""
    )
print(run)

# Step 7. Check the messages
thread_messages = client.beta.threads.messages.list("")
print(thread_messages.data[1])
for message in thread_messages.data:
    for content in message.content:
            print(content.text.value)

# Step 8. Modify the Assistant
assistant = client.beta.assistants.update(
    assistant_id='',
    tools=[{"type": "retrieval"}, {"type": "code_interpreter"}],
)
print(assistant)
