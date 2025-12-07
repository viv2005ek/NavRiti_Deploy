from datetime import datetime, date
from typing import Dict, Tuple, Any


# Zodiac definitions: (start_month, start_day), (end_month, end_day)
ZODIAC_RANGES: Dict[str, Tuple[Tuple[int, int], Tuple[int, int]]] = {
    "Aries":       ((3, 21),  (4, 19)),
    "Taurus":      ((4, 20),  (5, 20)),
    "Gemini":      ((5, 21),  (6, 20)),
    "Cancer":      ((6, 21),  (7, 22)),
    "Leo":         ((7, 23),  (8, 22)),
    "Virgo":       ((8, 23),  (9, 22)),
    "Libra":       ((9, 23),  (10, 22)),
    "Scorpio":     ((10, 23), (11, 21)),
    "Sagittarius": ((11, 22), (12, 21)),
    "Capricorn":   ((12, 22), (1, 19)),
    "Aquarius":    ((1, 20),  (2, 18)),
    "Pisces":      ((2, 19),  (3, 20)),
}

# Profile data
ZODIAC_PROFILE: Dict[str, Dict[str, Any]] = {
    "Aries": {
        "qualities": ["Courageous", "Energetic", "Direct", "Confident"],
        "jobs": ["Entrepreneur", "Military Officer", "Surgeon", "Sports Coach"]
    },
    "Taurus": {
        "qualities": ["Reliable", "Patient", "Practical", "Persistent"],
        "jobs": ["Banker", "Chef", "Architect", "Real Estate Agent"]
    },
    "Gemini": {
        "qualities": ["Communicative", "Adaptable", "Curious", "Quick-witted"],
        "jobs": ["Journalist", "Public Relations", "Software Developer", "Teacher"]
    },
    "Cancer": {
        "qualities": ["Emotional", "Caring", "Protective", "Intuitive"],
        "jobs": ["Nurse", "Counsellor", "Social Worker", "Chef"]
    },
    "Leo": {
        "qualities": ["Confident", "Creative", "Generous", "Dramatic"],
        "jobs": ["Actor", "Creative Director", "Manager", "Public Speaker"]
    },
    "Virgo": {
        "qualities": ["Analytical", "Hardworking", "Detail-oriented", "Modest"],
        "jobs": ["Analyst", "Editor", "Engineer", "Pharmacist"]
    },
    "Libra": {
        "qualities": ["Diplomatic", "Fair", "Social", "Charming"],
        "jobs": ["Lawyer", "Diplomat", "Designer", "Mediator"]
    },
    "Scorpio": {
        "qualities": ["Passionate", "Determined", "Intense", "Observant"],
        "jobs": ["Investigator", "Psychologist", "Surgeon", "Forensic Analyst"]
    },
    "Sagittarius": {
        "qualities": ["Optimistic", "Independent", "Adventurous", "Philosophical"],
        "jobs": ["Travel Writer", "Professor", "Pilot", "Outdoor Guide"]
    },
    "Capricorn": {
        "qualities": ["Disciplined", "Ambitious", "Responsible", "Practical"],
        "jobs": ["Manager", "Engineer", "Accountant", "Judge"]
    },
    "Aquarius": {
        "qualities": ["Innovative", "Humanitarian", "Independent", "Original"],
        "jobs": ["Researcher", "Data Scientist", "Inventor", "NGO Professional"]
    },
    "Pisces": {
        "qualities": ["Compassionate", "Artistic", "Imaginative", "Sensitive"],
        "jobs": ["Artist", "Therapist", "Musician", "Nurse"]
    },
}


def _parse_date_string(d: str) -> date:
    d = d.strip()
    today = date.today()
    for fmt in ("%Y-%m-%d", "%m-%d", "%m/%d", "%Y/%m/%d"):
        try:
            parsed = datetime.strptime(d, fmt)
            if "%Y" in fmt:
                return parsed.date()
            else:
                return date(today.year, parsed.month, parsed.day)
        except ValueError:
            continue
    raise ValueError("Please enter date in format YYYY-MM-DD or MM-DD.")


def _in_range(month: int, day: int, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
    m_d = (month, day)
    if start <= end:
        return start <= m_d <= end
    else:
        return m_d >= start or m_d <= end


def get_zodiac_sign(birth_date_str: str) -> str:
    d = _parse_date_string(birth_date_str)
    month, day = d.month, d.day
    for sign, (start, end) in ZODIAC_RANGES.items():
        if _in_range(month, day, start, end):
            return sign
    raise RuntimeError("Could not determine zodiac sign.")


def get_zodiac_profile(birth_date_str: str) -> Dict[str, Any]:
    sign = get_zodiac_sign(birth_date_str)
    start, end = ZODIAC_RANGES[sign]
    profile = ZODIAC_PROFILE[sign]

    return {
        "sign": sign,
        "qualities": profile["qualities"],
        "jobs": profile["jobs"],
        "date_range": f"{start[0]}/{start[1]} - {end[0]}/{end[1]}"
    }


if __name__ == "__main__":
    user_input = input("Enter birth date (YYYY-MM-DD or MM-DD): ")
    profile = get_zodiac_profile(user_input)

    print("\nYour Zodiac Sign:", profile["sign"])
    print("Date Range:", profile["date_range"])
    print("Qualities:", ", ".join(profile["qualities"]))
    print("Suggested Jobs:", ", ".join(profile["jobs"]))
