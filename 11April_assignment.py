# Assignment Name : Detection Brainstorm
# Description : List 5 uses of face/object detection and design one solution.

"""
Object detection is the task of identifying and locating objects within an 
image or video. This assignment explores its versatility across industries 
and outlines a specific solution design.
"""

def list_uses():
    """Lists 5 diverse uses of Face/Object Detection."""
    uses = [
        {
            "Industry": "1. SECURITY & ACCESS CONTROL",
            "Use Case": "Facial recognition for unlocking devices or entering secure buildings.",
            "Benefit": "Replaces vulnerable passwords/keys with unique biological data."
        },
        {
            "Industry": "2. RETAIL & ANALYTICS",
            "Use Case": "Automatic checkout in 'Grab and Go' stores (like Amazon Go).",
            "Benefit": "Reduces waiting times and labor costs significantly."
        },
        {
            "Industry": "3. HEALTHCARE / MEDICINE",
            "Use Case": "Detecting anomalies (tumors, fractures) in X-rays or MRI scans.",
            "Benefit": "Provides 'second opinion' for doctors, improving diagnostic accuracy."
        },
        {
            "Industry": "4. AUTOMOTIVE (AUTONOMOUS VEHICLES)",
            "Use Case": "Detecting pedestrians, cyclists, and traffic lights for self-driving cars.",
            "Benefit": "Essential for safety and navigation in complex urban environments."
        },
        {
            "Industry": "5. WILDLIFE CONSERVATION",
            "Use Case": "Using drones to count animal populations or detect poachers in reserves.",
            "Benefit": "Protects endangered species in vast areas humans cannot easily patrol."
        }
    ]
    return uses

def design_solution():
    """Detailed design for one specific solution."""
    design = {
        "Project Name": "AI-Powered Wildlife Monitor",
        "Problem": "Illegal pouching and lack of data on migration patterns in vast national parks.",
        "Proposed Solution": (
            "Deploy a network of stationary solar-powered cameras and mobile drones "
            "equipped with YOLOv8 (You Only Look Once) object detection models."
        ),
        "Key Features": [
            "Real-time identification of animal species (Elephants, Tigers, Rhinos).",
            "Automated alerts to rangers when 'Human' activity is detected in restricted zones.",
            "Heatmaps of animal movements generated from detection logs.",
            "Night-vision capability using infrared thermal imaging sensors."
        ],
        "Technical Stack": (
            "Hardware: Raspberry Pi 4 (Edge processing) + High-res Camera + Solar Panel. "
            "Software: Python, OpenCV, YOLOv8/TensorFlow Lite, LoRaWAN for communication."
        )
    }
    return design

def main():
    print("="*70)
    print("           ASSIGNMENT : DETECTION BRAINSTORM")
    print("="*70)

    # 1. List 5 Uses
    print("\n[PART 1] 5 USES OF FACE/OBJECT DETECTION")
    print("-" * 70)
    for use in list_uses():
        print(f"{use['Industry']}")
        print(f"  - Application: {use['Use Case']}")
        print(f"  - Benefit:     {use['Benefit']}\n")

    # 2. Solution Design
    print("\n[PART 2] SOLUTION DESIGN: AI WILDLIFE MONITOR")
    print("-" * 70)
    design = design_solution()
    print(f"Project Name : {design['Project Name']}")
    print(f"Problem      : {design['Problem']}")
    print(f"Solution     : {design['Proposed Solution']}")
    print("\nKey Features:")
    for feature in design['Key Features']:
        print(f" ✅ {feature}")
    print(f"\nTech Stack   : {design['Technical Stack']}")
    print("-" * 70)

if __name__ == "__main__":
    main()
