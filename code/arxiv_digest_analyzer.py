import os
import re # dealing with regular expressions
import pandas as pd

# Let's read the newly uploaded document and analyze it for papers that deal with the topic of generative AI, LLMs, and/or transformers.
# After identifying relevant papers, we will create a table containing the titles of those papers.

with open(os.path.join(os.getcwd(), "data", "2024-03-13.txt"), 'r') as file:
    content = file.read()

# Keywords for identifying relevant papers
keywords = ['generative AI', 'LLM', 'transformer', 'AGI']

# Function to parse the document and extract titles of relevant papers
def find_relevant_papers_titles(content, keywords):
    # Splitting the document based on a consistent structure to isolate each article
    raw_articles = content.split("-------------------------------------------------------------")
    relevant_titles = []
    
    for raw_article in raw_articles:
        if any(keyword.lower() in raw_article.lower() for keyword in keywords):
            title_match = re.search(r'Title: (.+)', raw_article)
            if title_match:
                relevant_titles.append(title_match.group(1).strip())
    
    return relevant_titles

# Extract titles of relevant papers
relevant_titles = find_relevant_papers_titles(content, keywords)

# Create a DataFrame for the titles of relevant papers
df_relevant_titles = pd.DataFrame(relevant_titles, columns=["Title"])

# Saving the DataFrame to a CSV file for the relevant titles
# Create the filepath from the root of the code workspace to the "output" folder
output_folder = os.path.join(os.getcwd(), "output")
os.makedirs(output_folder, exist_ok=True)

# Create the filepath for the relevant titles CSV file
relevant_titles_csv_path = os.path.join(output_folder, "relevant_titles_table.csv")
df_relevant_titles.to_csv(relevant_titles_csv_path, index=False)

relevant_titles_csv_path
