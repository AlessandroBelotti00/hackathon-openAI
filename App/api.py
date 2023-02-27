import os
import openai
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
print(items)

