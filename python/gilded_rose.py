# -*- coding: utf-8 -*-

class GildedRose(object):
    def __init__(self, items):
        self.items = items
        self.BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
        self.AGED_BRIE = "Aged Brie"
        self.SULFURAS = "Sulfuras, Hand of Ragnaros"
        self.CONJURED = "Conjured"
        self.MAX_QUALITY = 50
        self.MIN_QUALITY = 0
        self.MIN_SELLIN = 0
        self.BACKSTAGE_HIGH_SELLIN_VALUE = 11
        self.BACKSTAGE_LOW_SELLIN_VALUE = 6

    def handle_aged_brie(self, item):
        if item.quality < self.MAX_QUALITY:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < self.MIN_SELLIN and item.quality < self.MAX_QUALITY:
            item.quality += 1

    def handle_backstage(self, item):
        if item.quality < self.MAX_QUALITY:
            item.quality += 1
            if item.sell_in < self.BACKSTAGE_HIGH_SELLIN_VALUE:
                item.quality += 1
                if item.sell_in < self.BACKSTAGE_LOW_SELLIN_VALUE:
                    item.quality += 1
        item.sell_in -= 1
        if item.sell_in < self.MIN_SELLIN:
            item.quality -= item.quality

    def handle_conjured(self, item):
        if item.sell_in > self.MIN_SELLIN:
            item.quality -= 2
        else:
            item.quality -= 4

    def handle_default(self, item):
        if item.quality > self.MIN_QUALITY:
            item.quality -= 1
        if item.sell_in < self.MIN_SELLIN and item.quality > self.MIN_QUALITY:
            item.quality -= 1
        item.sell_in -= 1

    def update_quality(self):
        for item in self.items:
            if item.name == self.AGED_BRIE:
                self.handle_aged_brie(item)
            elif item.name == self.CONJURED:
                self.handle_conjured(item)
            elif item.name == self.BACKSTAGE:
                self.handle_backstage(item)
            elif item.name != self.SULFURAS:
                self.handle_default(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
