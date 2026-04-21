from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()

tavily = TavilyClient()
#@tool
#def search(query: str) -> str:
 #   """Tool that searches over internet."""
  #  print(f"Searching for {query}")
   # #return "Tokyo weather is sunny"
   # return tavily.search(query=query)



llm = ChatOpenAI()
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {"messages": [HumanMessage(content="Search and list top 5 current Network Engineer jobs listed in Linkedin in Melbourne, Australia currently list them with job title company and salary range and link for the job posting and 3 key responsibilities from job description")]}
    )
    print(result)


if __name__ == "__main__":
    main()
