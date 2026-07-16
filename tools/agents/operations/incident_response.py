import os
import sys
from groq import Groq
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

client = Groq(api_key=GROQ_API_KEY)

def detect_incident(description):
    prompt = f"""
You are the Incident Response Agent for a micro-hydro operations division. Your job is to detect, classify, and respond to operational incidents.

Incident Description: {description}

Return a classification, severity rating, and recommended immediate actions.
"""
    response = client.chat.completions.create(
        model="llama-3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()

def coordinate_response(incident_id, resources):
    prompt = f"""
You are the Incident Response Agent. Coordinate the response to the following incident, assigning resources and outlining a step-by-step action plan.

Incident ID: {incident_id}
Resources Assigned: {resources}

Return a detailed response plan and communication protocol.
"""
    response = client.chat.completions.create(
        model="llama-3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()

def report_incident_outcome(incident_id, outcome):
    prompt = f"""
You are the Incident Response Agent. Log and analyze the outcome of the following incident response:

Incident ID: {incident_id}
Outcome: {outcome}

Return a summary report, lessons learned, and recommendations for future prevention.
"""
    response = client.chat.completions.create(
        model="llama-3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Incident Response Agent CLI")
    subparsers = parser.add_subparsers(dest="command")

    detect_parser = subparsers.add_parser("detect", help="Detect and classify incident")
    detect_parser.add_argument("description")

    coordinate_parser = subparsers.add_parser("coordinate", help="Coordinate incident response")
    coordinate_parser.add_argument("incident_id")
    coordinate_parser.add_argument("resources")

    report_parser = subparsers.add_parser("report", help="Report incident outcome")
    report_parser.add_argument("incident_id")
    report_parser.add_argument("outcome")

    args = parser.parse_args()
    if args.command == "detect":
        print(detect_incident(args.description))
    elif args.command == "coordinate":
        print(coordinate_response(args.incident_id, args.resources))
    elif args.command == "report":
        print(report_incident_outcome(args.incident_id, args.outcome))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
