const Creature = require('../models/creature');
const db = require('../src/db');

// get all creatures
exports.getAllCreatures = async function (req, res) {
    try {
      const creatures = await Creature.findAll();
      res.status(200).json({ creatures });
    } catch (error) {
      console.log(error);
      res.status(500).json({ message: "Server error" });
    }
  };


exports.getCreatureById = (req, res) => {
  // Retrieve a creature by ID from the database and send it as a response
};

exports.getCreatureByField = async (req, res) => {
    const { field, value } = req.params;
    try {
        const creature = await Creature.findOne({
            where: {
                [field]: value
            }
        });
        if (!creature) {
            return res.status(404).json({ message: 'Creature not found' });
        }
        return res.status(200).json(creature);

    } catch (error) {
        console.error(error);
        return res.status(500).json({ message: 'Server Error' });
    }
};

exports.getCreatureByName = async function (req, res) {
    const name = req.params.name;
    try {
        const creature = await Creature.findOne({
            where: {
                name: name
            }
        });
        if (!creature) {
            return res.status(404).json({ message: 'Creature not found' });
        }
        return res.status(200).json(creature);

    } catch (error) {
        console.error(error);
        return res.status(500).json({ message: 'Server Error' });
    }
}

exports.createCreature = (req, res) => {
  // Create a new creature in the database and send it as a response
};

exports.updateCreature = (req, res) => {
  // Update a creature by ID in the database and send it as a response
};

exports.deleteCreature = (req, res) => {
  // Delete a creature by ID from the database and send a success message as a response
};
