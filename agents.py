## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()


from crewai import Agent, LLM #import Agent directly from crewai, not from crewai.agents

from tools import search_tool, FinancialDocumentTool, InvestmentTool, RiskTool

### Create the LLM using Gemini Model
llm = LLM(
    model="gemini/gemini-2.5-flash",
    temperature=0.7,
)

# Creating an Experienced Financial Analyst agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Provide thorough, evidence-based financial analysis using proper methodologies",
    backstory="You are an experienced financial analyst with deep expertise in financial statement analysis, valuation methods, and risk assessment. You follow industry best practices and regulatory guidelines.",
    tools=[FinancialDocumentTool()],
    llm=llm,
    verbose=True,
    memory=True,
    allow_delegation=False
)

# Creating a document verifier agent
verifier = Agent(
    role="Financial Data Verifier",
    goal="Verify the accuracy and completeness of financial analysis and cross-check data",
    backstory=(
        "You are a diligent financial compliance specialist with a strong background in auditing and regulatory standards."
        "You carefully review documents to ensure all financial data is accurate, complete, and adheres to industry regulations."
        "You are detail-oriented, thorough, and committed to maintaining the integrity of financial reporting."
    ),
    tools=[FinancialDocumentTool(), search_tool],
    verbose=True,
    memory=True,
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=True
)


investment_advisor = Agent(
    role="Investment Strategy Advisor",
    goal="Provide investment recommendations based on financial analysis and market insights",
    backstory="""You are a seasoned investment advisor with deep market knowledge 
    and expertise in creating actionable investment strategies based on financial analysis.""",
    tools=[InvestmentTool(), search_tool],
    verbose=True,
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False
)


risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal="Evaluate investment risks and provide comprehensive risk analysis",
    backstory="""You are a risk management expert who specializes in identifying, 
    analyzing, and quantifying various types of investment risks.""",
    tools=[RiskTool(), search_tool],
    verbose=True,
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False
)
