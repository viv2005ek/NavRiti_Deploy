import { Request, Response } from 'express';
import ParentPreference from '../models/ParentPreference';

export const submitParentPreferences = async (req: Request, res: Response) => {
  try {
    const data = req.body;

    // 1. Save to MongoDB
    const newPreference = new ParentPreference({
      ...data,
      timestamp: new Date() // Ensure timestamp is set
    });
    
    await newPreference.save();

    // 2. Return Static Result (Mocking the ML Model response)
    // In the future, this is where you'd call your Python/ML service
    const staticResult = {
      status: "success",
      message: "Preferences saved and analyzed.",
      prediction: {
        score: 85,
        recommended_path: "Software Engineering",
        match_reason: "High alignment with financial stability and low risk tolerance.",
        flags: ["Matches budget constraints"]
      },
      saved_id: newPreference._id
    };

    res.status(201).json(staticResult);

  } catch (error) {
    console.error("Error saving preferences:", error);
    res.status(500).json({ message: "Server error processing request", error });
  }
};