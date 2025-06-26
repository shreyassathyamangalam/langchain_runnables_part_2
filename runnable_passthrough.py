from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

# design the prompt
prompt_1 = PromptTemplate(
    template='Write a small joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0.6
)

parser = StrOutputParser()

prompt_2 = PromptTemplate(
    template='Explain the following joke in a succinct manner \n {text}',
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt_1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explaination': RunnableSequence(prompt_2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'Generative AI'})

print(result)
