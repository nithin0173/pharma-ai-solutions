import os

# --- MOCK PHARMA DATA ---
# This represents a simplified version of a Dr. Reddy's inventory system
inventory_db = {
    "PARACETAMOL": {"stock": 5000, "unit": "kg", "last_batch": "DRL-P01"},
    "IBUPROFEN": {"stock": 1200, "unit": "kg", "last_batch": "DRL-I99"},
    "METFORMIN": {"stock": 350, "unit": "liters", "last_batch": "DRL-M42"}
}

def pharma_ai_agent(query):
    """
    A simple AI Agent logic that simulates natural language processing
    to query pharmaceutical inventory.
    """
    query = query.upper()
    print(f"AI Agent: Processing query - '{query}'...")
    
    # Logic to simulate "Text-to-SQL" or "Semantic Search"
    for drug in inventory_db:
        if drug in query:
            data = inventory_db[drug]
            return f"MATCH FOUND: {drug} | Current Stock: {data['stock']} {data['unit']} | Latest Batch: {data['last_batch']}"
            
    return "NO MATCH: I couldn't find that compound in the current inventory. Please try 'Paracetamol' or 'Ibuprofen'."

# --- TEST THE AGENT ---
if __name__ == "__main__":
    print("--- Dr. Reddy's Lab: AI Inventory Agent Demo ---")
    user_input = "What is the current stock level for Paracetamol?"
    result = pharma_ai_agent(user_input)
    print(result)