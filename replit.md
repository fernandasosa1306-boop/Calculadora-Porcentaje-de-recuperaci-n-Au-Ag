# Metallurgical Simulator - Gold & Silver Recovery Calculator

## Overview
This is a web-based metallurgical simulator for calculating gold (Au) and silver (Ag) recovery percentages based on various operational parameters. The project was developed as part of a thesis project and uses predictive models to estimate recovery rates.

## Project Purpose
The simulator allows metallurgical engineers and researchers to:
- Calculate recovery percentages for gold (Au) and silver (Ag)
- Adjust operational parameters including pH, sulfur content, ore grade, collector dosage, and grinding time
- Visualize the impact of each parameter on recovery rates through interactive charts
- Get real-time feedback on parameter ranges and operational alerts

## Project Structure
```
.
├── ai_studio_code.html     # Web frontend with interactive sliders and charts
├── ai_studio_code.py       # Python CLI version with validation
├── server.py               # Flask backend with API endpoint
└── README.md               # Basic project information
```

## Features

### Web Interface (ai_studio_code.html + server.py)
- **Interactive Controls**: Sliders and numeric inputs for all parameters
- **Backend Calculations**: Flask API processes recovery calculations in Python
- **Visual Feedback**: 
  - Color-coded results (Red/Yellow/Green) based on recovery rates
  - Interactive bar charts showing contribution of each factor
  - Warning alerts for out-of-range parameters
- **Dual Metal Support**: Switch between Gold (Au) and Silver (Ag) calculations

### Python CLI (ai_studio_code.py)
- Menu-driven interface for terminal use
- Input validation with physical and operational limits
- Detailed warnings for values outside experimental ranges
- Classification of recovery rates (Low/Medium/High)

## Technical Details

### API Endpoint
- **POST /api/calcular**: Accepts JSON with parameters and returns recovery calculation
  - Request: `{ metal, x1, x2, x3, x4, x5 }`
  - Response: `{ recuperacion, clasificacion, components }`

### Recovery Formulas

**Gold (Au):**
```
Recovery = 35.5 - (4.2 x pH) + (0.35 x %Sulfides) + (1.8 x Grade) + (0.15 x Collector) + (0.8 x Grinding Time)
```

**Silver (Ag):**
```
Recovery = 30.0 - (3.8 x pH) + (0.40 x %Sulfides) + (0.05 x Grade) + (0.12 x Collector) + (0.9 x Grinding Time)
```

### Parameters
1. **pH de Pulpa**: Pulp pH (optimal range: 4.0-9.0)
2. **% Sulfuros**: Sulfide mineralization (0-100%)
3. **Ley de Cabeza**: Ore grade in g/t (alert: >20 g/t for Au, >200 g/t for Ag)
4. **Dosis Colector**: Collector dosage in g/t (experimental reference: ~150 g/t)
5. **Tiempo Molienda**: Grinding time in minutes (alert: >25 min)

### Recovery Classification
- **Low (< 50%)**: Requires optimization
- **Medium (50-75%)**: Standard range for ore blends
- **High (> 75%)**: Optimal efficiency

## How to Use

### Web Interface
The application is automatically served at the root URL:
1. Select the metal (Gold or Silver)
2. Adjust parameters using sliders or direct input
3. Click "CALCULAR RECUPERACION (BACKEND)" to see results
4. View the breakdown chart to understand factor contributions

### Python CLI
Run the CLI version using:
```bash
python ai_studio_code.py
```
Follow the menu to select metal type and input parameters.

## Development

### Local Server
The Flask server runs the web interface and API on port 5000:
```bash
python server.py
```

### Deployment
The project is configured for autoscale deployment with Flask serving both the frontend and API.

## Recent Changes
- 2025-12-06: Upgraded to backend-connected version with Flask API
- 2025-12-06: Added /api/calcular endpoint for server-side calculations
- 2025-12-06: Updated deployment configuration for autoscale

## Notes
- Results are clamped between 0-100%
- The models are based on experimental thesis data
- Values outside experimental ranges may reduce prediction accuracy
- Calculations are now performed server-side in Python
