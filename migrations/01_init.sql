-- Initial schema for OmniMind AI
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  tg_id BIGINT UNIQUE NOT NULL,
  username TEXT,
  name TEXT,
  language TEXT,
  age INT,
  sex TEXT,
  height_cm INT,
  weight_kg REAL,
  goal TEXT,
  premium BOOLEAN DEFAULT FALSE,
  credits INT DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS meals (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) ON DELETE CASCADE,
  logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  meal_text TEXT,
  calories REAL,
  protein REAL,
  carbs REAL,
  fats REAL,
  source TEXT
);

CREATE TABLE IF NOT EXISTS user_logs (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id),
  message TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
