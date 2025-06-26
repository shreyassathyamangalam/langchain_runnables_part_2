from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence
from dotenv import load_dotenv

load_dotenv()

# define prompt 1

prompt_1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt_2 = PromptTemplate(
    template='Generate a LinkedIn post about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0.7
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt_1, model, parser),
    'linkedin': RunnableSequence(prompt_2, model, parser)
})

result = parallel_chain.invoke({'topic':'Generative AI'})

# print(result) Result is in the form of a dictionary

print(result['tweet'])
print(result['linkedin'])
