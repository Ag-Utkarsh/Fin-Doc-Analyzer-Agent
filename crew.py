from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document

def run_crew(query: str, file_path: str="data/TSLA-Q2-2025-Update.pdf"):
    """To run the whole crew"""
    financial_crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_financial_document],
        process=Process.sequential,
    )

    result = financial_crew.kickoff({
        'query': query,
        'file_path': file_path
    })
    return result
run_crew("Analyze this financial document for investment insights", "data/TSLA-Q2-2025-Update.pdf")

