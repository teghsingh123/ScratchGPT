import scratchattach as scratch3
from groq import Groq
from scratchattach import Encoding
import time
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

key = os.getenv("API_KEY")
username = input("Enter your Scratch username")
password = input("Enter your Scratch password")


session = scratch3.login(username=username, password = password)
conn = session.connect_cloud("1032093853")

time.sleep(20)

while True:
    user_input = scratch3.get_var("1032093853", "ascii prompt")
    if user_input != "":
        break
print(user_input)


def ascii_to_string(input_ascii):
    chunks = [input_ascii[i:i+3] for i in range(0, len(input_ascii), 3)]
    characters = [chr(int(chunk)) for chunk in chunks]
    result_string = ''.join(characters)
    return result_string

user_input = ascii_to_string(user_input)







# for i in range(8):
#     conn.set_var("response" + str(i+1), "")
conn.set_var("response1","")
conn.set_var("response2","")
conn.set_var("response3","")
conn.set_var("response4","")
conn.set_var("response5","")
conn.set_var("response6","")
conn.set_var("response7","")
conn.set_var("response8","")       
conn.set_var("response9","")

#AI CLIENT

client = Groq(
    # This is the default and can be omitted
    api_key=key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "In 100 Words" + user_input,
        }
    ],
    model="llama3-8b-8192",
)

#sets response to the response given by the AI
response = chat_completion.choices[0].message.content

print(response)

#SCRATCH CLIENT

#Convert the string response into binary in order to upload it as a scratch variable
#However, the binary number is way to large to handle, so we have to break it into smaller ones and then put it together in the SCRATCH PROGRAM

def string_to_ascii(input_string):
    """
    Converts a string to its binary representation.
    
    Parameters:
    input_string (str): The string to convert.
    
    Returns:
    str: The binary representation of the string.
    """
    # binary_result = ' '.join(format(ord(char), '08b') for char in input_string)
    # return binary_result

    return " ".join([f"{ord(char):03d}" for char in input_string])

response = string_to_ascii(response)
print(response)


#response = response.replace(" ", "")



response1 = response[:252]
response2 = response[252:504]
response3 = response[504:756]
response4 = response[756:1008]
response5 = response[1008:1260]
response6 = response[1260:1512]
response7 = response[1512:1764]
response8 = response[1764:2016]
response9 = response[2016:2268]


#print(response.replace(" ",""))

#print(response1)
#print(response2)
# print(response3)
# print(response4)
# print(response5)
# print(response6)
# print(response7)
# print(response8)



#print(response1.replace(" ",""))   
#print(response1.replace(" ", ""))






conn.set_var("response1", response1.replace(" ", ""))
conn.set_var("response2", response2.replace(" ", ""))
conn.set_var("response3", response3.replace(" ", ""))
conn.set_var("response4", response4.replace(" ", ""))
conn.set_var("response5", response5.replace(" ", ""))
conn.set_var("response6", response6.replace(" ", ""))
conn.set_var("response7", response7.replace(" ", ""))
conn.set_var("response8", response8.replace(" ", ""))
conn.set_var("response9", response9.replace(" ", ""))