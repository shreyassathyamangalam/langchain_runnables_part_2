from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

# design the prompt
prompt_1 = PromptTemplate(
    template='Write a small joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0.4
)

parser = StrOutputParser()

prompt_2 = PromptTemplate(
    template='Explain the following joke in a succinct manner \n {text}',
    input_variables=['text']
)

chain = RunnableSequence(prompt_1, model, parser, prompt_2, model, parser)

result = chain.invoke({'topic':'Artifical Intelligence'})

print(result)
