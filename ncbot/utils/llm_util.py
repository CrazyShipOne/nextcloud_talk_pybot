from ncbot.utils.history import history_util
from ncbot.utils.prompt_config import default_history_template
from langchain.chains import ConversationChain


def get_user_chat_response(llm,userid, input):
    history = history_util.get_memory(userid)
    llm_chain = ConversationChain(llm=llm, memory = history, verbose=False, prompt=default_history_template)
    response = llm_chain.predict(input=input)
    history_util.save_memory(userid, history)
    return response