import express from 'express';
import mongoose from 'mongoose';
import cors from 'cors';
import parentRoutes from './routes/parentRoutes';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors()); // Critical for frontend to talk to backend
app.use(express.json());

// Routes
app.use('/api/parent', parentRoutes);

// DB Connection (Assuming you have this set up)
mongoose.connect(process.env.MONGO_URI as string)
  .then(() => console.log('MongoDB Connected'))
  .catch(err => console.log(err));

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});