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
├── ai_studio_code.html     # Web interface with interactive sliders and charts
├── ai_studio_code.py       # Python CLI version with validation
├── server.py               # Simple HTTP server for development
└── README.md               # Basic project information
```

## Features

### Web Interface (ai_studio_code.html)
- **Interactive Controls**: Sliders and numeric inputs for all parameters
- **Real-time Calculations**: Automatic updates as parameters change
- **Visual Feedback**: 
  - Color-coded results (Red/Yellow/Green) based on recovery rates
  - Interactive bar charts showing contribution of each factor
  - Warning alerts for out-of-range parameters
- **Dual Metal Support**: Switch between Gold (Au) and Silver (Ag) calculations
- **Self-contained**: No external dependencies except Chart.js from CDN

### Python CLI (ai_studio_code.py)
- Menu-driven interface for terminal use
- Input validation with physical and operational limits
- Detailed warnings for values outside experimental ranges
- Classification of recovery rates (Low/Medium/High)

## Technical Details

### Recovery Formulas

**Gold (Au):**
```
Recovery = 35.5 - (4.2 × pH) + (0.35 × %Sulfides) + (1.8 × Grade) + (0.15 × Collector) + (0.8 × Grinding Time)
```

**Silver (Ag):**
```
Recovery = 30.0 - (3.8 × pH) + (0.40 × %Sulfides) + (0.05 × Grade) + (0.12 × Collector) + (0.9 × Grinding Time)
```

### Parameters
1. **pH de Pulpa**: Pulp pH (optimal range: 4.0-9.0)
2. **% Sulfuros**: Sulfide mineralization (0-100%)
3. **Ley de Cabeza**: Ore grade in g/t (alert: >20 g/t for Au, >200 g/t for Ag)
4. **Dosis Colector**: Collector dosage in g/t (experimental reference: ~150 g/t)
5. **Tiempo Molienda**: Grinding time in minutes (alert: >25 min)

### Recovery Classification
- **🔴 Low (< 50%)**: Requires optimization
- **🟡 Medium (50-75%)**: Standard range for ore blends
- **🟢 High (> 75%)**: Optimal efficiency

## How to Use

### Web Interface
The application is automatically served at the root URL. Simply open the Replit webview to access the interactive simulator:
1. Select the metal (Gold or Silver)
2. Adjust parameters using sliders or direct input
3. Click "CALCULAR RECUPERACIÓN" to see results
4. View the breakdown chart to understand factor contributions

### Python CLI
Run the CLI version using:
```bash
python ai_studio_code.py
```
Follow the menu to select metal type and input parameters.

## Development

### Local Server
A simple Python HTTP server is configured to serve the web interface on port 5000:
```bash
python server.py
```

### Deployment
The project is configured for static deployment, serving the HTML file and assets directly.

## Recent Changes
- 2025-12-06: Imported from GitHub and configured for Replit
- 2025-12-06: Added web server configuration and deployment settings
- 2025-12-06: Verified full functionality of interactive web interface

## Notes
- Results are clamped between 0-100%
- The models are based on experimental thesis data
- Values outside experimental ranges may reduce prediction accuracy
- No backend API required - all calculations are client-side in the web version
