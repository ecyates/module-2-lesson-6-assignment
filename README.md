# Module 2 - Lesson 6 - Python Strings
Author: Elizabeth Yates

1. Product Review Analysis (product_review_analysis.py)

Task 1: Keyword Highlighter

Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
    reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

Task 2: Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

Task 3: Review Summary

Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

Example: "This product is really good. I'm...",

2. User Input Data Processor (user_input_data_processor.py)

Objective: The aim of this assignment is to process and format user input data.

Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

