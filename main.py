from flask import Flask, render_template, request, redirect, url_for
import scratchattach as scratch3
from groq import Groq
from dotenv import load_dotenv
import os
import time

load_dotenv()

app = Flask(__name__)

key = os.getenv("API_KEY")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        project_id = request.form['project_id']
        api_key = request.form['api_key']
        
        session = scratch3.login(username=username, password=password)
        conn = session.connect_cloud(project_id)
        
        time.sleep(20)
        
        while True:
            user_input = scratch3.get_var(project_id, "ascii prompt")
            if user_input != "":
                break
        print(user_input)
        
        def ascii_to_string(input_ascii):
            chunks = [input_ascii[i:i+3] for i in range(0, len(input_ascii), 3)]
            characters = [chr(int(chunk)) for chunk in chunks]
            result_string = ''.join(characters)
            return result_string
        
        user_input = ascii_to_string(user_input)
        
        conn.set_var("response1", "")
        conn.set_var("response2", "")
        conn.set_var("response3", "")
        conn.set_var("response4", "")
        conn.set_var("response5", "")
        conn.set_var("response6", "")
        conn.set_var("response7", "")
        conn.set_var("response8", "")       
        conn.set_var("response9", "")
        
        client = Groq(api_key=api_key)
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "In 100 Words" + user_input,
                }
            ],
            model="llama3-8b-8192",
        )
        
        response = chat_completion.choices[0].message.content
        print(response)
        
        def string_to_ascii(input_string):
            return " ".join([f"{ord(char):03d}" for char in input_string])
        
        response = string_to_ascii(response)
        print(response)
        
        response1 = response[:252]
        response2 = response[252:504]
        response3 = response[504:756]
        response4 = response[756:1008]
        response5 = response[1008:1260]
        response6 = response[1260:1512]
        response7 = response[1512:1764]
        response8 = response[1764:2016]
        response9 = response[2016:2268]
        
        conn.set_var("response1", response1.replace(" ", ""))
        conn.set_var("response2", response2.replace(" ", ""))
        conn.set_var("response3", response3.replace(" ", ""))
        conn.set_var("response4", response4.replace(" ", ""))
        conn.set_var("response5", response5.replace(" ", ""))
        conn.set_var("response6", response6.replace(" ", ""))
        conn.set_var("response7", response7.replace(" ", ""))
        conn.set_var("response8", response8.replace(" ", ""))
        conn.set_var("response9", response9.replace(" ", ""))
        
        return "Login successful and responses set."
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
