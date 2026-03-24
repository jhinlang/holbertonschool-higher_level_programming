#!/usr/bin/python3
"""Module for generating invitation files"""


def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template"""
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Invalid input types")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Invalid input types")
            return

    if template == "":
        print("Templat is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    
    for i, attendee in enumerate(attendees, start = 1):
        name = attendee.get("name")
        event_title = attendee.get("event_title")
        event_date = attendee.get("event_date")
        event_location = attendee.get("event_location")

        if name is None:
            name = "N/A"
        if event_title is None:
            event_title = "N/A"
        if event_date is None:
            event_date = "N/A"
        if event_location is None:
            event_location = "N/A"
            
        content = template
        content = template.replace("{name}", str(name))
        content = template.replace("{event_title}", str(event_title))
        content = template.replace("{event_date}", str(event_date))
        content = template.replace("{event_location}", str(event_location))

        filename = "output_{}.txt".format(i)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
