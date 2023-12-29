# Market Feeds
The market feeds are used to provide the latest market insights about the Ethereum. The coverage can be extended to other blockchains in the future.

This should be an open-source project which will welcome any contributions from the community. The goal is to provide a reliable, accurate and insightfull market feeds for the community. Below is explanation of the project structure and how to contribute. 

## How to contribute
You can contribute by adding new feeds. In order to create a new feed, you need to run create.py script. The script will initialize streamlit app and you should provide the information about the feed. Once you are happy with the results, you can submit your feed for being added on the website.

### Creator
Before you start, make sure you have the following installed:
- Python 3.7 or higher
- Streamlit

To install streamlit, run the following command:
- `pip install streamlit`

Then after you clone the repository, run the following command to start the app if you are in the root directory:
- `streamlit run create.py`

You will be prompted to provide the data and prompts about the feed. Once you are happy with the results, you can submit your feed for being added on the website. 
Be aware that the feed will be reviewed before being added to the website. 
Also you will be asked to insert your own OPENAI API key. If you don't have one, you can get it from [here](https://beta.openai.com/). Your API Key will be used only for your testing purposes and will not be stored anywhere. We don't have any access to your API key. This should just reduce our costs for testing/creating the feeds, while ensuring sustainability of the project. We will use our own API key for the feeds that will be added to the website.  

This app will support data from Dune Analytics only. More data sources will be added in the future. We plan to add Flipside Crypto and DefiLlama in the near future, but we are open to suggestions.


Each feed consists of the data (numeric) and prompts (text). The data is stored in the SQLite database under the `feed` table. Each feed is a separate line. The format of the data is as follows:

ID | name | source | query_id | frequency | role | goal | audience | constraints | size | instructions | closing 

By calling the source with the query_id, you will get the data. The frequency is the desired frequency of this market feed. We will only support weekly now. The rest is the prompt engineering: 
Role: You should let llm know what is the role of the feed.
Goal: What is the goal of the feed?
Audience: Who is the audience of the feed?
Constraints: What are the constraints of the feed?
Size: What is the size (words) of the feed?
Instructions: How should llm understand and analyze the given data?
Closing: Final prompt to close the feed.

I will provide an example of mostly used prompts. Unless you want to experiment with the existing prompts, you don't need to change them. You will spend most of the time by crafting the particular query on dune and then providing the propoer instructions how to analyze that data. 

```

```
