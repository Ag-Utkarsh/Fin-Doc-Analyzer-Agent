## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai.tools import BaseTool # to create custom tools
from crewai_tools import SerperDevTool #import it directly from crewai_tools
from pydantic import BaseModel, Field
from pypdf import PdfReader
from typing import Type


## Creating search tool
search_tool = SerperDevTool()

class FinancialDocumentToolInput(BaseModel):
    file_path: str = Field(..., description="Path to the financial document PDF.")

class FinancialDocumentTool(BaseTool):
    name: str = "FinancialDocumentTool"
    description: str = "A tool to read and extract text from financial document PDFs"
    args_schema: Type[BaseModel] = FinancialDocumentToolInput

    def _run(self, file_path: str) -> str:
        """Tool to read data from a pdf file from a path

        Args:
            file_path (str): Path of the pdf file.

        Returns:
            str: Full Financial Document file content
        """
        try:
            reader = PdfReader(file_path)
            full_report = ""
            for page in reader.pages:
                content = page.extract_text()
                if content:
                    # Remove extra whitespaces and format properly
                    while "\n\n" in content:
                        content = content.replace("\n\n", "\n")
                    full_report += content + "\n"
            return full_report
        except FileNotFoundError:
            return f"Error: PDF file not found at path: {file_path}"
        except Exception as e:
            return f"Error reading PDF: {str(e)}"

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