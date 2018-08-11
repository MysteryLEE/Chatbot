import spacy
#nlp = spacy.load('en_core_web_md')
nlp = spacy.load('en_core_web_sm')

def entity_type(word):
    corporations=['Facebook','GE','Apple','Advanced Micro Devices, Inc.','GPRO','Twitter, Inc.','NFLX','AMZN','Microsoft','NVIDIA','BABA','Tesla, Inc.','Micron Technology','The Walt Disney Co.','Cronos Group, Inc.']
    _type=None
    if word.text in corporations:
        _type='OPR'
    return _type



def extractent(message):
    doc=nlp(message)
    ents=doc.ents #提出实体，并作为一个全是实体的元组返回   他是存储句子所有实体的元组  ?加入过了新的实体
    for ent in ents:
        if entity_type(ent)=='OPR':
            return ent.text
        break





