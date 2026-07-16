import os
import sys
from groq import Groq
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

client = Groq(api_key=GROQ_API_KEY)

def schedule_maintenance(equipment, date, details):
    prompt = f"""
You are the Maintenance Management Agent for a micro-hydro operations division. Your job is to schedule preventive and corrective maintenance for all equipment. 

Equipment: {equipment}
Date: {date}
Details: {details}

Return a clear, actionable maintenance schedule entry with all relevant instructions and reminders.
"""
    response = client.chat.completions.create(
        model="llama-3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()

def track_maintenance(equipment):
    prompt = f"""
You are the Maintenance Management Agent. Retrieve and summarize the maintenance history and upcoming tasks for the following equipment:

Equipment: {equipment}

Return a concise report with completed, pending, and overdue tasks.
"""
    response = client.chat.completions.create(
        model="llama-3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()

def report_maintenance_issues(equipment, issue):
    prompt = f"""
You are the Maintenance Management Agent. Log and analyze a reported maintenance issue for the following equipment:

Equipment: {equipment}
Issue: {issue}

Return a recommended action plan, urgency rating, and escalation steps if needed.
"""
    response = client.chat.completions.create(
        model="llama-3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Maintenance Management Agent CLI")
    subparsers = parser.add_subparsers(dest="command")

    schedule_parser = subparsers.add_parser("schedule", help="Schedule maintenance task")
    schedule_parser.add_argument("equipment")
    schedule_parser.add_argument("date")
    schedule_parser.add_argument("details")

    track_parser = subparsers.add_parser("track", help="Track maintenance for equipment")
    track_parser.add_argument("equipment")

    report_parser = subparsers.add_parser("report", help="Report maintenance issue")
    report_parser.add_argument("equipment")
    report_parser.add_argument("issue")

    args = parser.parse_args()
    if args.command == "schedule":
        print(schedule_maintenance(args.equipment, args.date, args.details))
    elif args.command == "track":
        print(track_maintenance(args.equipment))
    elif args.command == "report":
        print(report_maintenance_issues(args.equipment, args.issue))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
