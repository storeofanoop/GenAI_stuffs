# Before starting this code, make sure document should be accessible
# to the code.
# Better to keep it in the same folder with this code.
########################## Preparation Stage ###################

# Install OpenAI
pip3 install openAI

## Install PDF handler library
pip3 install PyPDF2


################ Questions based on PDF ##################

# Import openai and pdf library
import openai
import PyPDF2 as pypdf

#openai.api_key="dsadsadsadsadsad"
openai.api_key=


## Check number of pages and Introduction of the document

# Open the PDF
#filename = list(uploaded.keys())[0]
with open("ING_Bank_additional_pillar_report.pdf", "rb") as f:
    reader = pypdf.PdfReader(f)
    print("Total Pages:", len(reader.pages))

    # Extract text from first page
    page = reader.pages[0]
    text = page.extract_text()
    print(text)

## Check the number of Words/Tokens are there in the document

with open("ING_Bank_additional_pillar_report.pdf", "rb") as f:
    reader = pypdf.PdfReader(f)
    all_text = ""

    # Extract text from all pages
    for page in reader.pages:
        text = page.extract_text()
        if text:  # check in case page has no text
            all_text += text

    # Get length of the text
    print("Total characters in PDF:", len(all_text))
    print("Total words in PDF:", len(all_text.split()))

## Asking multiple questions

Basic_instruction = '''Cover all the questions asked with max token of 350 for each question and try to respond with specific numbers and facts wherever possible.
If you are not sure about the accuracy of the information, just respond that you do not know'''

Question1 = "What are the discolusure requirements changes happened in 2024?"
Question2 = "What are the key points about Credit Quality?"
Question3 = "How ING mitigates Credit Risk?"

prompt1 = (
    Basic_instruction
    + "\n\n"
    + "Questions:\n"
    + "- {0}\n".format(Question1)
    + "- {0}\n".format(Question2)
    + "- {0}\n".format(Question3)
    + "\n\nTranscript:\n{0}".format(all_text)
)

messages=[
        {"role": "user", "content": prompt1}
    ]


chat_response=openai.chat.completions.create(
    model="gpt-4.1-mini",
    max_tokens=1500,
    messages=messages
)

print(chat_response.choices[0].message.content)
