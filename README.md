# Market Feeds
The market feeds are used to provide the latest market insights about the Ethereum. The coverage can be extended to other blockchains in the future.

This should be an open-source project which will welcome any contributions from the community. The goal is to provide a reliable, accurate and insightfull market feeds for the community. Below is explanation of the project structure and how to contribute. 

## How to contribute
You can contribute by adding new feeds or editting/reviewing the ones from other contributors. In order to create a new feed, you need to run create.py script. The script will initialize streamlit app and you should provide the information about the feed. Once you are happy with the results, you can submit your feed for a review by someone else. If being approved, the feed will be added on the website.

### Creator
Before you start, make sure you have the following installed:
- Python 3.7 or higher
- Streamlit

To install streamlit, run the following command:
- `pip install streamlit`

Then after you clone the repository, run the following command to start the app if you are in the root directory:
- `streamlit run create.py`

When you access the app, it will request the following information:

Data: This includes numerical values and a query_id from Dune Analytics (we plan to integrate more sources shortly).
Prompts: Guidelines on interpreting and analyzing this specific dataset.

Once you are happy with the results, you can submit your feed for being added on the website. 
Be aware that the feed will be reviewed before being added to the website. 
Also you will be asked to insert your own OPENAI API key. If you don't have one, you can get it from [here](https://beta.openai.com/). Your API Key will be used only for your testing purposes and will not be stored anywhere. We don't have any access to your API key. This should just reduce costs for testing/creating the feeds, while ensuring sustainability of the project. If you feed is approved, we will use our own API key for the feeds on the website.  

This app will support data from Dune Analytics only. More data sources will be added in the future. We plan to add Flipside Crypto and DefiLlama in the near future, but we are open to suggestions.

Each feed consists of the data (numeric) and prompts (text). For a clearer understanding of the inputs required for the app, consider reviewing the template.json file. Additionally, for further guidance, click on the question mark symbol next to each field to access helpful information. The data is stored in the SQLite database under the `feed` table. Each feed is a separate line. The format of the data is as follows:

name | source | query_id | frequency | role | goal | audience | constraints | size | instructions | closing 

By calling the source with the query_id, we will get the data. The frequency is the desired frequency of this market feed. We will only support weekly now. The rest is the prompt engineering: 
Role: You should let llm know what is the role of the feed.
Goal: What is the goal of the feed?
Audience: Who is the audience of the feed?
Constraints: What are the constraints of the feed?
Size: What is the size (words) of the feed?
Instructions: How should llm understand and analyze the given data?
Closing: Final prompt to close the feed.

### Reviewer
To submit your feed for review, upload your JSON file to GitHub or share it on Discord. This allows other community members to examine and approve your feed inputs for inclusion on the website.




```

```
