from langchain_core.tools import tool
import requests
import os

# Used tavily the search engine tool : https://app.tavily.com/home 
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")
# TAVILY_API_KEY = ""
@tool
def web_search(query: str) -> dict:
    """
    Search Tavily for dataset-related pages.
    Returns structured JSON results.
    """
    if not TAVILY_API_KEY:
        return {
            "error": "Tavily API key missing",
            "query": query
        }

    try:
        response = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": TAVILY_API_KEY,
                "query": query,
                "search_depth": "basic",
                "max_results": 5,
                "include_domains": [
                    "kaggle.com",
                    "uci.edu",
                    "huggingface.co",
                    "data.gov",
                    "data.europa.eu"
                ]
            },
            timeout=15
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        return {
            "error": "Request timed out",
            "query": query
        }

    except requests.exceptions.HTTPError as e:
        return {
            "error": f"HTTP error {response.status_code}",
            "details": response.text,
            "query": query
        }

    except Exception as e:
        return {
            "error": "Unexpected error",
            "details": str(e),
            "query": query
        }