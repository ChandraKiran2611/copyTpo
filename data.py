from fileinput import filename
import pymongo
import pandas as pd
if __name__ == "__main__":
    print("welcome!!!!!!!!")
    uri = "mongodb://localhost:27017/";
    client = pymongo.MongoClient(uri)
    print(client)
    mydb = client["nsrit"]
    info = mydb["details"]
roll = 0
file ="/Users/mr.chandu/Desktop/Project/flask_mongo/sampleSpread.xlsx"
excel_file = pd.read_excel(file,sheet_name="cse")
csv_str = excel_file.to_dict('records')
#print(csv_str)
#info.insert_many(csv_str).format()


ans = info.find_one()
print(ans)