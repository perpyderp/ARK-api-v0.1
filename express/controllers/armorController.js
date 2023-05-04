const Armor = require('../models/armor');
const db = require('../src/db');


exports.getArmor = async function (req, res) {
    try {
        const [rows, fields] = await db.query('SELECT * FROM armor');
        res.status(200).json(rows);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal server error' });
    }
}

exports.getArmorById = (req, res) => {
  // Retrieve a creature by ID from the database and send it as a response
};

exports.getArmorByType = async function (req, res) {
    try {
        const [rows, fields] = await db.query("SELECT * FROM armor WHERE armortype = " + db.escape(req.params.type));
        res.status(200).json(rows);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal server error' });
    }
}

exports.createArmor = (req, res) => {
  // Create a new creature in the database and send it as a response
};

exports.updateArmor = (req, res) => {
  // Update a creature by ID in the database and send it as a response
};

exports.deleteArmor = (req, res) => {
  // Delete a creature by ID from the database and send a success message as a response
};
