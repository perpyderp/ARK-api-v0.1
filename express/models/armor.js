class Armor {
    constructor(id, armortype, unlock_level, cold_protection, heat_protection, weight, durability, found_in, ingredients, url) {
        this.id = id;
        this.amortype = armortype;
        this.unlock_level = unlock_level;
        this.armor_rating = armor_rating;
        this.cold_protection = cold_protection;
        this.heat_protection = heat_protection;
        this.weight = weight;
        this.durability = durability;
        this.found_in = found_in;
        this.ingredients = ingredients;
        this.url = url;
    }
}

module.exports = Armor;