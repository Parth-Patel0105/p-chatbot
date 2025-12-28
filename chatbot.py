import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data FIRST (before any class initialization)
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)
nltk.download('punkt_tab', quiet=True)  # NEW: Required for some systems

class DataRetrievalChatbot:
    def __init__(self):
        # Define all intents with comprehensive patterns
        self.intents = {"intents": [
            {
                "tag": "sales_data",
                "patterns": [
                    "show sales", "sales data", "revenue", "sales figures",
                    "total revenue", "monthly sales", "sales report",
                    "what are our sales", "what is our revenue"
                ],
                "responses": ["📊 Sales Data Retrieved"]
            },
            {
                "tag": "customer_count",
                "patterns": [
                    "customer count", "how many customers", "total customers",
                    "customer base", "client count", "number of customers",
                    "active customers", "customer statistics", "customer total",
                    "client base size", "what is our customer count"
                ],
                "responses": ["👥 Customer Data Retrieved"]
            },
            {
                "tag": "inventory",
                "patterns": [
                    "inventory", "stock", "products", "inventory levels",
                    "check inventory", "stock status", "warehouse stock",
                    "product availability", "what is our inventory"
                ],
                "responses": ["📦 Inventory Data Retrieved"]
            },
            {
                "tag": "help",
                "patterns": [
                    "commands", "help", "show commands",
                    "how do i use this", "show me what i can ask"
                ],
                "responses": ["ℹ️ Help Information Retrieved"]
            },
            {
                "tag": "unknown",
                "patterns": ["weather", "joke", "news", "time", "random", "xyz", "abc"],
                "responses": ["❓ I don't understand. Try: sales, customers, inventory, or commands"]
            }
        ]}
        
        # Prepare training data
        patterns = []
        tags = []
        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                patterns.append(pattern)
                tags.append(intent['tag'])
        
        self.tags = tags
        
        # Use simple vectorizer - avoid custom tokenizer issues
        self.vectorizer = TfidfVectorizer()
        self.vectorizer.fit(patterns)
        self.pattern_vectors = self.vectorizer.transform(patterns)
    
    def chat(self, query):
        """Main chat processing method"""
        # Handle empty input
        if not query or not query.strip():
            return {
                'intent': 'unknown',
                'response': 'Please ask a question about sales, customers, or inventory.',
                'data': {},
                'confidence': 0.0
            }
        
        # Vectorize and classify
        query_vector = self.vectorizer.transform([query.lower()])
        similarities = cosine_similarity(query_vector, self.pattern_vectors).flatten()
        
        # Strict threshold for unknown detection
        if len(similarities) == 0 or max(similarities) < 0.25:
            intent = "unknown"
            confidence = 0.0
        else:
            best_match_idx = np.argmax(similarities)
            intent = self.tags[best_match_idx]
            confidence = min(float(max(similarities)), 1.0)
        
        # Get data for the intent
        data = self.get_data(intent)
        
        # Format response
        if intent == "help":
            response = self.get_help_response()
        else:
            response = f"### 📊 {intent.replace('_', ' ').title()}\n\n"
            for key, value in data.items():
                response += f"**{key.replace('_', ' ').title()}:** {value}\n\n"
        
        return {
            'intent': intent,
            'response': response,
            'data': data,
            'confidence': confidence
        }
    
    def get_data(self, intent):
        """Return data based on intent"""
        if intent == "sales_data":
            return {
                "total_sales": "$245,670",
                "growth": "+12.5%",
                "period": "Last 30 days",
                "top_product": "Premium Widget"
            }
        elif intent == "customer_count":
            return {
                "total_customers": 15234,
                "new_this_month": 234,
                "active_customers": 8945,
                "churn_rate": "2.3%"
            }
        elif intent == "inventory":
            return {
                "in_stock": 3421,
                "low_stock": 23,
                "out_of_stock": 5,
                "warehouse_location": "New Jersey"
            }
        elif intent == "help":
            return {"available_commands": ["sales", "customers", "inventory"]}
        else:
            return {"message": "Try asking about sales, customers, inventory, or type 'commands' for help"}
    
    def get_help_response(self):
        """Return formatted help response"""
        return """
### 🤖 Available Commands

**💰 Sales & Revenue:**
• show sales
• sales data
• revenue
• sales figures

**👥 Customer Analytics:**
• customer count
• how many customers
• total customers
• customer statistics

**📦 Inventory:**
• inventory
• stock status
• check inventory
• product availability

**📚 Help:**
• commands
• help

**Try asking:** "show sales" or "customer count"
"""

# Initialize bot instance
bot = DataRetrievalChatbot()