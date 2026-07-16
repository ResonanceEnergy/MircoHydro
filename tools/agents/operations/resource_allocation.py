import os
import sys
from groq import Groq
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

client = Groq(api_key=GROQ_API_KEY)

def plan_resources(project, resources_needed, timeframe):
    prompt = f"""
You are the Resource Allocation Agent for a micro-hydro operations division. Your job is to plan and allocate resources (personnel, equipment, budget) for operational projects.

Project: {project}
Resources Needed: {resources_needed}
Timeframe: {timeframe}

Return a detailed resource allocation plan with assignments, timelines, and optimization notes.
"""
    response = client.chat.completions.create(
        model="llama-3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()

def optimize_allocation(current_status):
    prompt = f"""
You are the Resource Allocation Agent. Analyze the current resource allocation and suggest optimizations for efficiency and cost-effectiveness.

Current Status: {current_status}

Return actionable recommendations and a revised allocation plan if needed.
"""
    response = client.chat.completions.create(
        model="llama-3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()

def track_resource_usage(resource):
    prompt = f"""
You are the Resource Allocation Agent. Track and report the usage, availability, and bottlenecks for the following resource:

Resource: {resource}

Return a summary report with usage statistics and recommendations.
"""
    response = client.chat.completions.create(
        model="llama-3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Resource Allocation Agent CLI")
    subparsers = parser.add_subparsers(dest="command")

    plan_parser = subparsers.add_parser("plan", help="Plan resource allocation")
    plan_parser.add_argument("project")
    plan_parser.add_argument("resources_needed")
    plan_parser.add_argument("timeframe")

    optimize_parser = subparsers.add_parser("optimize", help="Optimize current allocation")
    optimize_parser.add_argument("current_status")

    track_parser = subparsers.add_parser("track", help="Track resource usage")
    track_parser.add_argument("resource")

    args = parser.parse_args()
    if args.command == "plan":
        print(plan_resources(args.project, args.resources_needed, args.timeframe))
    elif args.command == "optimize":
        print(optimize_allocation(args.current_status))
    elif args.command == "track":
        print(track_resource_usage(args.resource))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
