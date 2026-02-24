def health_chatbot(user, question):

    if not question:
        return "Please ask a health-related question."

    q = str(question).lower()

    if "sleep" in q:
        return "Try maintaining a fixed sleep schedule and avoid screens before bedtime."

    elif "stress" in q:
        return "Practice deep breathing, short walks, and relaxation exercises."

    elif "exercise" in q:
        return "Start with 20–30 minutes of walking or stretching daily."

    elif "water" in q:
        return "Drink at least 2–2.5 litres of water daily."

    elif "diet" in q or "food" in q:
        return "Include fruits, vegetables, and protein-rich foods."

    else:
        return "Maintain balanced sleep, hydration, exercise, and stress management."