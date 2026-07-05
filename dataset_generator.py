import random
import hashlib
import pandas as pd

def generate_and_save_dataset(num_requests=10000, filename="requests_dataset.csv"):
    """
    Generates a mock dataset of academic credential verification requests 
    and saves it to a CSV file to be used by the main algorithm.
    """
    print(f"Generating {num_requests} mock requests...")
    dataset = []
    
    for i in range(num_requests):
        # 1. Generate a mock DID (Decentralized Identifier)
        student_did = f"did:ethr:0x{random.getrandbits(160):040x}"
        
        # 2. Generate a fake IPFS Hash for the document
        mock_pdf_content = f"Degree_Data_{i}".encode()
        ipfs_hash = "Qm" + hashlib.sha256(mock_pdf_content).hexdigest()[:44]
        
        # 3. Assign a region for Sharding purposes
        region = random.choice(["Asia", "Europe", "Americas"])
        
        # Add to our list
        dataset.append({
            "request_id": i,
            "student_did": student_did,
            "ipfs_document_hash": ipfs_hash,
            "shard_region": region
        })
        
    # Convert to Pandas DataFrame
    df = pd.DataFrame(dataset)
    
    # Save to CSV
    df.to_csv(filename, index=False)
    print(f"Success! Dataset saved to {filename}")

# Run the generator
if __name__ == "__main__":
    generate_and_save_dataset(10000)