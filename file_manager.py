import json
import os

class FileManager:
    FILE_NAME = "results.json"

    @staticmethod
    def save_result(result):
        data = []

        if os.path.exists(FileManager.FILE_NAME):
            with open(FileManager.FILE_NAME, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except:
                    data = []

        data.append(result)

        with open(FileManager.FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
