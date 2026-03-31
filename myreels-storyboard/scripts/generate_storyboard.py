#!/usr/bin/env python3
"""
Generate storyboard CSV file

Usage:
    python3 generate_storyboard.py <story_text> [--shots N] [--style STYLE] [--aspect RATIO]

Example:
    python3 generate_storyboard.py "A girl smiling under cherry blossoms" --shots 10 --style cinematic --aspect 16:9
"""

import argparse
import csv
import json
import sys
import os
from pathlib import Path

DEFAULT_OUTPUT = "storyboard.csv"

# Shot types
SHOT_TYPES = ["Wide/Long", "Full", "Medium", "Close-up", "Extreme Close-up"]

# Camera angles
CAMERA_ANGLES = ["Eye-level", "Low-angle", "High-angle", "Side", "Bird's Eye", "Dutch"]


def parse_args():
    parser = argparse.ArgumentParser(description="Generate storyboard CSV")
    parser.add_argument("story", help="Story content or outline")
    parser.add_argument("--shots", type=int, default=10, help="Number of shots, default 10")
    parser.add_argument("--style", default="cinematic", help="Video style")
    parser.add_argument("--aspect", default="16:9", help="Aspect ratio")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="Output CSV file path")
    return parser.parse_args()


def generate_shots(story, num_shots, style, aspect):
    """
    Generate storyboard data based on story content
    This is a placeholder; actual content is filled by AI
    """
    shots = []
    for i in range(1, num_shots + 1):
        shot = {
            "shot_id": i,
            "shot_type": "",
            "camera_angle": "",
            "duration": "",
            "visual_prompt": "",
            "action": "",
            "dialogue": "",
            "notes": "",
            "image_url": "",
            "video_url": "",
            "status": "pending"
        }
        shots.append(shot)
    return shots


def write_csv(shots, output_path):
    """Write CSV file"""
    fieldnames = [
        "shot_id", "shot_type", "camera_angle", "duration",
        "visual_prompt", "action", "dialogue", "notes",
        "image_url", "video_url", "status"
    ]

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(shots)

    print(f"Storyboard generated: {output_path}")
    print(f"Total {len(shots)} shots. Please edit CSV to fill in details.")


def main():
    args = parse_args()

    print(f"Story: {args.story}")
    print(f"Shot count: {args.shots}")
    print(f"Style: {args.style}")
    print(f"Aspect ratio: {args.aspect}")
    print()

    # Generate storyboard data
    shots = generate_shots(args.story, args.shots, args.style, args.aspect)

    # Write CSV
    output_path = Path(args.output).resolve()
    write_csv(shots, output_path)

    print(f"\nNote: AI will automatically fill in detailed descriptions for each shot")
    print(f"      Please confirm and edit the visual_prompt field after generation")


if __name__ == "__main__":
    main()
