# asistente-linux
Asistente linux que te recuerda los comandos que necesites, funciona desde terminal, usa un modelo de Sentence Transformers para emparejar preguntas con respuestas.

0. Editar commands.txt segun su necesidad
1. docker build -t assistant .
2. docker run -d \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/comandos.json:/app/comandos.json \
  -p 8000:8000 \
  --restart=always \
  assistant

3. sudo cp assistant /usr/local/bin/
4. sudo apt install jq xclip
5. dele una pregunta al asistente, por ejemplo:

prompt: como genero el requirements?

pip freeze > requirements.txt
--------------------------------------------

⏱️  0.02 s  –  📊 Probability: 58.21 %
--------------------------------------------
[The command has been copied to the clipboard]

Language: Python
Library: SentenceTransformer all-MiniLM-L6-v2

Screenshot

![image](https://github.com/user-attachments/assets/2a80317d-081d-408a-a07e-82f48734f511)



