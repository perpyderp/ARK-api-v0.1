const { DataTypes } = require('sequelize');
const db = require('../src/db');

const Creature = db.define('Creature', {
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    name: {
        type: DataTypes.STRING(255),
        field: 'name',
        allowNull: false
    },
    diet: {
        type: DataTypes.STRING(255),
        field: 'diet',
        allowNull: true
    },
    temperament: {
        type: DataTypes.STRING(255),
        field: 'temperament',
        allowNull: true
    },
    tameable: {
        type: DataTypes.STRING(255),
        field: 'tameable',
        allowNull: true
    },
    rideable: {
        type: DataTypes.STRING(255),
        field: 'rideable',
        allowNull: true
    },
    breedable: {
        type: DataTypes.STRING(255),
        field: 'breedable',
        allowNull: true
    },
    saddleLevelObtained: {
        type: DataTypes.STRING(255),
        field: 'saddleLevelObtained',
        allowNull: true
    },
    creatureID: {
        type: DataTypes.STRING(255),
        field: 'creatureID',
        allowNull: true
    },
    url: {
        type: DataTypes.STRING(255),
        field: 'url',
        allowNull: true
    }
}, {
    tableName: 'creatures',
    timestamps: false
})

// class Creature {
//     constructor(id, name, diet, temperament, tameable, rideable, breedable, saddleLevelObtained, creatureID, url) {
//         this.id = id;
//         this.name = name;
//         this.diet = diet;
//         this.temperament = temperament;
//         this.tameable = tameable;
//         this.rideable = rideable;
//         this.breedable = breedable;
//         this.saddleLevelObtained = saddleLevelObtained;
//         this.creatureID = creatureID;
//         this.url = url;
//     }
// }

module.exports = Creature;