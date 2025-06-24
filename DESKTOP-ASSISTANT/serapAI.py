import requests
from serpapi import GoogleSearch

# Get the search query from the user
search_query = input("Enter a word to define: ")

params = {
    "engine": "google",
    "q": f"define {search_query}",  # Focus on retrieving definitions
    "location": "Seattle-Tacoma, WA, Washington, United States",
    "hl": "en",
    "gl": "us",
    "google_domain": "google.com",
    "num": "1",  # Limit to one result for focus
    "safe": "active",
    "api_key": "f453fbf81aa38dcfeb2974d3845fbe44044feef5001e0cfb4a2a5322287467c5"
}

# Fetch search results
search = GoogleSearch(params)
results = search.get_dict()

# Extract the "answer box" or definition from the response
try:
    # Check if a dictionary definition is present
    if "knowledge_graph" in results:
        definition = results["knowledge_graph"].get("description", "No definition found.")
        print(f"Definition: {definition}")
    elif "answer_box" in results and "definition" in results["answer_box"]:
        # Handle cases where the answer box contains a definition
        definition = results["answer_box"].get("definition", "No definition found.")
        print(f"Definition: {definition}")
    else:
        print("No definition found. Please refine your query.")
except Exception as e:
    print(f"An error occurred: {e}")
