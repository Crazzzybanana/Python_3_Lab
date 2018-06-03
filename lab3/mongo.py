import pickle

from pymongo import MongoClient
from tqdm import tqdm
from db import MONGO_URL


def mongo_data():
    client = MongoClient(MONGO_URL)
    messages = []
    for d in tqdm(client.lab_2.data.find()):
        messages.append(d['message'])
    with open("messages", "wb") as file:
        pickle.dump(messages, file)
    return messages
