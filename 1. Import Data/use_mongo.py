import os
from pymongo import MongoClient

mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017')

client = MongoClient(mongo_uri)
db = client.myloProdServer

# find: if you just want to find some document without any calculation or change  
find_data = list(
            db.collection.find(
                {
                    # match part
                    "user_id": "1234", 
                },
                {
                    # project part
                    "_id": 1,
                    "data": 1
                },
            )
        )

# aggregate
aggregate_data = list(
            db.collection.aggregate([
                {
                    "$match": {
                        "$eq": [
                            "user_id", "1234"
                        ]
                    }
                },
                {
                    "$project": {
                        "user_id": "$_id",
                        "data": "$detail.data"
                    }
                }
            ]
        )
    )
