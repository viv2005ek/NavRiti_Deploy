# main.py
from planet import get_time_profile
from zodiac import get_zodiac_profile


def normalize(j: str) -> str:
    return " ".join(j.lower().strip().split())


def intersect_jobs(jobs1, jobs2):
    n1 = {normalize(j): j for j in jobs1}
    n2 = {normalize(j): j for j in jobs2}
    common = set(n1.keys()) & set(n2.keys())
    return [n1[c] for c in common]


def main():
    date_input = input("Enter birth date (YYYY-MM-DD or MM-DD): ").strip()
    time_input = input("Enter birth time (HH:MM): ").strip()

    zodiac_profile = get_zodiac_profile(date_input)
    planet_profile = get_time_profile(time_input)

    zodiac_jobs = zodiac_profile["jobs"]
    planet_jobs = planet_profile["jobs"]

    intersection = intersect_jobs(zodiac_jobs, planet_jobs)

    print("\n--- RESULTS ---")
    print(f"Zodiac Sign: {zodiac_profile['sign']}")
    print(f"Planet: {planet_profile['planet']} (Index {planet_profile['index']})")

    print("\nZodiac Jobs:", ", ".join(zodiac_jobs))
    print("Planet Jobs:", ", ".join(planet_jobs))

    print("\nIntersection (Matching Jobs):")
    if intersection:
        for job in intersection:
            print(" •", job)
    else:
        print("No exact job matches found.")


if __name__ == "__main__":
    main()
