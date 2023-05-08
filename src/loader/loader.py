import os
import re

from src.model.dataset import Dataset
from src.model.person import Person
from src.model.sequence import Sequence


class DatasetLoader:
    def __init__(self, dataset_path: str):
        self.__path = dataset_path
        self.__dataset = self.load_dataset(dataset_path)

    def get_dataset(self):
        return self.__dataset

    def load_dataset(self, path):
        dataset = Dataset()
        dataset.persons = []

        dataset_dict = dict()

        for entry in os.listdir(path):
            samples_path = os.path.join(path, entry)
            if not entry.startswith('.'):
                desc = re.match(r"p(?P<person>\d+)s(?P<sample>\d+)", entry)
                person = desc["person"]
                sample = desc["sample"]

                if person not in dataset_dict:
                    dataset_dict[person] = dict()

                dataset_dict[person][sample] = samples_path

        for idx in dataset_dict.keys():
            person = Person()
            person.id = idx
            person.sequences = []

            for sample in dataset_dict[idx].keys():
                seq = Sequence()
                seq.seq_id = sample
                seq.path = dataset_dict[idx][sample]

                person.sequences.append(seq)

            dataset.persons.append(person)

        return dataset
