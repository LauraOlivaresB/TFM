import sys
from yachalk import chalk
sys.path.append("..")

import json
import ollama.client as client


def extractConcepts(prompt: str, metadata={}, model="mistral-openorca:latest"):
    SYS_PROMPT = (
        "Your task is extract the key concepts (and non personal entities) mentioned in the given context. "
        "Extract only the most important and atomistic concepts, if  needed break the concepts down to the simpler concepts."
        "Categorize the concepts in one of the following categories: "
        "[event, concept, place, object, document, organisation, condition, misc]\n"
        "Format your output as a list of json with the following format:\n"
        "[\n"
        "   {\n"
        '       "entity": The Concept,\n'
        '       "importance": The concontextual importance of the concept on a scale of 1 to 5 (5 being the highest),\n'
        '       "category": The Type of Concept,\n'
        "   }, \n"
        "{ }, \n"
        "]\n"
    )
    response, _ = client.generate(model_name=model, system=SYS_PROMPT, prompt=prompt)
    try:
        result = json.loads(response)
        result = [dict(item, **metadata) for item in result]
    except:
        print("\n\nERROR ### Here is the buggy response: ", response, "\n\n")
        result = None
    return result


def graphPrompt(input: str, metadata={}, model=None):
    if model == None:
        model = "mistral-openorca:latest"

    # model_info = client.show(model_name=model)
    # print( chalk.blue(model_info))

    SYS_PROMPT = (
        "You are a pharmaceutical knowledge graph creator tasked with extracting pharmacological interactions from articles. This articles are chunked."
        "You will be provided with a context chunk, delimited by triple backticks (```). Your goal is to identify the ontology of pharmacs and their interactions."
        "Consider the following thoughts while processing the context:\n"
        "Thought 1: While analyzing each sentence, focus on key terms related to pharmacological interactions. Consider terms such as 'Drugs', 'pharmacokinetics (PK)', 'pharmacodynamics (PD)', 'pharmacogenetics (PG)', diseases.\n"
        "\tTry to break down terms into atomic components.\n\n"
        "Thought 2: Explore how these drugs interacts between them with expresions such as the interaction of drug and drug, interacts with,potential interaction between, can affect the metabolism of, enhances the effects of, may potentiate the effects of.\n"
        "\tTerms mentioned in the same sentence or paragraph are likely related.\n"
        "\tTerms can have multiple relationships with other terms.\n\n"
        "Thought 3: Determine the interactions between pairs of terms.\n\n"
        "When extracting properties such as 'Type of Interaction,' 'Severity,' 'Gender,' and 'Pregnancy,' pay attention to expressions like:\n"
        "- 'Type of Interaction': Look for phrases indicating the nature of the interaction, e.g., 'synergistic,' 'antagonistic,' 'additive.'\n"
        "- 'Severity': Identify words conveying the intensity or seriousness of effects, e.g., 'severe,' 'mild,' 'moderate.'\n"
        "- 'Gender': Seek terms indicating the gender specificity of interactions, e.g., 'male,' 'female.'\n"
        "- 'Pregnancy': Recognize language discussing the impact of interactions on pregnancy, e.g., 'safe for pregnant individuals,' 'contraindicated during pregnancy.'\n\n"
        "Format your output as a list of JSON objects. Each element in the list should represent a pair of terms and the interaction between them. For example:\n"
        "[\n"
    "   {\n"
    '       "node_1": "Drug",\n'
    '       "node_2": "Drug",\n'
    '       "edge": "HAS_INTERACTION",\n'
    '       "properties": {\n'
    '           "type": "Synergistic",\n'
    '           "severity": "High",\n'
    '           "gender": "Differential Dosages for Males and Females",\n'
    '           "pregnancy": Safe for use during pregnancy,\n'
    '           "contraindications": "History of Heart Disease",\n'
    '           "adverse_effects": "Gastrointestinal Irritation"\n'
    '       }\n'
    "   },\n"
    "   {\n"
    '       "node_1": "Drug",\n'
    '       "node_2": "Disease",\n'
    '       "edge": "HAS_INTERACTION",\n'
    '       "properties": {\n'
    '           "type": "Synergistic",\n'
    '           "severity": "High",\n'
    '           "gender": "Differential Dosages for Males and Females",\n'
    '           "pregnancy": Safe for use during pregnancy,\n'
    '           "contraindications": "History of Heart Disease",\n'
    '           "adverse_effects": "Gastrointestinal Irritation"\n'
    '       }\n'
    "   }\n"
    "]"
    )

    USER_PROMPT = f"context: ```{input}``` \n\n output: "
    response, _ = client.generate(model_name=model, system=SYS_PROMPT, prompt=USER_PROMPT)
    try:
        result = json.loads(response)
        result = [dict(item, **metadata) for item in result]
    except:
        print("\n\nERROR ### Here is the buggy response: ", response, "\n\n")
        result = None
    return result
