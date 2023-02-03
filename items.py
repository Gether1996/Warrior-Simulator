from serializable import Serializable
import json
import random


class Item(Serializable):

    def __init__(self):
        self.m_item_id = ...
        self.m_type = ...
        self.m_name = ...

    def save_object(self):
        data = {
            "m_item_id": self.m_item_id,
            "m_type": self.m_type,
            "m_name": self.m_name
        }
        return data

    def load_object(self, data):
        self.m_item_id = data['m_item_id']
        self.m_type = data['m_type']
        self.m_name = data['m_name']


class Armor(Item):

    def __init__(self):
        super().__init__()
        self.m_armor_value = ...

    def save_object(self):
        data = {
            "m_armor_value": self.m_armor_value
        }
        parentData = super().save_object()
        data.update(parentData)
        return data

    def load_object(self, data):
        Item.load_object(self, data)
        self.m_armor_value = data['m_armor_value']


class Weapon(Item):

    def __init__(self):
        super().__init__()
        self.m_damage_lower = ...
        self.m_damage_upper = ...

    def save_object(self):
        data = {
            "m_damage_lower": self.m_damage_lower,
            "m_damage_upper": self.m_damage_upper
        }
        parentData = super().save_object()
        data.update(parentData)
        return data

    def load_object(self, data):
        Item.load_object(self, data)
        self.m_damage_lower = data['m_damage_lower']
        self.m_damage_upper = data['m_damage_upper']


class ItemManager:

    def __init__(self):
        self.m_items = []

    def load_items_from_json(self):
        f = open('armors.json')
        armor_data_from_json = json.loads(f.read())
        for itemData in armor_data_from_json['armors']:
            armor = Armor()
            armor.load_object(itemData)
            self.m_items.append(armor)

        g = open('weapons.json')
        weapon_data_from_json = json.loads(g.read())
        for itemData in weapon_data_from_json['weapons']:
            weapon = Weapon()
            weapon.load_object(itemData)
            self.m_items.append(weapon)

    def get_item_name_by_its_id(self, m_item_id):
        for item in self.m_items:
            if item.m_item_id == m_item_id:
                return item.m_name

    def generate_spawning_armor(self):
        if random.randint(1, 100) <= 50:
            for item in self.m_items:
                if item.m_item_id == 2:
                    return item
        else:
            for item in self.m_items:
                if item.m_item_id == 1:
                    return item

    def add_random_weapon_kek(self):
        random_wep = random.choice(self.m_items[8:])
        return random_wep
