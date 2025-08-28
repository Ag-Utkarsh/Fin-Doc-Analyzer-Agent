## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier, investment_advisor, risk_assessor #import the agents
from tools import search_tool, FinancialDocumentTool, InvestmentTool, RiskTool #import the tools

## Creating a task to help solve user's query
analyze_financial_document = Task(
    description="Analyze the financial document at {file_path} to answer the user's query: {query}. Use FinancialDocumentTool to extract and analyze the document content.",
    expected_output="Comprehensive financial analysis based on the document content, addressing the user's specific query with evidence-based insights.",
    agent=financial_analyst,
    tools=[FinancialDocumentTool()],
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis = Task(
    description="Analyze the financial data from the document at {file_path} to provide actionable investment advice based on the user's query: {query}. Use InvestmentTool to evaluate key financial metrics, trends, and market context. Recommend suitable investment strategies and products that align with the user's financial goals and risk tolerance.",
    expected_output="""Detailed investment analysis including:
- Evaluation of relevant financial ratios and performance indicators
- Identification of investment opportunities and potential risks
- Recommendations for appropriate investment products or asset classes
- Evidence-based rationale for each recommendation
- References to supporting data from the financial document""",
    agent=investment_advisor,
    tools=[InvestmentTool(), search_tool],
    context=[analyze_financial_document],
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment = Task(
    description="Assess the risks associated with the financial document at {file_path} in relation to the user's query: {query}. Use RiskTool to identify and evaluate key financial, operational, and market risks. Consider regulatory compliance, risk mitigation strategies, and the overall risk profile relevant to the user's objectives.",
    expected_output="""Thorough risk assessment including:
- Identification and analysis of major financial, operational, and market risks
- Evaluation of risk exposure and potential impact on financial goals
- Recommendations for risk mitigation strategies and controls
- Consideration of regulatory and compliance requirements
- References to supporting data and evidence from the financial document""",
    agent=risk_assessor,
    tools=[RiskTool(), search_tool],
    context=[analyze_financial_document, investment_analysis],
    async_execution=False,
)

    
verification = Task(
    description="Verify whether the document at {file_path} is a legitimate financial document. Carefully examine the content for financial terminology, structure, and relevant data. Avoid assumptions and base your verification on clear evidence from the document.",
    expected_output="""Verification report including:
- Determination of whether the document is a financial document, with supporting evidence
- Identification of key financial terms, sections, or data present in the document
- Explanation of reasoning behind the verification decision
- Reference to specific content or features found in the document""",
    agent=verifier,
    tools=[FinancialDocumentTool(), search_tool],
    context=[analyze_financial_document, investment_analysis, risk_assessment],
    async_execution=False
)
