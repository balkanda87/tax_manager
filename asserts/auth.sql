-- Drop tables if they exist
DROP TABLE IF EXISTS user_profile CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS user_role;
DROP TABLE IF EXISTS blacklist;
DROP TABLE IF EXISTS password_history;
DROP TABLE IF EXISTS refresh_tokens;
DROP TABLE IF EXISTS tokens;

-- Create tables
CREATE TABLE user_profile (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
	email VARCHAR(100) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    mobile_number VARCHAR(18) NOT NULL,
	profile_image bytea,
    pan_id VARCHAR(18),
    aadhar_id VARCHAR(18),
    uan_id VARCHAR(50)
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    hashed_password VARCHAR(255) NOT NULL
);


CREATE TABLE user_role (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    user_role VARCHAR(50) NOT NULL
);

CREATE TABLE tokens (
    id SERIAL PRIMARY KEY,
	user_id INT REFERENCES users(id),
    token_type VARCHAR(10) NOT NULL,
	token VARCHAR(255) NOT NULL,
    expiration_time TIMESTAMP NOT NULL
);

-- CREATE TABLE refresh_tokens (
--     id SERIAL PRIMARY KEY,
-- 	user_id INT REFERENCES users(id),
--     token VARCHAR(255) NOT NULL,
--     expiration_time TIMESTAMP NOT NULL
-- );

CREATE TABLE password_history (
    id SERIAL PRIMARY KEY,
	user_details_id INT REFERENCES user_profile(id),
    hashed_password VARCHAR(255) NOT NULL,
    last_updated TIMESTAMP NOT NULL
);

CREATE TABLE blacklist (
	id SERIAL PRIMARY KEY,
	refresh_token_id INT REFERENCES refresh_tokens(id),
    blacklisted_at TIMESTAMP NOT NULL
);
