## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai.tools import BaseTool # to create custom tools
from crewai_tools import SerperDevTool #import it directly from crewai_tools

# Add import for PDF reading
from pypdf import PdfReader

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
class FinancialDocumentTool(BaseTool): #creates a custom tool for reading financial documents
    name: str = "FinancialDocumentTool"
    description: str = "A tool to read and extract text from financial document PDFs"
    async def _run(path="data/TSLA-Q2-2025-Update.pdf"):
        """Tool to read data from a pdf file from a path

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Financial Document file
        """
        # Use PdfReader to read the PDF file
        reader = PdfReader(path)
        full_report = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                # Remove extra whitespaces and format properly
                while "\n\n" in content:
                    content = content.replace("\n\n", "\n")
                full_report += content + "\n"
        return full_report

## Creating Investment Analysis Tool
class InvestmentTool:
    async def analyze_investment_tool(financial_document_data):
        # Process and analyze the financial document data
        processed_data = financial_document_data

        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1

        # TODO: Implement investment analysis logic here
        return "Investment analysis functionality to be implemented"

## Creating Risk Assessment Tool
class RiskTool:
    async def create_risk_assessment_tool(financial_document_data):        
        # TODO: Implement risk assessment logic here
        return "Risk assessment functionality to be implemented"