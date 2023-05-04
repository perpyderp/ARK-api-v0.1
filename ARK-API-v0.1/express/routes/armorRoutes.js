
const express = require('express');
const router = express.Router();
const armorController = require('../controllers/armorController');

router.get('/armor', armorController.getArmor);
router.get('/armor/:type', armorController.getArmorByType);
// router.post('/users', creatureController.createCreature);
// router.put('/users/:id', creatureController.updateCreature);
// router.delete('/users/:id', creatureController.deleteCreature);

module.exports = router;
