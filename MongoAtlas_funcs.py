import pymongo
from pymongo import MongoClient
from bson import ObjectId
cluster=MongoClient("mongodb+srv://Khalid:Khalid@cluster0.nvgc2.mongodb.net/?retryWrites=true&w=majority")
db = cluster["NLP_Project"]

# defining funcions for the logic:
def GetGenericUsers(db):
    """
    This function takes the database as an input
    This functions outputs all the possible logins for the application
    it output: [[name,password,classid,id]]
    where classid: 1 for manager, 2 for agents, and 3 for users
    """
    gen_all=[]
    collection_manager = db["manager"]
    collection_agents = db["agents"]
    collection_users = db["users"]
    for i in collection_manager.find():
        gen_all.append([i['name'],i['password'],i['generic_users_id'],i['_id']])
    for i in collection_agents.find():
        gen_all.append([i['name'],i['password'],i['generic_users_id'],i['_id']])
    for i in collection_users.find():
        gen_all.append([i['name'],i['password'],i['generic_users_id'],i['_id']])
    return gen_all

# adding reviews
def addreview(db,body,user_id,product_id):
    """
    This funciton takes as input the database , the body of the reply, user_id, and product_id
    it outputs True if everything went without any problems and False otherwise.
    """

    collection_users = db["users"]
    collection_products = db["products"]
    collection_reviews=db['reviews']
    collection_reviews.insert_one({'body':body,'user_id':user_id,'product_id':product_id})
    return True

def getproducts(db,typ=1,agent_id=0):
    """This function takes an input: the database and the type of the generic user 
    so if this is typ: 1 (user) it will output all the products 
    it outputs : list of lists [[produc name, product id]] if user and list of lists [[product name, product id, [[review body, review id]] ]]
    """
    out=list()
    collection_products = db["products"]
    collection_agents=db['agents']
    
    if typ==1:
        for p in collection_products.find():
            out.append([p['name'],p['_id']])
        
    elif typ==2:
        collection_reviews=db['reviews']
        for p in collection_products.find({'agent_id':agent_id}):
            rev=[]
            for r in collection_reviews.find({'product_id':p['_id']}):
                rev.append([r['body'],r['_id']])
            out.append([p['name'],p['_id'],rev])
        
    else:
        raise('you are giving a wrong class for the user')
    return out

def add_reply(db,body,review_id,agent_id):
    """
    This functions takes an input: the database, the body of the reply, the reviewid, and the agent_id
    it adds a reply to a specific review and outputs true if every thing went good and false other wise
    """
    
    collection_replys=db['replys']
    collection_agents=db['agents']
    collection_reviews=db['reviews']
    collection_replys.insert_one({'body':body,'agent_id':agent_id,'review_id':review_id})
    return True
