# src/nodes/context_node.py
import logging
import os
from langchain_openai import ChatOpenAI
from src.context.ecommerce import get_ecommerce_queries
from src.tools.search_engine import web_search
from src.models.state_models import MainState, Context

logger = logging.getLogger(__name__)

# used open router api : https://openrouter.ai and trinity mini for samll search mapping
model = ChatOpenAI(
    model="arcee-ai/trinity-mini:free",
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key= "",
)

queryCat = {
    "ecommerce": get_ecommerce_queries,
    # "streaming": get_streaming_queries, etc.
}

def context_node(state: MainState):
    logger.info(f"Fetching context for category: {state.get('category')}")
    
    # 1. Fetch queries based on category
    category = state.get("category", "ecommerce")
    query_func = queryCat.get(category)
    queries = query_func() # Function call
    
    combined_raw_data = ""
    
    # 2. Fetch data from web_search
    try:
        for q in queries:
            res = web_search.invoke({"query": q})
            combined_raw_data += str(res.get("results", "")) + "\n"
    except Exception as e:
        logger.error(f"Search failed: {e}")
        return {}
    print("what the hellllllllll", combined_raw_data)

    # 3. LLM Mapping: Structured Output
    # Hum model ko Context class pass kar rahe hain
    structured_llm = model.with_structured_output(Context)
    contextSch = Context
    prompt = f"""
    Analyze the following search results about the industry and map them to the Context schema {contextSch}.
    If no relevant event is found, set event_name to 'None' and impact_level to 'LOW'.
    
    Search Results:
    {combined_raw_data[:2000]} # Limit tokens
    """
    context_obj = structured_llm.invoke(prompt)
    print(context_obj)
    try:
        # LLM will return an instance of the Context class
        context_obj = structured_llm.invoke(prompt)
       
    
        return {"context": [context_obj]}
    except Exception as e:
        logger.error(f"LLM Mapping failed: {e}")
        return {"context": []}