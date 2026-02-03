def chatbot():
    print("Chatbot: Hi! I'm your Smart Education Assistant.")
    while True:
        user = input("You: ").lower()
        if "exam" in user:
            print("Chatbot: Exams start from November 20, 2025.")
        elif "syllabus" in user:
            print("Chatbot: You can download the syllabus from the college portal.")
        elif "career" in user:
            print("Chatbot: You can explore jobs, higher studies, or GATE prep based on your interest.")
        elif "fee" in user:
            print("Chatbot: The last date to pay fees is October 15.")
        elif "bye" in user:
            print("Chatbot: Goodbye! All the best.")
            break
        else:
            print("Chatbot: Sorry, I don’t know that yet. I will improve in future versions.")

chatbot()
