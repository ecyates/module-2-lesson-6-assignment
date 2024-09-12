# 1. Product Review Analysis
# Task 1: Keyword Highlighter

# Write a program that searches through reviews list and looks for keywords such as "good", 
# "excellent", "bad", "poor", and "average". We want you to capitalize those keywords 
# then print out each review. Print out each review with the keywords in uppercase so they stand out.
# So for the first string in the reviews list, we want it to say: 
# "This product is really GOOD. I'm impressed with its quality."

def keywordHighlighter(reviews):
    # Temporary list
    reviews_upper = []

    # Take the keywords that we want to highlight
    keywords = ["good", "excellent", "bad", "poor", "average"]
    
    # For each review
    for review in reviews:
        # For each keyword
        for word in keywords:
            # Check if the word is in there (regardless of case)
            index = review.casefold().find(word)
            # Create a new review string
            new_review = ""
            # If the word is the first word, the new string is the uppercase word + the rest of the review
            if index == 0:
                new_review = word.upper() + review[index+len(word):len(review)+1]
            # If the word is found later, the new string is the beginning + the uppercase word + the ending
            elif index > 0:
                new_review = review[0:index] + word.upper() + review[index+len(word):len(review)+1]
            # If the word is not found, continue
            else: pass
            # If the new string was created, add it to the uppercase list
            if new_review != "":
                reviews_upper.append(new_review)
    return reviews_upper

# Take the reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
    ]

print("\n".join(keywordHighlighter(reviews)))
        
# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review.  
# The function should return the total count of positive and negative words.

def sentimentTally (review):
    # Declare the positive words
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    # Declare the negative words
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    # Let's keep the positive and negative tallies
    pos_tally = 0
    neg_tally = 0

    # For each positive word, if it's in the review, mark the tally
    for pw in positive_words:
        if pw in review.lower(): 
            pos_tally+=1
    # For each negative word, if it's in the review, mark the tally
    for nw in negative_words:
        if nw in review.lower():
            neg_tally+=1

    # Return the total instances of positive and negative words    
    return pos_tally, neg_tally

# Iterate the reviews and print their sentiment tallies.
for r in reviews: 
    pos_tally, neg_tally = sentimentTally(r)
    print(f"Review #{reviews.index(r)} has {pos_tally} positive words and {neg_tally} negative words.")

# Task 3: Review Summary
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.
# Example: "This product is really good. I'm...",

def review_summary(review):
    # Split the review into a list of words
    by_word = review.split()
    summary = ""
    # For each of the words, check if it's going to go over the limit, if not, add the next words to the summary
    for word in by_word:
        if len(summary)>=30:
            break
        else:
            summary = summary + " " + word
    # Add the ellipsis
    summary = summary + "..."
    # Remove any extra spaces when it returns the summary
    return summary.strip()

# Iterate through the reviews and print their summaries.
for r in reviews: 
    print(review_summary(r))
    
