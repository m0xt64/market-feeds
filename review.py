import os
from openai import OpenAI
from dune_client.client import DuneClient
import streamlit as st
import json
import openai
import pandas as pd
import base64

#os.environ["OPENAI_API_KEY"] = "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"
#os.environ["DUNE_API_KEY"] = "hTdFI8LQcHtFauNrRuY394W2hRZRIfUQ"

# Function to read JSON data from the uploaded file
def load_json_data(uploaded_file):
    if uploaded_file is not None:
        string_data = uploaded_file.getvalue().decode("utf-8")
        return json.loads(string_data)
    return None

def save_json(data, default_filename='updated_data'):
    """Save data to a JSON file and return a link for downloading."""
    # Use feed_info['name'] as the filename, with a fallback to default_filename
    filename = f"{data['feed_info'].get('name', default_filename)}.json"

    # Replace characters not allowed in filenames
    filename = filename.replace('/', '_').replace('\\', '_')

    with open(filename, 'w') as f:
        json.dump(data, f)
    with open(filename, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    href = f'<a href="data:file/json;base64,{b64}" download="{filename}">Download updated JSON file</a>'
    return href

# Function to prepare the prompt from JSON data
def prepare_prompt(data):
    # Modify this function based on your JSON structure and requirements
    prompt = f"{data['feed_info']['role']} {data['feed_info']['goal']} {data['feed_info']['audience']} {data['feed_info']['constraints']} {data['feed_info']['size']} {data['feed_info']['instructions']} {data['feed_info']['closing']}"
    return prompt

def get_data(query_id):
    dune = DuneClient.from_env()
    results = dune.get_latest_result(query_id)
    data_ = results.result.rows
    df = pd.DataFrame(data_)
    _data = df.loc[:0]
    merged_data = _data.to_json(orient='records')
    return merged_data

def main():
    st.sidebar.markdown('# Market Feeds Reviewer')
    st.sidebar.markdown("##### Review and Edit your market feed.")
    st.sidebar.markdown("###### See help icon for tips and templates.")

    # API key input (should be done securely in production)
    api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")
    api_dune_key = st.sidebar.text_input("Enter your Dune API key:", type="password")

    if api_key and api_dune_key:
        os.environ["OPENAI_API_KEY"] = api_key
        os.environ["DUNE_API_KEY"] = api_dune_key

        # File uploader
        uploaded_file = st.sidebar.file_uploader("Upload a JSON file", type=["json"])

        if uploaded_file is not None:
            data = load_json_data(uploaded_file)  
            if data and 'feed_info' in data:
                feed_info = data['feed_info']
                st.write("Edit Feed Info:")

                # Create editable text areas for each field
                for key in ['name', 'role', 'goal', 'constraints', 'size', 'instructions', 'closing']:
                    feed_info[key] = st.text_area(key.capitalize(), value=feed_info.get(key, ''), height=50)

                if st.button("Save Changes"):
                    # Update the feed_info in the main data object
                    data['feed_info'] = feed_info

                    # Save the updated data to a new JSON file and provide a download link
                    st.markdown(save_json(data), unsafe_allow_html=True)

                prompt = prepare_prompt(data)

                query_id = data['feed_info'].get('query_id')
                if query_id:
                    merged_data = get_data(query_id)
                    st.write("Data:")
                    st.text_area("Data", merged_data, height=150)

                    if st.button("Run Model"):
                        model = data['model_info']['model']
                        temperature = data['model_info']['temperature']
                        response = execute_model(prompt, merged_data, model, temperature)
                        st.write("Model Response:")
                        st.text_area("Response", response, height=150)
                else:
                    st.error("Query ID not found in JSON.")
    else:
        st.error("API keys are required.")

# Modify execute_model to accept model and temperature as arguments
def execute_model(prompt, merged_data, model, temperature):
    system_message = prompt
    client = OpenAI()
    response = client.chat.completions.create(
        model=model, 
        messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": merged_data}
            ],
        max_tokens=4000, 
        temperature=temperature)

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    main()
