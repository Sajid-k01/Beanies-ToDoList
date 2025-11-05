import json

filename = "storage.json"

def WriteToStorage(id, desc, category):

    newTask = {
        "id" : id,
        "description" : desc,
        "category" : category
    }

    with open(filename, 'r+') as file:
        fileData = json.load(file)

        fileData["tasks"].append(newTask)

        file.seek(0)

        try:
            json.dump(fileData, file, indent=4)
        except Exception as e:
            print(e)
            

WriteToStorage("4", "Yessir", "High")