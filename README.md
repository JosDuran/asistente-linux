# asistente-linux
Asistente linux que te recuerda los comandos que necesites, funciona desde terminal, usa un modelo de Sentence Transformers para emparejar preguntas con respuestas.

0. edit commands.txt as needed
1. docker build -t assistant .
2. docker run -d \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/comandos.json:/app/comandos.json \
  -p 8000:8000 \
  --restart=always \
  assistant

3. sudo cp assistant /usr/local/bin/
4. sudo apt install jq xclip
5. run a query, for example:

prompt: how to generate requirements?

pip freeze > requirements.txt
--------------------------------------------

⏱️  0.02 s  –  📊 Probability: 58.21 %
--------------------------------------------
[The command has been copied to the clipboard]

Language: Python
Library: SentenceTransformer all-MiniLM-L6-v2

Screenshot
![image](https://github.com/user-attachments/assets/86035dd5-ccd4-42f3-8419-8df2c837329e)


