from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.examples

def porsche_query():
    autos = db.autos.find({"manufacturer":"Porsche"})
    query = {}
    for a in autos:
        query.append(a)
    num_autos = db.myautos.find().count()
    return query, num_autos

    # To insert the data
def insert_autos(infile, db):
    data = process_file(infile)
    db.autos.insert(data)

    # to import file to another file
mongoimport -d dbname -c collectionname --file input-file.json

    # inequality commands: $gt >, $lt <, $gte >=, $lte <=, $ne !=
    # to find all cities with population >= 250000:
    query = {"population" : {"$gt" : 250000}}
    # or cities that begin with X:
    query = {"name" : {"$gt" : "X", "$lt" : "Y"}}
    cities = db.cities.find(query)
    # to count, add .count(), to make the output look more structured, add .pretty()
    # to search by existance of a field, query = {"field" : {"exist" : 1}} or 0 for non existing field
    db.cities.find({"motto" : {"$regex" : "[Ff]riendship | [Pp]ride"}} # will find cities in field "Motto" of which is going to present words friendship or pride starting with lower or upper case
    """MongoDB also looks inside an array for a value, AND values themselves can be an array with preseiding "$in" to match at least one of them. "$all" is to match all"""
    # to add a field and value to one entity:
    city = db.cities.find_one({"name" : "Munchen", "country" : "Germany"})
    city["isoCountryCode"] = "DEU"
    db.cities.save(city)
    # OR
    city = db.cities.update({"name" : "Munchen", "country" : "Germany"},
                            {"$set" : {"isoCountryCode" : "DEU"}}) # and "$unset" : {"field" : ""} to delete one
    # to modify all cities with country field Germany, add multi=True

    # removing documents works same as .find(), but gotta put .remove()


                   ###WHO TWEETED THE MOST / Pipeline = []

    #Group tweets by user
    # Count each tweet
    # Sort into descending order
    # Select user at the top
def most_tweets():
    result = db.tweets.aggregate([{"$group" : {"_id" : "$user.screen_name", #groups tweets by user's screen_name under user ("_id" is mandatory)
                                               "count" : {"$sum" : 1}}}, # counts in 1 increment grouped items
                                  {"$sort" : {"count" : -1}}]) #sort in descending order

                ### THE HIGHEST FOLLOWER-FOLLOWERS RATIO / Match and Project

def highest_ratio():
    result = db.tweets.aggregate([
        {"$match" : {"user.friends_count": {"$gt": 0},
                     "user.followers.count": {"$gt": 0}}},#works like .find()
        {"$project":{"ratio": {"$divide":["$user.followers_count", "$user.friends_count"]},
                    "screen_name": "$user.screen_name"}},#decide which field will be passed along to the next stage (include, create, rename or insert computed fields)
        {"$sort": {"ratio":-1}},
        {"$limit": 1}])#if we need only one username
                   # more about project operators: https://docs.mongodb.com/manual/reference/operator/aggregation/project/#pipe._S_project


        ### WHICH DISTRICT HAS MOST CITIES (each city has flield "part of" the 1 district or more) / Unwind

def district_pipeline():
    pipeline = [{"$unwind" : "$isPartOf"},
                {"$group" : {"_id":"$isPartOf", "count" : {"$sum" : 1}}},
                {"$sort":{"count":-1}},
                {"$limit":1}]

            ### Add to Set
def unique_hashtags_by_user():
    result = db.tweets.aggregate([
        {"$unwind":"$entities.hashtags"},
        {"$group":{"_id":"$user.screen_name",
                   "unique_hashtags":{"$addToSet": "$entities.hashtags.text"}}}])

            # $PUSH
            # Using an aggregation query, count the number of tweets for each user. In the same $group stage, 
            # use $push to accumulate all the tweet texts for each user. Limit your output to the 5 users
            # with the most tweets.
def make_pipeline():
    pipeline = [{"$group" : {"_id":"$user.screen_name", "count" : {"$sum" : 1}, "tweet_texts":{"$push":"$text"}}},
                {"$sort":{"count":-1}},
                {"$limit":5}]
    return pipeline


            ### MULTIPLE STAGES *** 
            # show 10 users who mentioned the most unique users in their tweets
                   #  https://classroom.udacity.com/courses/ud032/lessons/760758686/concepts/7842387560923

def unique_user_mentions():
    result = db.tweets.aggregate([
        {"$unwind":"$entities.user_mentions"},#generates 1 document for every user mention
        {"group":{
            "_id":"$user.screen_name",
            "mset":{"$addToSet":"$entities.user_mentiones.screen_name"}}}, #accumulates an array (list) of usernames mentioned by "_id" user (for every user)
        {"$unwind":"$mset"},# unwind to count unique user_mentions
        {"$group":{"_id":"$_id", "count":{"$sum":1}}}, # counts them
        {"$sort":{"count":-1}},
        {"$limit":10}])

                   ## QUIZZ
                   ## What is the average city population for a region in India? Calculate your answer by first 
                    # finding the average population of cities in each region and then by calculating the average of the regional averages.

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    pipeline = [{"$match":{"country":"India"}},
                {"$unwind" : "$isPartOf"},
                {"$group" : {"_id":"$isPartOf", "dist_avg":{"$avg":"$population"}}},
                {"$group":{"_id":"India Regional City Population Average", "avg" :{"$avg":"$dist_avg"}}}]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]


