
const express = require('express');
const router = express.Router();
const creatureController = require('../controllers/creatureController');

router.get('/creatures', creatureController.getAllCreatures);
router.get('/creatures/:name', creatureController.getCreatureByName);
router.post('/users', creatureController.createCreature);
router.put('/users/:id', creatureController.updateCreature);
router.delete('/users/:id', creatureController.deleteCreature);

module.exports = router;
