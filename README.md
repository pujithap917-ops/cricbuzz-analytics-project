# 🏏 Cricbuzz Cricket Analytics Project

## 📌 Project Overview

Cricbuzz Cricket Analytics is an end-to-end cricket data analytics project that collects cricket data through an API, stores the data in a MySQL database, performs SQL-based analysis, and presents insights through an interactive Streamlit dashboard.

## 🎯 Objectives

- Fetch cricket data using an API
- Store structured cricket data in MySQL
- Perform data analysis using SQL
- Analyze players, teams, matches, venues and series
- Implement CRUD operations
- Build an interactive Streamlit dashboard
- Generate meaningful cricket insights

## 🛠️ Technologies Used

- Python
- SQL
- MySQL
- Streamlit
- Pandas
- Requests
- SQLAlchemy
- PyMySQL
- Plotly
- RapidAPI

## 🔄 Project Architecture

Cricbuzz API
↓
Python API Client
↓
JSON Data
↓
MySQL Database
↓
SQL Analytics
↓
Streamlit Dashboard

## 📊 Dashboard Features

### 🏠 Home
- Project overview
- Database connection status
- Technology overview
- Data flow

### 🏏 Live Matches
- Fetch live cricket matches
- Display match information
- View API response

### 🏆 Top Players
- Top run scorers
- Player statistics
- Batting performance

### 📈 SQL Analytics
- Player analysis
- Team analysis
- Match analysis
- Venue analysis
- Series analysis
- 25 SQL analytical questions

### ✏️ CRUD Operations
- Add players
- View players
- Delete players
- Manage database records

### ⚙️ Settings
- Database configuration
- API configuration
- Connection status

## 🗄️ Database

The project uses MySQL as the relational database.

Main tables include:

- Teams
- Players
- Venues
- Series
- Matches
- Innings
- Batting Performance
- Bowling Performance
- Fielding Performance
- API Raw Responses

## 📁 Project Structure

```text
cricbuzz-analytics-project/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── api/
│   ├── __init__.py
│   └── cricbuzz_client.py
│
├── database/
│   ├── __init__.py
│   └── connection.py
│
├── pages/
│   ├── 1_Live_Matches.py
│   ├── 2_Top_Players.py
│   ├── 3_SQL_Analytics.py
│   ├── 4_CRUD.py
│   └── 5_Settings.py
│
├── sql/
│   └── schema.sql
│
└── data/
