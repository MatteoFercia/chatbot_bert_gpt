from create_input_file import input_file
import csv
import openai
openai.api_key = "api"

diz_qa_gpt_3 = {}

class Responder:
 def __init__(self):
  pass

 def answer_to(self, question):
  response = openai.Answer.create(
   search_model="ada",
   model="text-davinci-002",
   question=question,
   documents=input_file,
   examples_context="Stanza Semplice® pays particular attention to environmental issues and energy saving.For this reason, he is confident that all students belonging to the Stanza Semplice® Club will embrace and share this important ethical principle.We ask all our tenants to carry out the separate collection in a correct and conscious way, following all the instructions you will receive from your Apartment Manager.Properly sorting waste is the responsibility and obligation of each individual tenant, all of which is regulated by municipal and national laws.Any penalties deriving from inappropriate use of separate waste collection are the responsibility of all tenants.However, we ask you to pay particular interest and attention to this issue, informing yourself in advance with your Apartment Manager upon entering your room.",
   examples=[["What can I do if I not have a tax code?",
              "Italian law requires the unique identification code, also called the tax code, to formalize a lease agreement. Every citizen, whether Italian or foreign, must possess it for tax reasons. That why is essential you have the tax code. Read below how to obtain it: - Through the Revenue Agency You can physically go to an office of the Revenue Agency with identification documents (identity card/passport with visa/residence permit). To avoid wasting time, we recommend calling the local office closest to you to receive confirmation. Depending on the agency of reference,  you will be able to make an appointment or not."]],
   max_tokens=20,
   stop=["\n", "<|endoftext|>"])
  with open('results_qa', 'a') as f:
   writer = csv.writer(f)
   writer.writerow([question, response["answers"]])
  return response

if __name__ == '__main__':

 qa = Responder()
 qa.answer_to("How do I choose the city area?")