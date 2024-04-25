from langchain_core.prompts import PromptTemplate

default_history_template_str = """
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know. If it knows, just answer the question once. But do output 1 round for current conversation, not more.

Current conversation:
{history}
Human: {input}
AI:
"""

default_history_template = PromptTemplate(template= default_history_template_str, input_variables=["history","input"])