from crewai import Crew, Process
from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from task import analyze_financial_document, investment_analysis, risk_assessment, verification

def run_crew(query: str, file_path: str):
    """To run the whole crew"""
    financial_crew = Crew(
        agents=[financial_analyst, investment_advisor, risk_assessor, verifier],
        tasks=[analyze_financial_document, investment_analysis, risk_assessment, verification],
        process=Process.sequential
    )

    result = financial_crew.kickoff({
        'query': query,
        'file_path': file_path
    })
    return result
run_crew("Analyze this financial document for investment insights", "data/TSLA-Q2-2025-Update.pdf")

