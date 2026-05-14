# ChildShield Risk Scoring Schema
 
This document describes the initial data schema for the EyeOnBlue ChildShield demo risk scoring engine.
 
## Objective
 
The objective is to generate child-centred climate-health risk scores for schools, health facilities and communities without collecting personal data from children.
 
## Entity Types
 
The system can generate scores for:
 
- School
- Health facility
- Community / neighbourhood
- Public space
 
## Input Indicators
 
### Climate and Environmental Indicators
 
- Temperature
- Heat index
- Humidity
- UV level
- Air quality index
- PM2.5
- PM10
- Wildfire smoke exposure
- Flood risk
- Extreme weather warning
- Power outage risk, if available
- Drought or water stress indicator, if available
 
### Exposure Indicators
 
- School location
- Health facility location
- Distance to nearest health facility
- Community population density
- Aggregated child population estimate
- Outdoor activity exposure, if available
- Critical infrastructure exposure, if available

### Vulnerability Indicators
 
- High child population density
- Limited access to healthcare
- High heat exposure
- Repeated air quality anomalies
- Flood-prone area
- Wildfire-prone area
- Service disruption risk
 
## Output
 
The system generates:
 
- Risk score from 0 to 100
- Risk category: Low, Moderate, High, Critical
- Main contributing hazards
- Recommended early actions
 
## Example Output
 
```json
{
  "entity_type": "school",
  "entity_name": "Demo School A",
  "location": "Antalya, Türkiye",
  "risk_score": 78,
  "risk_category": "High",
  "main_hazards": ["Extreme heat", "Poor air quality", "Wildfire smoke exposure"],
  "recommended_actions": [
    "Limit outdoor activities",
    "Prepare shaded or cooling areas",
    "Inform families and school staff",
    "Monitor respiratory symptoms",
    "Coordinate with local health services"
  ]
}
```
 
## Privacy Principle
 
The model does not require personal child data. It uses aggregated demographic indicators, facility 
