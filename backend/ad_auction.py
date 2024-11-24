from sentence_transformers import SentenceTransformer, util
import numpy as np
import sponsors_data as sd

# Load the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Encode sponsor descriptions into embeddings
sponsor_descriptions = [s["description"] for s in sd.sponsors]
sponsor_embeddings = model.encode(sponsor_descriptions, convert_to_tensor=True)

def ad_auction(user_query):
    # Encode user query into an embedding
    query_embedding = model.encode(user_query, convert_to_tensor=True)
    
    # Compute cosine similarity between query and sponsor embeddings
    relevance_scores = util.cos_sim(query_embedding, sponsor_embeddings)[0]  # 1 x N tensor
    relevance_scores = relevance_scores.cpu().numpy()  # Convert to NumPy array

    # Multiply relevance scores by bid values
    quality_adjusted_bids = relevance_scores * np.array([s["bid"] for s in sd.sponsors])

    # Sort quality-adjusted bids in descending order
    sorted_indices = np.argsort(quality_adjusted_bids)[::-1]
    
    # Get the highest and second-highest quality-adjusted bids
    winning_index = sorted_indices[0]
    second_best_index = sorted_indices[1] if len(sorted_indices) > 1 else None

    # Identify the winning sponsor
    winning_sponsor = sd.sponsors[winning_index]

    # Calculate actual CPC (second-price logic)
    if second_best_index is not None:
        actual_cpc = (
            quality_adjusted_bids[second_best_index] / relevance_scores[winning_index]
        ) + 0.01  # Add a small baseline
    else:
        actual_cpc = quality_adjusted_bids[winning_index]  # Fallback if no second bidder
    
    return winning_sponsor
