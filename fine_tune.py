from openai_client import get_client

client = get_client()

try:
    with open("data/auto-whitepaper.jsonl", "rb") as file:
        response = client.files.create(
            file=file,
            purpose="fine-tune"
        )
    
    file_id = response.id
    print(f"File created with ID: {file_id}")

    job = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-4o-mini-2024-07-18"  
    )

    print(f"Fine-tuning job created with ID: {job.id}")

except Exception as e:
    print(f"An error occurred: {str(e)}")