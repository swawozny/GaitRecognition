import json


class ResultSaver:
    @staticmethod
    def save_results_to_file(filename: str, results: dict):
        with open(f"{filename}.json", "w+") as file:
            json.dump(results, file)
