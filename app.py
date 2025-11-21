# # Install required packages before running:
# # pip install langchain streamlit langchain-openai python-dotenv

# import streamlit as st
# from langchain_core.messages import HumanMessage, AIMessage
# from langchain_core.prompts import ChatPromptTemplate
# from dotenv import load_dotenv
# from langchain_nvidia_ai_endpoints import ChatNVIDIA
# from langchain_core.output_parsers import StrOutputParser

# # load_dotenv()

# # Initialize chat history in session state for persistence across runs
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# st.set_page_config(page_title="Ai Bot", page_icon="🤖")
# st.title("Joire AI : RCM Optimization")

# # Function to get AI response from LangChain ChatNVIDIA endpoint with streaming
# def get_response(query, chat_history):
#     template = """ 
#         You are a helpful assistant. Answer the following questions:

#         Chat History: {chat_history}

#         User question: {user_question}
#     """
#     prompt = ChatPromptTemplate.from_template(template)
#     llm = ChatNVIDIA()
#     # Compose the chain (pipe) to generate streamed output string
#     chain = prompt | llm | StrOutputParser()
#     # Stream the response (generator)
#     return chain.stream({
#         "chat_history": chat_history,
#         "user_question": query
#     })

# # Render chat messages from history
# for message in st.session_state.chat_history:
#     if isinstance(message, HumanMessage):
#         with st.chat_message("User"):
#             st.markdown(message.content)
#     else:
#         with st.chat_message("Joire AI"):
#             st.markdown(message.content)

# # User message input
# user_query = st.chat_input("Your Message")

# if user_query and user_query.strip() != "":
#     # Append user message to chat history
#     st.session_state.chat_history.append(HumanMessage(user_query))

#     # Display the user's message
#     with st.chat_message("User"):
#         st.markdown(user_query)

#     # Generate and display AI response with streaming
#     with st.chat_message("Joire AI"):
#         ai_response = st.write_stream(get_response(user_query, st.session_state.chat_history))

#     # Append AI response to chat history after it fully streams
#     st.session_state.chat_history.append(AIMessage(ai_response))
