"""
EyeOnBlue ChildShield Demo Risk Scoring Engine
 
This is a simplified open-source demo for child-centred climate-health risk scoring.
It does not include EyeOnBlue's proprietary production models or client-specific data.
"""
 
def normalize(value, min_value, max_value):
    """Normalize a value between 0 and 1."""
    if max_value == min_value:
        return 0
    return max(0, min(1, (value - min_value) / (max_value - min_value)))
 
 
def calculate_childshield_risk(data):
    """
    Calculate a simplified climate-health risk score for a school, health facility or community.
 
    Expected input:
    {
        "temperature_c": float,
        "air_quality_index": float,
        "flood_risk": float,
        "wildfire_smoke_risk": float,
        "humidity_percent": float,
        "child_exposure_index": float,
        "healthcare_access_risk": float
    }
    """
 
    heat_score = normalize(data.get("temperature_c", 25), 25, 45)
    air_quality_score = normalize(data.get("air_quality_index", 50), 0, 300)
    flood_score = normalize(data.get("flood_risk", 0), 0, 1)
    smoke_score = normalize(data.get("wildfire_smoke_risk", 0), 0, 1)
    humidity_score = normalize(data.get("humidity_percent", 40), 30, 100)
    exposure_score = normalize(data.get("child_exposure_index", 0.5), 0, 1)
    healthcare_score = normalize(data.get("healthcare_access_risk", 0.5), 0, 1)
 
    weighted_score = (
        heat_score * 0.20 +
        air_quality_score * 0.20 +
        flood_score * 0.15 +
        smoke_score * 0.15 +
        humidity_score * 0.10 +
        exposure_score * 0.10 +
        healthcare_score * 0.10
    )
 
    risk_score = round(weighted_score * 100, 2)
 
    if risk_score < 30:
        category = "Low"
    elif risk_score < 60:
        category = "Moderate"
    elif risk_score < 80:
        category = "High"
    else:
        category = "Critical"
 
    return {
        "risk_score": risk_score,
        "risk_category": category,
        "recommended_actions": generate_recommendations(category)
    }
 
 
def generate_recommendations(category):
    """Generate simple early action recommendations based on risk category."""
    if category == "Low":
        return [
            "Continue routine monitoring."
        ]
 
    if category == "Moderate":
        return [
            "Monitor weather and air quality updates.",
            "Inform school or facility staff.",
            "Prepare basic protective actions."
        ]
 
    if category == "High":
        return [
            "Limit outdoor activities for children.",

                      "Prepare shaded or cooling areas.",
            "Inform families and staff.",
            "Coordinate with local authorities and health services."
        ]
 
    return [
        "Activate emergency preparedness protocol.",
        "Suspend outdoor activities.",
        "Prepare cooling or clean-air spaces.",
        "Notify families, schools, health facilities and local authorities.",
        "Monitor vulnerable children and respiratory or heat-related symptoms."
    ]
 
 
if __name__ == "__main__":
    demo_input = {
        "temperature_c": 39,
        "air_quality_index": 160,
        "flood_risk": 0.3,
        "wildfire_smoke_risk": 0.7,
        "humidity_percent": 65,
        "child_exposure_index": 0.8,
        "healthcare_access_risk": 0.4
    }
 
    result = calculate_childshield_risk(demo_input)
    print(result)

