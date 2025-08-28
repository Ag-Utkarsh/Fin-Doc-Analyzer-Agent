## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai.tools import BaseTool # to create custom tools
from crewai_tools import SerperDevTool #import it directly from crewai_tools
from pydantic import BaseModel, Field
from pypdf import PdfReader
from typing import Type
import re


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
class InvestmentAnalysisInput(BaseModel):
    """Input schema for InvestmentAnalysisTool."""
    financial_document_data: str = Field(..., description="Financial data to analyze for investment recommendations")

class InvestmentTool(BaseTool):
    name: str = "InvestmentTool"
    description: str = "Analyzes financial data to provide investment recommendations, valuation metrics, and growth prospects. Uses financial ratios and market analysis."
    args_schema: Type[BaseModel] = InvestmentAnalysisInput
    def _run(self, financial_document_data: str) -> str:
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
        # Example: Extract key financial metrics (revenue, profit, expenses)

        metrics = {}
        patterns = {
            "revenue": r"(?:Revenue|Total Revenue|Net Revenue)[^\d]*([\d,\.]+)",
            "profit": r"(?:Profit|Net Profit|Gross Profit)[^\d]*([\d,\.]+)",
            "expenses": r"(?:Expenses|Total Expenses|Operating Expenses)[^\d]*([\d,\.]+)"
        }

        for key, pattern in patterns.items():
            match = re.search(pattern, processed_data, re.IGNORECASE)
            if match:
                value = match.group(1).replace(",", "")
                metrics[key] = float(value)
            else:
                metrics[key] = None

        analysis = "Investment Analysis:\n"
        for key, value in metrics.items():
            analysis += f"- {key.capitalize()}: {value if value is not None else 'Not found'}\n"
        return analysis

## Creating Risk Assessment Tool
class RiskInput(BaseModel):
    """Input schema for RiskAssessmentTool."""
    financial_document_data: str = Field(..., description="Financial data for risk assessment")

class RiskTool(BaseTool):
    name: str = "RiskTool"
    description: str = "Assesses financial risks based on document analysis and keyword extraction."

    def _run(self, financial_document_data: str) -> str:
        # Example: Extract risk-related keywords and basic scoring

        risk_keywords = [
            "debt", "liability", "loss", "risk", "uncertainty", "volatility",
            "default", "bankruptcy", "lawsuit", "regulatory", "fraud"
        ]
        risk_score = 0
        found_keywords = []

        for keyword in risk_keywords:
            count = len(re.findall(rf"\b{keyword}\b", financial_document_data, re.IGNORECASE))
            if count > 0:
                risk_score += count
                found_keywords.append(f"{keyword} ({count})")

        assessment = "Risk Assessment:\n"
        assessment += f"- Risk Score: {risk_score}\n"
        assessment += "- Keywords found: " + (", ".join(found_keywords) if found_keywords else "None") + "\n"
        return assessment