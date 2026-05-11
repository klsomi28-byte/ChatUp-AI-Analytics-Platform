#  ChatUp AI Analytics Platform
An AI-powered real-time communication and analytics platform developed using Python, MongoDB, Flask, JWT authentication, socket programming, and NLP techniques.

#  Features
## Real-Time Communication
- Multi-user chat system
- Public messaging
- Private messaging
- Concurrent client handling using threading
- Socket-based communication

## Authentication & Security
- User registration
- Login authentication
- JWT token verification
- Password hashing using bcrypt
## Database Integration
- MongoDB integration
- User data storage
- Chat history storage
- Activity logging
- Connection management
## Data Analytics Features
- User activity analysis
- Daily active users (DAU)
- Message statistics
- Peak activity hours
- User engagement tracking
- User growth analytics
## AI & NLP Features
- Sentiment analysis
- Trending keyword extraction
- Message polarity analysis
- Text analytics
## Dashboard Features
- Flask analytics dashboard
- JSON analytics API
- Real-time analytics reporting


#  Technologies Used
- Python
- MongoDB
- Flask
- Socket Programming
- JWT Authentication
- bcrypt
- TextBlob NLP
- Threading
- REST APIs

# Project Structure
```bash
ChatUp/
│
├── auth.py
├── client.py
├── server.py
├── analytics.py
├── ai_analysis.py
├── dashboard.py
├── social_service.py
├── db.py
├── config.py
│

# Installation
## Clone Repository
```bash
git clone https://github.com/yourusername/ChatUp-AI-Analytics-Platform.git
## Install Dependencies

```bash
pip install -r requirements.txt
``
## Start MongoDB

```bash
mongod
```
# Running the Project
## Start Server
```bash
python server.py
```
## Run Client
```bash
python client.py
```
## Run Dashboard
```bash
python dashboard.py
```
#  Dashboard
Open browser:
```bash
http://127.0.0.1:5000
```
##Anlytics Supported
- User Activity Tracking
- Sentiment Analysis
- Trending Keywords
- Message Statistics
- Peak Usage Hours
- Daily Active Users
- User Growth Metrics

#  Authentication Flow

```text
User Login
    ↓
JWT Token Generated
    ↓
Client Sends Token
    ↓
Server Verifies Token
    ↓
Access Granted
```
#  NLP Features
The platform uses TextBlob NLP for:
- Sentiment Analysis
- Polarity Detection
- Keyword Analysis

#  Future Improvements
- Kafka Streaming
- Redis Caching
- React Frontend
- WebSocket Integration
- Docker Deployment
- Kubernetes Scaling
- Machine Learning Models
- Recommendation Systems
- Power BI Dashboard

# 👨‍💻 Author

Developed by Sanjana K L
