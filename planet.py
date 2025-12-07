PLANET_MAPPING = {
    1: {
        "planet": "Sun",
        "qualities": ["Leadership", "Creativity", "Confidence"],
        "jobs": ["Manager", "Entrepreneur", "Creative Director", "Public Speaker"]
    },
    2: {
        "planet": "Moon",
        "qualities": ["Emotional", "Intuitive", "Sensitive"],
        "jobs": ["Psychologist", "Writer", "Nurse", "Counsellor"]
    },
    3: {
        "planet": "Jupiter",
        "qualities": ["Wise", "Optimistic", "Expansive"],
        "jobs": ["Professor", "Researcher", "Financial Advisor", "Spiritual Guide"]
    },
    4: {
        "planet": "Rahu (North Node)",
        "qualities": ["Innovative", "Unconventional", "Risk-Taking"],
        "jobs": ["Tech Innovator", "AI Engineer", "Data Analyst", "Startup Founder"]
    },
    5: {
        "planet": "Mercury",
        "qualities": ["Communicative", "Smart", "Adaptable"],
        "jobs": ["Journalist", "Software Developer", "Marketer", "Teacher"]
    },
    6: {
        "planet": "Venus",
        "qualities": ["Artistic", "Harmonious", "Loving"],
        "jobs": ["Designer", "Artist", "Fashion Stylist", "Therapist"]
    },
    7: {
        "planet": "Ketu (South Node)",
        "qualities": ["Spiritual", "Deep Thinker", "Mystical"],
        "jobs": ["Meditation Coach", "Astrologer", "Philosopher", "Healer"]
    },
    8: {
        "planet": "Saturn",
        "qualities": ["Disciplined", "Patient", "Hardworking"],
        "jobs": ["Engineer", "Lawyer", "Auditor", "Project Manager"]
    },
    9: {
        "planet": "Mars",
        "qualities": ["Energetic", "Brave", "Passionate"],
        "jobs": ["Athlete", "Military", "Surgeon", "Firefighter"]
    }
}


def reduce_to_single_digit(n):
    """Reduce any number to a single digit 1–9."""
    while n > 9:
        n = sum(int(d) for d in str(n))
    return 1 if n == 0 else n


def time_to_number(time_str):
    """
    Convert time (HH:MM) → index number (1–9).
    Example: "14:27" → 1+4+2+7 = 14 → 1+4 = 5
    """
    digits = [int(c) for c in time_str if c.isdigit()]
    total = sum(digits)
    return reduce_to_single_digit(total)


def get_time_profile(time_str):
    """
    Main function:
    Input = "HH:MM"
    Output = index, planet, qualities, and jobs
    """
    number = time_to_number(time_str)
    data = PLANET_MAPPING[number]

    return {
        "index": number,
        "planet": data["planet"],
        "qualities": data["qualities"],
        "jobs": data["jobs"]
    }


if __name__ == "__main__":
    time_input = input("Enter birth time (HH:MM): ")
    profile = get_time_profile(time_input)

    print("\nYour Time Index:", profile["index"])
    print("Planet:", profile["planet"])
    print("Qualities:", ", ".join(profile["qualities"]))
    print("Suggested Jobs:", ", ".join(profile["jobs"]))