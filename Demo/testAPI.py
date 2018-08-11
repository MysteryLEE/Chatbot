import requests
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
import extractopent


# Create a trainer
trainer = Trainer(config.load("/Users/siliguo/rasa_nlu/sample_configs/config_spacy.yml"))

# Load the training data
training_data = load_data('/Users/siliguo/Desktop/UCR/GRE/Chatbot/Project/demo-rasa.json')

# Create an interpreter by training the model
interpreter = trainer.train(training_data)



def handleapi(url):    #提取API变成一个字典的函数
    r=requests.get(url)
    #print("status code:",r.status_code)
    response_dict=r.json()
    return response_dict

def respond(message,url):   #用提取函数构造一个回答的函数
    # Extract the entities
    entities = interpreter.parse(message)["entities"]
    #print(entities)
    for ent in entities:
        #print(type(ent))   #我去看ent究竟是什么东西的代码，没有实际作用print(ent,'my entity')
        #print()
        enti = ent['value']
    apidict=handleapi(url)
    return apidict[enti]



#print(respond('I want to know high stock of Facebook','https://api.robinhood.com/fundamentals/FB/'))
#print(respond('I want to know description of Facebook','https://api.robinhood.com/fundamentals/FB/'))


def respondI(message):       #分支回答
    enti=extractopent.extractent(message)
    if enti=='Facebook':
        return respond(message,'https://api.robinhood.com/fundamentals/FB/')
    #添加有关其他公司的分支，以及修改json
    elif enti=='Apple':
        return respond(message,'https://api.robinhood.com/fundamentals/AAPL/')
    elif enti=='GE':
        return respond(message,'https://api.robinhood.com/fundamentals/GE/')
    elif enti=='Advanced Micro Devices, Inc.':
        return respond(message,'https://api.robinhood.com/fundamentals/AMD/')
    elif enti=='GPRO':
        return respond(message,'https://api.robinhood.com/fundamentals/GPRO/')
    elif enti=='Twitter, Inc.':
        return respond(message,'https://api.robinhood.com/fundamentals/TWTR/')
    elif enti=='NFLX':
        return respond(message,'https://api.robinhood.com/fundamentals/NFLX/')
    elif enti=='AMZN':
        return respond(message,'https://api.robinhood.com/fundamentals/AMZN/')
    elif enti=='Microsoft':
        return respond(message,'https://api.robinhood.com/fundamentals/MSFT/')
    elif enti=='NVIDIA':
        return respond(message,'https://api.robinhood.com/fundamentals/NVDA/')
    elif enti=='BABA':
        return respond(message,'https://api.robinhood.com/fundamentals/BABA/')
    elif enti=='Tesla, Inc.':
        return respond(message,'https://api.robinhood.com/fundamentals/TSLA/')
    elif enti=='Micron Technology':
        return respond(message,'https://api.robinhood.com/fundamentals/MU/')
    elif enti=='The Walt Disney Co.':
        return respond(message,'https://api.robinhood.com/fundamentals/DIS/')
    elif enti=='Cronos Group, Inc.':
        return respond(message,'https://api.robinhood.com/fundamentals/CRON/')






#print(respondI('I want to know description of Facebook'))
#print(respondI('Can you tell me the business sector of Cronos Group, Inc.'))
#print(respondI('Would you like to show me the total volume of Cronos Group, Inc.'))
#print(respondI('I want to know high stock of Facebook'))


