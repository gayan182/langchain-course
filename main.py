from typing import Dict

from pydantic import BaseModel,Field
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()

class Source(BaseModel):
    """Schema for a source used by the agent"""
    url: str = Field(description="The URL of the source")

class Salary(BaseModel):
    """Schema for salary details for jobs"""
    salary: str = Field(description="The salary of the job")    


class AgentResponse(BaseModel):
    """Schema for the response from the agent"""
    #message: str = Field(description="The answer from the agent to the query")
    salary: Dict[str,str] = Field(default_factory=dict,description="Dictionary of job titles and salaries")
    #sources: List[Source] = Field(default_factory=list, description="The sources used to answer the query")


tavily = TavilyClient()
#@tool
#def search(query: str) -> str:
 #   """Tool that searches over internet."""
  #  print(f"Searching for {query}")
   # #return "Tokyo weather is sunny"
   # return tavily.search(query=query)



llm = ChatOpenAI()
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {"messages": [HumanMessage(content="Search and list top 5 current Network Engineer jobs listed in Linkedin in Melbourne, Australia currently list them with job title company and salary range and link for the job posting and 3 key responsibilities from job description")]}
    )
    print(result)


if __name__ == "__main__":
    main()
