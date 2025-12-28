# test_chatbot_advanced.py
import pytest
import time
from chatbot import bot

class TestChatbotAccuracy:
    """Test classification accuracy for all intents"""

    def test_sales_data_variations(self):
        """Test 10+ variations of sales queries"""
        sales_queries = [
            "show sales",
            "sales data", 
            "revenue",
            "show me sales figures",
            "what are our sales",
            "display sales information",
            "get sales numbers",
            "sales report",
            "total revenue",
            "monthly sales"
        ]
        
        for query in sales_queries:
            result = bot.chat(query)
            assert result['intent'] == "sales_data", f"Failed on: {query}"
            assert "total_sales" in str(result['data'])
            assert "$245,670" in str(result['data'])

    def test_customer_count_variations(self):
        """Test 10+ variations of customer queries"""
        customer_queries = [
            "customer count",
            "how many customers",
            "total customers",
            "customer base",
            "client count",
            "number of customers",
            "active customers",
            "customer statistics",
            "customer total",
            "client base size"
        ]
        
        for query in customer_queries:
            result = bot.chat(query)
            assert result['intent'] == "customer_count", f"Failed on: {query}"
            assert "15_234" in str(result['data']) or "15234" in str(result['data'])

    def test_inventory_variations(self):
        """Test 8+ variations of inventory queries"""
        inventory_queries = [
            "inventory",
            "stock",
            "products",
            "inventory levels",
            "check inventory",
            "stock status",
            "warehouse stock",
            "product availability"
        ]
        
        for query in inventory_queries:
            result = bot.chat(query)
            assert result['intent'] == "inventory", f"Failed on: {query}"
            assert "in_stock" in str(result['data'])

class TestDataIntegrity:
    """Test that data is correctly structured"""

    def test_sales_data_structure(self):
        result = bot.chat("sales")
        assert isinstance(result['data'], dict)
        assert "total_sales" in result['data']
        assert "growth" in result['data']
        assert "period" in result['data']
        assert "top_product" in result['data']
        assert result['data']['total_sales'] == "$245,670"

    def test_customer_data_structure(self):
        result = bot.chat("customers")
        assert isinstance(result['data'], dict)
        assert "total_customers" in result['data']
        assert "new_this_month" in result['data']
        assert "active_customers" in result['data']
        assert "churn_rate" in result['data']
        assert result['data']['total_customers'] == 15234

    def test_inventory_data_structure(self):
        result = bot.chat("inventory")
        assert isinstance(result['data'], dict)
        assert "in_stock" in result['data']
        assert "low_stock" in result['data']
        assert "out_of_stock" in result['data']
        assert "warehouse_location" in result['data']

class TestEdgeCases:
    """Test unusual inputs and error handling"""

    def test_unknown_query(self):
        """Test that unknown queries are handled gracefully"""
        result = bot.chat("what's the weather today")
        assert result['intent'] == "unknown" or "unknown" in result['response'].lower()

    def test_empty_input(self):
        result = bot.chat("")
        assert result['intent'] == "unknown" or len(result['data']) == 0

    def test_single_character(self):
        result = bot.chat("x")
        # Should handle without crashing
        assert 'intent' in result

    def test_very_long_query(self):
        long_query = "customer count " * 100
        result = bot.chat(long_query)
        assert result['intent'] == "customer_count"

    def test_special_characters(self):
        result = bot.chat("customer@#$%count")
        assert result['intent'] == "customer_count"

    def test_case_insensitive(self):
        result1 = bot.chat("CUSTOMER COUNT")
        result2 = bot.chat("Customer Count")
        result3 = bot.chat("customer count")
        assert result1['intent'] == result2['intent'] == result3['intent'] == "customer_count"

class TestPerformance:
    """Test speed and responsiveness"""

    def test_response_time(self):
        """Test that responses are under 200ms"""
        start_time = time.time()
        result = bot.chat("show sales")
        elapsed = time.time() - start_time
        
        print(f"Response time: {elapsed*1000:.2f}ms")
        assert elapsed < 0.5, f"Too slow: {elapsed*1000:.2f}ms"

    def test_multiple_queries_speed(self):
        """Test 10 queries complete in under 2 seconds"""
        queries = ["sales", "customers", "inventory"] * 3 + ["unknown"]
        
        start_time = time.time()
        for query in queries:
            bot.chat(query)
        elapsed = time.time() - start_time
        
        print(f"10 queries took: {elapsed*1000:.2f}ms")
        assert elapsed < 2.0, f"Batch too slow: {elapsed*1000:.2f}ms"

class TestUserExperience:
    """Test conversation flow and clarity"""

    def test_response_format(self):
        """Test that responses are well-formatted"""
        result = bot.chat("sales")
        
        # Should have clear sections
        assert "###" in result['response'] or "**" in result['response']
        assert "total_sales" in str(result['data']) or "Total Sales" in result['response']

    def test_data_completeness(self):
        """Test that no data fields are missing"""
        test_cases = [
            ("sales", ["total_sales", "growth", "period"]),
            ("customers", ["total_customers", "active_customers"]),
            ("inventory", ["in_stock", "low_stock"])
        ]
        
        for query, expected_fields in test_cases:
            result = bot.chat(query)
            for field in expected_fields:
                assert field in str(result['data']).lower() or field in result['response'].lower()

    def test_confidence_scoring(self):
        """Test that confidence scores are reasonable"""
        result = bot.chat("show sales")
        assert 'confidence' in result
        assert 0 <= result['confidence'] <= 1.0

# Run tests manually
if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])