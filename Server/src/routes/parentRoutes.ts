import { Router } from 'express';
import { submitParentPreferences } from '../controllers/parentController';

const router = Router();

// POST /api/parent/preferences
router.post('/preferences', submitParentPreferences);

export default router;