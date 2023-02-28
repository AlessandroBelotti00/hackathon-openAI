import os
import openai
import re
openai.organization = "org-Qbmwr4JuTIH5YCgjktHYrLBE"
openai.api_key = "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"

gpt_prompt = "what is the complete syllabus of Mathematics in the second year of primary school?"


response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=gpt_prompt,
  temperature=0.5,
  max_tokens=1024,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)


items = response['choices'][0]['text']

bull_list_re = re.compile('(.+)[:]')  # extract only the bullet list
bull_list = bull_list_re.search(items).group(1)

bull_list = items.replace(bull_list + ":",'')  # remove the first part of the api response (take only the items in the list)

list_item = bull_list.split("•")
split_list = [item.split("-") for item in list_item]
for i in list_item:
  
  i_re = re.compile('.+') # check if the item doesn't contain only '\n' characters
  if i_re.search(i) is not None:
    gpt_prompt = "Tell me a complete explanation about the concept of " + i.strip("\n ")
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=gpt_prompt,
      temperature=0.5,
      max_tokens=1024,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    print(gpt_prompt+'\n')
    print(response['choices'][0]['text'] )

    name_file = i.strip("\n ")
    fileObject = open("../Example/"+name_file+".txt", "w")
    fileObject.write(response['choices'][0]['text'] + '\n')

    gpt_prompt = "Create 10 exercises with solutions about " + i.strip("\n ")
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=gpt_prompt,
      temperature=0.5,
      max_tokens=1024,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )

    print(gpt_prompt+'\n')
    print(response['choices'][0]['text'] )

    fileObject.write(response['choices'][0]['text'] + '\n')
    fileObject.close() 



