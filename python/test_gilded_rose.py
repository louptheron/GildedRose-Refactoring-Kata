# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_should_return_update_item(self):
        # Given
        quality = 10
        expected_quality = 9
        items = [Item("foo", 1, quality)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(("foo", 0, expected_quality),
            (items[0].name, items[0].sell_in, items[0].quality))

    def test_when_sellin_is_positive_quality_decrease_from_one(self):
        # Given
        quality = 1
        expected_quality = quality - 1
        items = [Item("foo", 1, quality)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(expected_quality, items[0].quality)

    def test_when_sellin_is_negative_quality_decrease_twice_as_fast(self):
        # Given
        quality = 10
        expected_quality = quality - 1 * 2
        items = [Item("foo", -1, quality)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(expected_quality, items[0].quality)

    def test_quality_cant_be_negative(self):
        # Given
        quality = 0
        expected_quality = quality
        items = [Item("foo", 2, quality)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(expected_quality, items[0].quality)

    def test_aged_brie_increase_in_quality_the_older_it_gets(self):
        # Given
        quality = 2
        expected_quality = quality + 1
        items = [Item("Aged Brie", 2, quality)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(expected_quality, items[0].quality)

    def test_aged_brie_increase_in_quality_when_sellin_is_negative(self):
        # Given
        quality = 2
        expected_quality = quality + 2
        items = [Item("Aged Brie", -2, quality)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(expected_quality, items[0].quality)

    # TODO: Fix quality check if already > 50
    def test_quality_of_item_cant_exceed_50(self):
        # Given
        quality = 50
        expected_quality = quality
        items = [Item("Aged Brie", 2, quality)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(expected_quality, items[0].quality)

    def test_sulfuras_should_never_be_sold_or_decrease_in_quality(self):
        # Given
        quality = 2
        expected_quality = quality
        sell_in = 3
        expected_sell_in = sell_in

        items = [Item("Sulfuras, Hand of Ragnaros", sell_in, quality)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(expected_quality, items[0].quality)
        self.assertEquals(expected_sell_in, items[0].sell_in)

    def test_backstage_passes_increase_from_2_when_sellin_is_10(self):
        # Given
        quality = 5
        expected_quality = quality + 2
        sell_in = 10
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(expected_quality, items[0].quality)

    def test_backstage_passes_increase_from_3_when_sellin_is_5(self):
        # Given
        quality = 5
        expected_quality = quality + 3
        sell_in = 5
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(expected_quality, items[0].quality)

    def test_backstage_passes_decrease_when_selling_is_negative(self):
        # Given
        quality = 5
        expected_quality = 0
        sell_in = 0
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(expected_quality, items[0].quality)
    
    def test_conjured_degrade_twice_in_quality_from_two_when_sellin_is_positive(self):
        # Given
        quality = 5
        expected_quality = 3
        sell_in = 4
        items = [Item("Conjured", sell_in, quality)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(expected_quality, items[0].quality)

    def test_conjured_degrade_twice_in_quality_from_4_when_sellin_is_negative(self):
        # Given
        quality = 5
        expected_quality = 1
        sell_in = -1
        items = [Item("Conjured", sell_in, quality)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(expected_quality, items[0].quality)


if __name__ == '__main__':
    unittest.main()
