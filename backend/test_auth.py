import requests
import json

BASE_URL = "http://localhost:8000"

print("=" * 50)
print("Testing Authentication Endpoints")
print("=" * 50)

# Test 1: Register a new client
print("\n1. Registering new client...")
register_data = {
    "email": "test@example.com",
    "name": "Test Restaurant"
}

try:
    response = requests.post(f"{BASE_URL}/api/auth/register", json=register_data)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 201:
        data = response.json()
        print("✅ Registration successful!")
        print(f"Client ID: {data['client_id']}")
        print(f"Client Key: {data['client_key']}")
        
        client_id = data['client_id']
        client_key = data['client_key']
        
        # Test 2: Login
        print("\n2. Logging in...")
        login_data = {
            "client_id": client_id,
            "client_key": client_key
        }
        
        response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Login successful!")
            print(f"Access Token: {data['access_token'][:50]}...")
            
            access_token = data['access_token']
            
            # Test 3: Get client info
            print("\n3. Getting client info...")
            headers = {
                "Authorization": f"Bearer {access_token}"
            }
            
            response = requests.get(f"{BASE_URL}/api/auth/client-info", headers=headers)
            print(f"Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print("✅ Client info retrieved!")
                print(json.dumps(data, indent=2))
            else:
                print(f"❌ Error: {response.text}")
        else:
            print(f"❌ Login failed: {response.text}")
    elif response.status_code == 400:
        print(f"⚠️  Email already registered. Try a different email.")
        print(f"Response: {response.text}")
    else:
        print(f"❌ Registration failed: {response.text}")
        
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nMake sure the server is running on http://localhost:8000")

print("\n" + "=" * 50)
