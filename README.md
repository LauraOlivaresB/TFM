## This project
Here I have created my master thesis. The automatization of the identification of drug-drug interactions and the creation of a interface where you can interact with the database that is created on Neo4j but local, so is not available all the time.

This is the main notebook https://github.com/LauraOlivaresB/TFM/blob/main/extract_graph.ipynb to execute

But before generating this code, is important to install Ollama in the terminal and run ollama zephyr. Also to activate the enviroment https://github.com/LauraOlivaresB/TFM/blob/main/environment.yml then you are ready to use the code.

It's already with only one document in the folder cureus2 in format .txt but here is where you can put more documents if you need, the only thing is that you need a really good machine because is slow. In the line [10] there is this line df=df[1:20] this should be changed if you want to process all the document.

All the components I used here are set up locally, so this project can be run very easily on a personal machine. I have adopted a no-GPT approach here to keep things economical. I am using the fantastic Mistral 7B openorca instruct, which crushes this use case wonderfully. The model can be set up locally using Ollama so processing the documents is basically free (No calls to GPT).

---
## Tech Stack

### Ollama
<a href="https://ollama.ai"><img src='https://github.com/jmorganca/ollama/assets/3325447/0d0b44e2-8f4a-4e99-9b52-a5c1c741c8f7 ' height='50'/></a>

Ollama makes it easy to host any model locally. Mistral 7B OpenOrca version is already available with Ollama to use out of the box. 

To set up this project, you must install Ollama on your local machine. 

Step 1: Install Ollama https://ollama.ai

Step 2: run `ollama run zephyr` in your terminal. This will pull the zephyr model to your local machine and start the Ollama server.

### Pandas 
dataframes for graph schema (can use a graphdb at a later stage).




