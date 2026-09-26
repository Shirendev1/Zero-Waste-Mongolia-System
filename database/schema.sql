-- Zero-Waste Mongolia Pilot System v1 Database Schema

CREATE TABLE IF NOT EXISTS waste_categories (
    category_id SERIAL PRIMARY KEY,
    name_en VARCHAR(50) NOT NULL UNIQUE,
    name_mn VARCHAR(50),
    icon VARCHAR(20),
    active BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS waste_batches (
    waste_id VARCHAR(20) PRIMARY KEY,
    qr_code TEXT NOT NULL UNIQUE,
    category_id INT NOT NULL REFERENCES waste_categories(category_id),
    source_name VARCHAR(200),
    source_phone VARCHAR(20),
    source_address VARCHAR(500),
    weight_kg DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    status VARCHAR(30) DEFAULT 'Registered',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS waste_events (
    event_id SERIAL PRIMARY KEY,
    waste_id VARCHAR(20) NOT NULL REFERENCES waste_batches(waste_id) ON DELETE CASCADE,
    event_type VARCHAR(50) NOT NULL,
    event_date TIMESTAMP DEFAULT NOW(),
    actor_name VARCHAR(200),
    actor_role VARCHAR(50),
    weight_kg DECIMAL(10, 2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    role VARCHAR(20) NOT NULL DEFAULT 'viewer',
    language VARCHAR(10) DEFAULT 'en',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_waste_status ON waste_batches(status);
CREATE INDEX IF NOT EXISTS idx_waste_category ON waste_batches(category_id);
CREATE INDEX IF NOT EXISTS idx_waste_created ON waste_batches(created_at);
CREATE INDEX IF NOT EXISTS idx_events_waste_id ON waste_events(waste_id);
CREATE INDEX IF NOT EXISTS idx_events_type ON waste_events(event_type);
CREATE INDEX IF NOT EXISTS idx_events_date ON waste_events(event_date);

-- Seed waste categories
INSERT INTO waste_categories (name_en, name_mn, icon, active) VALUES
('Battery', 'Батерей', '🔋', TRUE),
('E-waste', 'Электрон хог', '📱', TRUE),
('Plastic', 'Хуванцар', '♻️', TRUE),
('Paper/Cardboard', 'Цаас/Картон', '📦', TRUE),
('Glass', 'Шил', '🔍', TRUE),
('Metal', 'Метал', '🔧', TRUE),
('Textile', 'Хэнгэцэнг', '👕', TRUE),
('Organic', 'Органик', '🌱', TRUE),
('Used Tire', 'Ашигласан дугуй', '⚫', TRUE),
('Used Oil', 'Ашигласан тос', '🛢️', TRUE),
('Other Hazardous Waste', 'Бусад аюултай хог', '⚠️', TRUE)
ON CONFLICT (name_en) DO NOTHING;
