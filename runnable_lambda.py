from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

# function to count words
def word_count(text):
    return len(text.split())


# design the prompt
prompt = PromptTemplate(
    template='Write a small joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0.6
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'Generative AI'})

# print(result)

# print in a better format

final_result = """{} \n word count - {} """.format(result['joke'], result['word_count'])

print(final_result)
   