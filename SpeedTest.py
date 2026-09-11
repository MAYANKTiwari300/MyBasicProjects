import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "This is the ways for us to reference the object of the class."
]

def measure_accuracy(test_sentence, user_input):
    test_words = test_sentence.split()
    user_words = user_input.split()
    correct_words = sum(1 for test_word, user_word in zip(test_words, user_words) if test_word == user_word)
    accuracy = (correct_words / len(test_words)) * 100 if test_words else 0
    return accuracy

def typing_test():
    test_sentence = random.choice(sentences)
    print("Type the following sentence as fast as you can:")
    print(test_sentence)
    input("Press Enter when you're ready...")
    start_time = time.time() # Measure the start time
    user_input = input("\nStart typing:\n ")
    end_time = time.time() # Measure the end time
    time_taken = end_time - start_time
    
    word_count = len(user_input.split())

    print("Results:")
    print(f"Time taken: {time_taken} seconds")
    print(f"Words typed: {word_count}")   
    print(f"Typing speed: {word_count / (time_taken/60):.2f} words per minute")
    accuracy = measure_accuracy(test_sentence, user_input)  
    print(f"Accuracy: {accuracy:.2f}%")
    
    
typing_test()
