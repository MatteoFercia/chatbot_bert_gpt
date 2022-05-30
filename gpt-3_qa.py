from create_input_file import input_file
import openai
openai.api_key = "API"

response = openai.Answer.create(
 search_model="ada",
 model="text-davinci-002",
 question="When can I enter in the room?",
 documents=input_file,
 examples_context="In 2017, U.S. life expectancy was 78.6 years.",
 examples=[["What is human life expectancy in the United States?","78 years."]],
 max_tokens=20,
 stop=["\n", "<|endoftext|>"],
)



if __name__ == '__main__':

 print(response)
