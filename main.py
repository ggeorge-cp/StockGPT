import openai

TWITTER_API_KEY = 'zeBQwSp2Jbs0bjO04ZIZnB07U'
TWITTER_SECRET_KEY = 'NTmuN1QIg4kMe4Kzcn6r9Pgk8sHE4kapfE0gejmiqOaHkqBnHV'
TWITTER_BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAB%2F8nQEAAAAAKks5%2Bn9bRpLK03AZryM%2FjMhs9UE%3Dhm7gXI7SJ7aelD805OA9zL7NwkmdKOPrNMbLTKzlR5WVFnoUTc'
GPT_SECRET_KEY = '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'
openai.api_key = GPT_SECRET_KEY

def get_completion(prompt, model="gpt-3.5-turbo",temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

if __name__ == '__main__':
    ticker = "PANW"

    prompt = f"""
    Please translate the following ticker symbol, delimited by triple backticks, /
    into the full company name. 
     
     Ticker Symbol: ```{ticker}```
    
    Please just return the company name, and do not include any other text.
    
    Please remove any of the strings in the following list from /
    the full company name:
    
    list = ['Inc.','Ltd.','LLC', 'Co.', 'Corp.', 'GmbH', 'S.A.', 'Pte. Ltd.', 'Incorp.', 'LLP']  
    
    """

    response = get_completion(prompt)
    print(response)