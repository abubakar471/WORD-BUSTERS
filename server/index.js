import express from "express";
import dotenv from "dotenv";
import cookieParser from "cookie-parser";
import cors from "cors";
import { readdirSync } from "fs";
import {spawn} from "child_process";
dotenv.config();
const app = express();


const port = process.env.PORT || 8000;

app.listen(port, () => {
  console.log(`server is running on port ${port}...`);
});
