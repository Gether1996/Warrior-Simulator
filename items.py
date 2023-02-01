from serializable import Serializable
import json
import random


class Item(Serializable):

    def __init__(self):
        self.m_item_id = ...
        self.m_type = ...
        self.m_name = ...

    def save_object(self):
        pass

    def load_object(self, data):
        pass


class Armor(Item):

    def __init__(self):
        super().__init__()
        self.m_armor_value = ...

    def load_object(self, data):
        self.m_item_id = data['m_item_id']
        self.m_type = data['m_type']
        self.m_name = data['m_name']
        self.m_armor_value = data['m_armor_value']

    def __str__(self):
        return self.m_name


class ItemManager:

    def __init__(self):
        self.m_items = []

    def load_items_from_json(self):
        f = open('armors.json')
        data_from_json = json.loads(f.read())
        for itemData in data_from_json['armors']:
            armor = Armor()
            armor.load_object(itemData)
            self.m_items.append(armor)

    def get_item_name_by_its_id(self, m_item_id):
        for item in self.m_items:
            if item.m_item_id == m_item_id:
                return item.m_name

    def get_armor_id1_50percent_chance(self):
        if random.randint(1, 100) <= 50:
            for item in self.m_items:
                if item.m_item_id == 1:
                    return item.m_name



