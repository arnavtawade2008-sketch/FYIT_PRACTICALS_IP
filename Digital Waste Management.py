# GREENTECH - INTRODUCTION TO PROGRAMMING PROJECT

def device_recommendation():
    device_name = input("Enter the device name: ")
    age_input = input(f"How many years have you used the {device_name}? ")
    age = int(age_input)
    working_input = input("Is the device working properly? (yes/no): ")
    major_problem_input = input("Does the device have a major problem? (yes/no): ")
    working = working_input.lower()
    major_problem = major_problem_input.lower()
    if working == "yes" and major_problem == "no":
        if age <= 5:
            recommendation = "Continue using"
        else:
            recommendation = "Reuse (consider donating or repurposing)"
    elif working == "no" and major_problem == "no":
        recommendation = "Repair"
    elif major_problem == "yes":
        if age <= 3:
            recommendation = "Repair"
        else:
            recommendation = "Recycle"
    else:
        recommendation = "Recycle"

    print(f"\nDevice: {device_name}")
    print(f"Age: {age} year(s)")
    print(f"Recommendation: {recommendation}")

    print("\nNote: This is general guidance based on fixed rules only.")
    print("It cannot identify the exact technical fault without professional inspection.\n")
    
    return recommendation

def e_waste_information():
    # Brand and Series Information
    e_waste_data = {
        "samsung": {
            "s": {
                "common_issues": "Battery degradation, screen damage, and software issues.",
                "repair_advice": "Visit an authorized service center for battery or screen replacement.",
                "reuse_donation": "Use the device as a media player or donate it if working.",
                "recycling": "Give the device to an authorized e-waste recycler.",
                "safety": "Do not use a swollen battery or damaged charger.",
                "data_wiping": "Back up data and perform a factory reset before disposal.",
                "environmental_impact": "Improper disposal can release harmful materials and waste valuable resources.",
                "resale": "Estimated resale depends on model, age, condition, and battery health."
            },

            "a": {
                "common_issues": "Battery wear, charging problems, and screen damage.",
                "repair_advice": "Check the charger and consult a service professional for repairs.",
                "reuse_donation": "Use it for learning, music, or donate it to someone in need.",
                "recycling": "Recycle through an authorized e-waste collection center.",
                "safety": "Avoid damaged batteries and unofficial repairs.",
                "data_wiping": "Back up important files and factory reset the phone.",
                "environmental_impact": "Recycling helps recover materials and reduce electronic waste.",
                "resale": "Resale value depends on condition, storage, and market demand."
            },

            "m": {
                "common_issues": "Battery aging, charging issues, and software slowdown.",
                "repair_advice": "Get the battery or charging port inspected by a professional.",
                "reuse_donation": "Reuse the device for basic tasks or donate it if functional.",
                "recycling": "Send the device to a certified e-waste recycler.",
                "safety": "Do not use a swollen battery.",
                "data_wiping": "Back up data and perform a factory reset.",
                "environmental_impact": "Responsible recycling reduces e-waste and resource loss.",
                "resale": "Estimated resale depends on age, condition, and demand."
            }
        },

        "apple": {
            "iphone": {
                "common_issues": "Battery health reduction, screen damage, and charging issues.",
                "repair_advice": "Contact Apple or an authorized service provider.",
                "reuse_donation": "Reuse as a camera, music player, or donate if working.",
                "recycling": "Use an authorized Apple or e-waste recycling program.",
                "safety": "Avoid using a damaged or swollen battery.",
                "data_wiping": "Back up data, sign out of accounts, and erase all content.",
                "environmental_impact": "Recycling helps recover valuable materials and reduce electronic waste.",
                "resale": "Value depends on model, storage, battery health, and condition."
            },
            "ipad": {
                "common_issues": "Battery aging, screen damage, charging problems, and software issues.",
                "repair_advice": "Contact Apple or an authorized service provider for repair.",
                "reuse_donation": "Reuse it for studying, reading, media, or donate it if working.",
                "recycling": "Send the iPad to an authorized Apple or e-waste recycling program.",
                "safety": "Do not use the device if the battery is swollen or physically damaged.",
                "data_wiping": "Back up important data, sign out of Apple ID, and erase all content.",
                "environmental_impact": "Responsible recycling helps recover materials and reduces electronic waste.",
                "resale": "Value depends on model, storage, age, condition, and battery health."
            },
            "macbook": {
                "common_issues": "Battery aging, keyboard or trackpad problems, screen damage, and software issues.",
                "repair_advice": "Contact Apple or an authorized service provider for inspection and repair.",
                "reuse_donation": "Continue using it for learning or office work, or donate it if functional.",
                "recycling": "Recycle through an authorized Apple or e-waste recycling program.",
                "safety": "Avoid using a damaged battery or damaged charging equipment.",
                "data_wiping": "Back up files, sign out of accounts, and erase the Mac before disposal.",
                "environmental_impact": "Proper recycling helps recover useful materials and reduces electronic waste.",
                "resale": "Value depends on model, year, storage, condition, and battery health."
            },
            "watch": {
                "common_issues": "Battery aging, screen damage, charging problems, and software issues.",
                "repair_advice": "Contact Apple or an authorized service provider for assistance.",
                "reuse_donation": "Continue using it for fitness or notifications, or donate it if working.",
                "recycling": "Use an authorized Apple or e-waste recycling program.",
                "safety": "Do not use the device if the battery is swollen or physically damaged.",
                "data_wiping": "Back up required data, unpair the watch, and erase its content.",
                "environmental_impact": "Responsible recycling helps recover materials and reduce electronic waste.",
                "resale": "Value depends on model, age, condition, battery health, and demand."
            }
        },

        "oppo": {
            "reno": {
                "common_issues": "Battery wear, screen damage, and charging problems.",
                "repair_advice": "Visit an authorized OPPO service center.",
                "reuse_donation": "Use the phone for learning or donate it if functional.",
                "recycling": "Recycle through an authorized e-waste collection center.",
                "safety": "Do not use damaged batteries or chargers.",
                "data_wiping": "Back up data and perform a factory reset.",
                "environmental_impact": "Proper recycling helps reduce environmental pollution.",
                "resale": "Resale depends on model, age, condition, and demand."
            }
        },

        "oneplus": {
            "oneplus": {
                "common_issues": "Battery degradation, screen damage, and software problems.",
                "repair_advice": "Contact an authorized OnePlus service center.",
                "reuse_donation": "Reuse for entertainment or donate if working.",
                "recycling": "Send the device to an authorized recycler.",
                "safety": "Avoid using damaged batteries and chargers.",
                "data_wiping": "Back up files and perform a factory reset.",
                "environmental_impact": "Responsible recycling reduces electronic waste and resource loss.",
                "resale": "Estimated resale depends on condition, storage, and market demand."
            }
        },

        "xiaomi": {
            "redmi": {
                "common_issues": "Battery aging, charging problems, and screen damage.",
                "repair_advice": "Visit an authorized Xiaomi service center.",
                "reuse_donation": "Reuse for basic tasks or donate the device.",
                "recycling": "Recycle through an authorized e-waste recycler.",
                "safety": "Do not use a swollen battery or damaged charger.",
                "data_wiping": "Back up data and perform a factory reset.",
                "environmental_impact": "Recycling helps conserve resources and reduce e-waste.",
                "resale": "Resale depends on model, age, condition, and market demand."
            }
        }
    }
    brand = input("Enter device brand: ").lower().strip()
    series = input("Enter device series: ").lower().strip()
    if brand in e_waste_data:
        if series in e_waste_data[brand]:
            information = e_waste_data[brand][series]
            print("\n--- E-WASTE INFORMATION ---")
            print("Brand:", brand.title())
            print("Series:", series.title())

            print("\nCommon Issues:", information["common_issues"])
            print("Repair Advice:", information["repair_advice"])
            print("Reuse / Donation:", information["reuse_donation"])
            print("Recycling Advice:", information["recycling"])
            print("Safety Precautions:", information["safety"])
            print("Data Wiping:", information["data_wiping"])
            print("Environmental Impact:", information["environmental_impact"])
            print("Estimated Resale:", information["resale"])
        else:
            print("Sorry! This series is not available.")
    else:
        print("Sorry! This brand is not available.")
        
def digital_cleanup_tips():
    tips = [
        "Delete unnecessary downloads.",
        "Remove duplicate files.",
        "Organise files into folders.",
        "Delete unwanted emails."
    ]
    print("\n--- Digital Cleanup Tips ---")
    for tip in tips:
        print("-", tip)

def green_computing_tips():
    tips = [
        "Repair devices before replacing them.",
        "Donate working electronics.",
        "Switch off devices when not needed.",
        "Use energy-saving settings.",
        "Recycle e-waste responsibly."
    ]
    print("\n--- Green Computing Tips ---")
    for tip in tips:
        print("-", tip)
        
def main():
    while True:
        print("\n================================")
        print("          GREENTECH")
        print("================================")
        print("1. Device Advisor")
        print("2. E-Waste Information")
        print("3. Digital Cleanup Tips")
        print("4. Green Computing Tips")
        print("5. Exit")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            device_recommendation()
        elif choice == "2":
            e_waste_information()
        elif choice == "3":
            digital_cleanup_tips()
        elif choice == "4":
            green_computing_tips()
        elif choice == "5":
            print("\nThank you for using GreenTech!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")
main()
