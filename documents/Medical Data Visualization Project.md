# Medical Data Visualization Project.docx

Clinical Informatics Report: Longitudinal Physiological Analysis and Digital Health Visualization Architecture for Patient E.A.C.

1. Executive Summary and Clinical Informatics Framework

This comprehensive report serves a dual purpose: first, to provide an exhaustive clinical analysis of the longitudinal medical data for patient Elizabeth Ann Chadwell (DOB: 03/27/1947), a 77-year-old female with a complex history of cardiovascular and metabolic conditions; and second, to architect a robust digital health solution—comprising a structured dataset and an interactive visualization dashboard—that empowers the patient and her care team to monitor these physiological trends effectively.

The analysis synthesizes data from a series of clinical encounters spanning from October 2024 through February 2026. This period captures a critical window in the patient's trajectory, characterized by the management of Coronary Artery Disease (CAD), Non-ST-Elevation Myocardial Infarction (NSTEMI), and emerging metabolic volatilities. The report integrates raw laboratory values 1 with evidence-based clinical guidelines and informatics best practices to deliver a nuanced interpretation of her health status.

1.1 Clinical Trajectory and Key Findings

The longitudinal data reveals a patient navigating the delicate balance of geriatric chronic disease management. Several high-priority clinical narratives have emerged from the deep analysis of the provided records:

Metabolic Instability and Glycemic Volatility: The patient exhibits a distinct "U-shaped" trajectory in glycemic control. Initial measurements in October 2024 showed an elevated Hemoglobin A1c (HbA1c) of 7.3%. Following therapeutic interventions, this improved significantly to 6.4% by July 2025. However, this control was not sustained, with a regression to 7.3% by February 2026, accompanied by a concerning random glucose spike to 247 mg/dL. This pattern suggests a recent deterioration in metabolic regulation that requires immediate investigation.1

Supraphysiological Micronutrient Status: A striking anomaly is the sudden, dramatic elevation in Vitamin B12 levels, rising from a normal baseline to >1,500 pg/mL in February 2026, alongside persistently elevated Vitamin D levels (>120 ng/mL). In the absence of documented hepatopathology or hematologic malignancy, this pattern strongly implies exogenous hyper-supplementation. This presents a risk of masking other hematologic conditions or causing toxicity, necessitating a review of all supplements.2

Thyroid Axis Dynamics: The patient experienced a period of subclinical hyperthyroidism in mid-2025 (TSH suppressed to 0.107–0.207 uIU/mL), which has since resolved with TSH normalizing to 0.598 uIU/mL in February 2026. The potential for biotin interference in these immunoassays remains a critical differential diagnosis given the B12/Vitamin D findings.4

Cardiovascular Resilience amid Diastolic Dysfunction: Despite a history of NSTEMI, the patient’s lipid profile is aggressively managed (LDL ~53 mg/dL), likely reflecting high-intensity statin therapy adherence. Structurally, the heart demonstrates hyperdynamic Left Ventricular (LV) function (EF 70-75%) but confirms Grade 1 Diastolic Dysfunction. This diagnosis, common in elderly women, requires vigilant fluid management to prevent progression to Heart Failure with Preserved Ejection Fraction (HFpEF).5

1.2 Informatics Deliverables Overview

To address the user's request for data organization and visualization, this report includes:

Structured Data Schema: A normalized, machine-readable CSV dataset extracted from the unstructured PDF reports, adhering to "tidy data" principles suitable for longitudinal analysis.

Interactive Visualization Dashboard: A fully functional, single-file HTML/JavaScript solution leveraging the Chart.js library. This tool allows the user to dynamically filter between metabolic, cardiovascular, and hematologic views, providing visual context through reference range annotations and trend lines.

2. Comprehensive Clinical Data Analysis

2.1 Cardiovascular and Hemodynamic Profile

The patient's cardiovascular health is the cornerstone of her prognosis, given her documented history of CAD and NSTEMI. The integration of laboratory lipids with echocardiographic data provides a multi-dimensional view of her cardiac status.

2.1.1 Structural Heart Function: Echocardiographic Analysis

The echocardiogram dated October 15, 2024, provides a critical baseline for structural function. In a 77-year-old female with ischemic history, the interplay between systolic and diastolic function is paramount.1

Left Ventricular Systolic Function:

The Left Ventricular Ejection Fraction (LVEF) is estimated at 70-75%. While a "normal" LVEF is typically defined as 50-70%, a hyperdynamic state (>70%) in an elderly female warrants careful interpretation.

Physiological Context: Hyperdynamic function can sometimes be a compensatory mechanism for volume depletion (dehydration) or reduced afterload (low blood pressure), though the patient’s blood pressure was recorded as 102/59 mmHg, which is on the lower side of normal.1

Clinical Implication: This robust systolic function is a positive prognostic indicator post-NSTEMI, suggesting that the ischemic event did not result in significant myocardial necrosis or wall motion abnormalities (LV wall motion was noted as normal).

Diastolic Function: Grade 1 Dysfunction:

The report classifies the patient with Grade 1 Diastolic Dysfunction (Impaired Relaxation).

Pathophysiology: Diastolic dysfunction refers to the stiffening of the ventricular wall, impairing the heart's ability to relax and fill passively during the diastolic phase of the cardiac cycle. In Grade 1, the left ventricle relaxes slower than normal. This is largely an age-related phenomenon in 77-year-olds, driven by myocardial fibrosis and collagen deposition.5

Hemodynamic Consequence: In this stage, the heart relies heavily on the "atrial kick" (the contraction of the left atrium) to complete filling. The ratio of early (E) to late (A) filling velocities typically reverses.

Clinical Management: The primary goal is to manage heart rate (to allow sufficient filling time) and blood pressure (to reduce wall stress). The absence of significant pulmonary hypertension (Right Ventricular Systolic Pressure < 35 mmHg) is reassuring, indicating that the diastolic stiffness has not yet transmitted high pressures backward into the pulmonary circulation.6

2.1.2 Lipid Management and Secondary Prevention

The lipid panel from November 27, 2024, demonstrates exceptional control, clearly indicating effective pharmacological intervention.

Analysis: Current guidelines for patients with established Atherosclerotic Cardiovascular Disease (ASCVD), such as this patient with prior NSTEMI, recommend an LDL target of <70 mg/dL, with some European guidelines advocating for <55 mg/dL.8 An LDL of 53 mg/dL represents ideal adherence to these rigorous secondary prevention targets.

Lipid Ratios: The HDL of 66 mg/dL is protective. The Triglyceride/HDL ratio is <1.0, which is a strong marker of insulin sensitivity and low atherogenic particle size, contrasting somewhat with the A1c data (discussed below).

2.2 Metabolic and Endocrine Systems Analysis

2.2.1 Glycemic Control and Diabetes Management

The patient’s glucose metabolism shows significant volatility, presenting a complex management challenge often seen in geriatric diabetes.

Longitudinal Glycemic Trends:

The data reveals a concerning regression in control over the observed period:

Hypoglycemia Risk (July 2025): The HbA1c of 6.4% in July 2025 appeared excellent on paper, but the concurrent random glucose of 62 mg/dL reveals a hidden danger. In geriatric patients (age >75), hypoglycemia is a potent predictor of adverse events, including falls, fractures, and cognitive decline.9 The "tight control" strategy may have been too aggressive.

Recurrent Hyperglycemia (Feb 2026): The return to an A1c of 7.3% and a random glucose of 247 mg/dL suggests a recent precipitating factor. Potential causes include:

Medication Non-adherence: Discontinuation of oral hypoglycemics or insulin.

Dietary Changes: Increased carbohydrate intake.

Infection/Stress: Acute illness can drive cortisol release, spiking glucose.

Steroid Therapy: Use of corticosteroids for other conditions (e.g., COPD, arthritis) would sharply elevate glucose.

Guideline Context: For a 77-year-old with complex comorbidities (CAD), the American Diabetes Association (ADA) suggests a relaxed A1c target of <7.5% or even <8.0% to prioritize safety over strict euglycemia.9 While 7.3% is within this "acceptable" range, the random spike to 247 mg/dL is symptomatic of volatility that needs stabilization.

2.2.2 Thyroid Axis Function

The thyroid data presents a narrative of resolving subclinical hyperthyroidism.

Suppressed TSH (2025): TSH values of 0.107 and 0.207 uIU/mL in 2025, with normal Free T4 (implied), characterize subclinical hyperthyroidism. In the elderly, this increases the risk of Atrial Fibrillation and osteoporosis.

Normalization (2026): The TSH recovery to 0.598 uIU/mL in Feb 2026 indicates the axis has re-regulated. This could be due to a dose reduction in Levothyroxine (if the patient is hypothyroid treated) or the natural resolution of a thyroiditis phase.

Interference Consideration: High-dose biotin intake (discussed below regarding B12) can cause falsely low TSH results in streptavidin-biotin immunoassays.4 Given the patient's massive B12 spike, biotin interference leading to the artifactual appearance of hyperthyroidism (low TSH) must be ruled out.

2.3 Micronutrient Anomalies: The "More is Not Better" Phenomenon

A critical finding in the February 2026 data is the extreme elevation of micronutrients, signaling a potential case of supplement overuse.

2.3.1 Vitamin B12 (Cobalamin)

Trend: 400 pg/mL (Jul 2025) → 359 pg/mL (Oct 2025) → >1,500 pg/mL (Feb 2026).

Interpretation: This >4x increase in 4 months is physiologically impossible via dietary sources alone. It strongly indicates the initiation of high-dose supplementation (oral or injectable).

Clinical Significance:

Direct Toxicity: Vitamin B12 is water-soluble and generally safe, but levels >1,000 pg/mL have been associated with acne-form dermatitis and, in some observational studies, a correlation with higher mortality in hospitalized elderly patients, though causation is debated.3

Diagnostic Masking: High B12 can be a marker for underlying hematologic malignancies (e.g., CML, Polycythemia Vera) or liver disease, where the liver releases stored B12. However, the patient's normal liver enzymes (AST 28, ALT 21) and normal WBC count (4.6) make these organic causes less likely than supplementation.12

2.3.2 Vitamin D (25-Hydroxy)

Trend: 120 ng/mL → 135 ng/mL → 126 ng/mL. All values are flagged High.

Risk Assessment: The optimal therapeutic range is 30–100 ng/mL. Levels >100 ng/mL approach the threshold for toxicity.14

Consequences: The primary risk of hypervitaminosis D is hypercalcemia, which can lead to kidney stones, renal insufficiency, and vascular calcification.

Correlation: The patient’s Calcium levels have trended upward: 9.5 (Nov '24) → 9.9 (Jul '25) → 9.8 (Oct '25) → 10.1 mg/dL (Feb '26). While 10.1 is still within the normal range (8.5-10.4), the upward drift toward the upper limit in the context of Vitamin D >125 ng/mL suggests incipient physiological impact.2

2.4 Hematology and Renal Function

2.4.1 Hematologic Stability

The Complete Blood Count (CBC) trends reflect stability:

Hemoglobin: Ranging 13.4 – 14.4 g/dL. This rules out anemia (iron deficiency or anemia of chronic disease), which is common in geriatric cohorts.

White Blood Cells: Stable (3.9 – 5.1 k/cumm), indicating no active infection or profound immunosuppression.

Platelets: Stable (140 – 176 k/cumm).

2.4.2 Renal Function Trajectory

A subtle but important decline in renal function is evident.

eGFR Trend: 87 (Jul '25) → 87 (Oct '25) → 70 mL/min/1.73m² (Feb '26).

Analysis: A drop of 17 mL/min in 4 months is significant. While eGFR >60 is technically "non-CKD," the rapid rate of decline warrants investigation.

Possible Drivers:

Dehydration: Common in elderly, leads to prerenal azotemia.

Hypercalcemia: As noted above, high Vitamin D/Calcium can impair renal concentration mechanisms.

Medication Effect: Initiation of diuretics or ACE inhibitors for heart failure/blood pressure.

Diabetes: The spike in glucose (247 mg/dL) can induce hyperfiltration initially, but fluctuations strain the glomerulus.

3. Data Organization and Structured Dataset

To fulfill the user's request for a spreadsheet, the unstructured data from the PDF reports has been extracted, normalized, and structured into a CSV-ready format. This schema follows "Tidy Data" principles, where each row represents a single observation, making it ideal for pivot tables and visualization software.

3.1 Dataset Schema Definition

The dataset is structured with the following columns:

Date: The date of sample collection (YYYY-MM-DD format for sorting).

Category: Clinical grouping (e.g., Metabolic, Hematology, Thyroid).

Test Name: Standardized nomenclature for the biomarker.

Result Value: The numeric result extracted.

Result Unit: The unit of measurement (e.g., mg/dL).

Reference Low: The lower bound of the "Normal" range.

Reference High: The upper bound of the "Normal" range.

Flag: Clinical flags (L=Low, H=High).

Notes: Contextual details (e.g., "Fasting", "Random").

3.2 Master Laboratory Dataset (CSV Content)

This table contains all extracted data points and is formatted for direct copy-pasting into Excel or Google Sheets.

4. Interactive Visualization Architecture

To fulfill the requirement for an "interactive webpage," I have designed a self-contained, client-side application. This solution uses standard web technologies (HTML5, CSS3, and JavaScript) and leverages the Chart.js library for data visualization. This approach ensures privacy (data runs locally in the browser) and accessibility.

4.1 Design Philosophy and User Experience (UX) Strategy

The dashboard is engineered with specific consideration for a 77-year-old user and their care team:

Cognitive Accessibility: Instead of overwhelming the user with a "data wall," the design uses a Dropdown Selector mechanism. This allows the user to focus on one biomarker at a time (e.g., "Show me my Diabetes trends").

Contextual Annotation: Raw numbers are abstract. The charts utilize Shaded Reference Bands (using the chartjs-plugin-annotation library) to visually demarcate the "Normal Range." If a data point falls inside the green box, it is normal; if outside, it requires attention. This reduces the cognitive load of interpreting numeric values.16

Visual Hierarchy: High-contrast colors are used (Safety Blue for trends, Alert Red/Orange for out-of-range values). Fonts are large and sans-serif (Segoe UI/Roboto) to ensure readability on varying screen sizes.

Trend Visualization: Line charts are selected over bar charts to emphasize the trajectory of health over time, which is critical for conditions like diabetes and renal function where the rate of change is as important as the absolute value.18

4.2 Implementation Code

The following code block contains the complete source code for the dashboard. It can be saved as an .html file (e.g., PatientDashboard.html) and opened in any web browser.



HTML





<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient Health Dashboard: Elizabeth Ann Chadwell</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation@2.1.0/dist/chartjs-plugin-annotation.min.js"></script>
    
    <style>
        /* CSS Variables for consistent theming */
        :root {
            --primary-color: #2c3e50; /* Dark Slate */
            --accent-color: #3498db;  /* Medical Blue */
            --alert-color: #e74c3c;   /* Red for alerts */
            --warning-color: #f39c12; /* Orange for warnings */
            --bg-color: #f8f9fa;      /* Light Grey Background */
            --card-bg: #ffffff;       /* White Card Background */
            --success-color: #27ae60; /* Green */
        }

        body {
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-color);
            margin: 0;
            padding: 20px;
            color: #333;
            line-height: 1.6;
        }

       .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        /* Header Styling */
        header {
            background: linear-gradient(135deg, var(--primary-color), #34495e);
            color: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        h1 { margin: 0; font-size: 2rem; font-weight: 600; }
       .patient-info { 
            font-size: 1rem; 
            opacity: 0.9; 
            margin-top: 8px; 
            font-weight: 300; 
            letter-spacing: 0.5px;
        }

        /* KPI Cards Grid */
       .stat-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
       .stat-card {
            background: var(--card-bg);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            border-left: 5px solid var(--accent-color);
            transition: transform 0.2s ease;
        }
       .stat-card:hover { transform: translateY(-3px); }
       .stat-label { 
            font-size: 0.85rem; 
            color: #7f8c8d; 
            text-transform: uppercase; 
            letter-spacing: 1px; 
            font-weight: 600;
        }
       .stat-value { 
            font-size: 1.8rem; 
            font-weight: 700; 
            color: var(--primary-color); 
            margin: 10px 0 5px 0; 
        }
       .stat-date { font-size: 0.8rem; color: #95a5a6; font-style: italic; }
        
        /* Utility classes for dynamic coloring of KPI cards */
       .border-red { border-left-color: var(--alert-color); }
       .border-orange { border-left-color: var(--warning-color); }
       .border-green { border-left-color: var(--success-color); }
       .text-red { color: var(--alert-color); }

        /* Controls Section */
       .controls {
            background: var(--card-bg);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 25px;
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            align-items: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            border: 1px solid #e1e8ed;
        }
       .control-group {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        label { font-weight: 600; color: var(--primary-color); }
        select {
            padding: 12px;
            font-size: 1rem;
            border: 1px solid #bdc3c7;
            border-radius: 6px;
            min-width: 250px;
            background-color: #fff;
            cursor: pointer;
        }
        select:focus { outline: 2px solid var(--accent-color); border-color: transparent; }

        /* Legend for Reference Range */
       .chart-legend {
            margin-left: auto;
            display: flex;
            align-items: center;
            font-size: 0.9rem;
            color: #666;
            background: #f8f9fa;
            padding: 8px 15px;
            border-radius: 20px;
        }
       .legend-box {
            width: 15px;
            height: 15px;
            background-color: rgba(75, 192, 192, 0.15);
            border: 1px solid rgba(75, 192, 192, 0.6);
            margin-right: 8px;
            border-radius: 3px;
        }

        /* Charts Section */
       .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 25px;
        }
       .chart-card {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            position: relative;
            height: 450px;
            border: 1px solid #e1e8ed;
        }
        h3 { margin-top: 0; color: var(--primary-color); font-size: 1.1rem; }

        /* Footer */
        footer {
            margin-top: 40px;
            text-align: center;
            font-size: 0.85rem;
            color: #95a5a6;
            padding-bottom: 20px;
        }
    </style>
</head>
<body>

<div class="container">
    <header>
        <h1>Longitudinal Health Dashboard</h1>
        <div class="patient-info">
            <strong>Patient:</strong> CHADWELL, ELIZABETH ANN  |  
            <strong>DOB:</strong> 03/27/1947 (Age 77)  |  
            <strong>MR#:</strong> 000205791
        </div>
    </header>

    <div class="stat-grid">
        <div class="stat-card border-red">
            <div class="stat-label">HbA1c (Diabetes)</div>
            <div class="stat-value text-red">7.3%</div>
            <div class="stat-date">Last: Feb 05, 2026</div>
        </div>
        <div class="stat-card border-red">
            <div class="stat-label">Random Glucose</div>
            <div class="stat-value text-red">247 <span style="font-size:1rem">mg/dL</span></div>
            <div class="stat-date">Last: Feb 05, 2026</div>
        </div>
        <div class="stat-card border-orange">
            <div class="stat-label">Vitamin B12</div>
            <div class="stat-value" style="color:var(--warning-color)">>1,500 <span style="font-size:1rem">pg/mL</span></div>
            <div class="stat-date">Last: Feb 05, 2026</div>
        </div>
        <div class="stat-card border-green">
            <div class="stat-label">LDL Cholesterol</div>
            <div class="stat-value" style="color:var(--success-color)">60 <span style="font-size:1rem">mg/dL</span></div>
            <div class="stat-date">Last: Feb 05, 2026</div>
        </div>
    </div>

    <div class="controls">
        <div class="control-group">
            <label for="metricSelect">Select Biomarker to Visualize:</label>
            <select id="metricSelect" onchange="updateChart()">
                <optgroup label="Metabolic & Diabetes">
                    <option value="HbA1c">Hemoglobin A1c (%)</option>
                    <option value="Glucose">Glucose (mg/dL)</option>
                </optgroup>
                <optgroup label="Vitamins">
                    <option value="Vitamin B12">Vitamin B12 (pg/mL)</option>
                    <option value="Vitamin D">Vitamin D (ng/mL)</option>
                </optgroup>
                <optgroup label="Thyroid Function">
                    <option value="TSH">TSH (uIU/mL)</option>
                    <option value="Free T4">Free T4 (ng/dL)</option>
                </optgroup>
                <optgroup label="Hematology">
                    <option value="WBC">White Blood Cells (k/cumm)</option>
                    <option value="Hemoglobin">Hemoglobin (g/dL)</option>
                    <option value="Platelets">Platelets (k/cumm)</option>
                </optgroup>
                <optgroup label="Renal Function">
                    <option value="eGFR">eGFR (mL/min)</option>
                    <option value="Creatinine">Creatinine (mg/dL)</option>
                </optgroup>
                <optgroup label="Lipids (Cholesterol)">
                    <option value="LDL Calculated">LDL Cholesterol (mg/dL)</option>
                    <option value="HDL">HDL Cholesterol (mg/dL)</option>
                    <option value="Triglycerides">Triglycerides (mg/dL)</option>
                </optgroup>
            </select>
        </div>
        
        <div class="chart-legend">
            <div class="legend-box"></div>
            <span>Shaded Area = Normal Reference Range</span>
        </div>
    </div>

    <div class="dashboard-grid">
        <div class="chart-card">
            <canvas id="mainChart"></canvas>
        </div>
        
        <div class="chart-card">
            <h3>Metabolic Correlation: A1c vs Glucose</h3>
            <canvas id="scatterChart"></canvas>
        </div>
    </div>

    <footer>
        <p>Data Source: Clinical Laboratory Reports (Oct 2024 - Feb 2026). <br>
        <strong>Disclaimer:</strong> This dashboard is for informational purposes only. The green shaded regions represent standard adult reference ranges. 
        Specific targets for patients with Diabetes/CAD (e.g., A1c goals) may differ based on physician guidance.</p>
    </footer>
</div>

<script>
    /**
     * 1. CENTRALIZED DATA REPOSITORY
     * Extracted from the PDF reports. This array serves as the single source of truth.
     * Tidy Data format: Each object is one observation.
     */
    const labData =;

    // Global references for chart instances to allow destruction/updating
    let mainChartInstance = null;
    let scatterChartInstance = null;

    /**
     * Helper: Returns measurement unit string based on test name.
     */
    function getUnit(testName) {
        const units = {
            'HbA1c': '%', 'Glucose': 'mg/dL', 'TSH': 'uIU/mL', 'Vitamin B12': 'pg/mL',
            'Vitamin D': 'ng/mL', 'WBC': 'k/cumm', 'Hemoglobin': 'g/dL', 'Platelets': 'k/cumm',
            'eGFR': 'mL/min', 'Creatinine': 'mg/dL', 'LDL Calculated': 'mg/dL', 
            'HDL': 'mg/dL', 'Triglycerides': 'mg/dL', 'Free T4': 'ng/dL'
        };
        return units[testName] |

| '';
    }

    /**
     * Logic to extract specific series data for Chart.js
     */
    function getChartData(testName) {
        // Filter and Sort by Date
        const filtered = labData
           .filter(d => d.test === testName)
           .sort((a,b) => new Date(a.date) - new Date(b.date));
        
        if (filtered.length === 0) return null;

        return {
            dates: filtered.map(d => d.date),
            values: filtered.map(d => d.value),
            // Use the reference range from the most recent test
            min: filtered[filtered.length-1].min,
            max: filtered[filtered.length-1].max,
            unit: getUnit(testName)
        };
    }

    /**
     * MAIN CHART RENDER FUNCTION
     */
    function updateChart() {
        const selectedMetric = document.getElementById('metricSelect').value;
        const data = getChartData(selectedMetric);

        if (!data) return;

        const ctx = document.getElementById('mainChart').getContext('2d');

        // Clean up previous chart to avoid memory leaks/visual glitches
        if (mainChartInstance) mainChartInstance.destroy();

        // Aesthetic: Create a gradient fill for the line chart
        const gradient = ctx.createLinearGradient(0, 0, 0, 400);
        gradient.addColorStop(0, 'rgba(52, 152, 219, 0.4)');
        gradient.addColorStop(1, 'rgba(52, 152, 219, 0.0)');

        // Chart Configuration
        mainChartInstance = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.dates,
                datasets:
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: false, 
                        title: { display: true, text: data.unit, font: { weight: 'bold' } }
                    },
                    x: {
                        grid: { display: false } // Cleaner look
                    }
                },
                plugins: {
                    annotation: {
                        annotations: {
                            // The Green Box representing the Normal Range
                            box1: {
                                type: 'box',
                                yMin: data.min,
                                yMax: data.max,
                                backgroundColor: 'rgba(75, 192, 192, 0.15)', // Transparent Green
                                borderColor: 'rgba(75, 192, 192, 0.5)',
                                borderWidth: 1,
                                label: {
                                    display: true,
                                    content: 'Normal Range (' + data.min + '-' + data.max + ')',
                                    position: 'start',
                                    color: '#27ae60',
                                    font: { size: 11 }
                                }
                            }
                        }
                    },
                    tooltip: {
                        backgroundColor: 'rgba(44, 62, 80, 0.9)',
                        padding: 12,
                        titleFont: { size: 14 },
                        bodyFont: { size: 14 },
                        displayColors: false,
                        callbacks: {
                            label: function(context) {
                                return `Result: ${context.parsed.y} ${data.unit}`;
                            }
                        }
                    },
                    legend: {
                        display: true,
                        labels: { font: { size: 14 } }
                    }
                }
            }
        });
    }

    /**
     * SCATTER CHART: GLUCOSE VS HBA1C
     * Shows the relationship between long-term control (A1c) and point-in-time (Glucose)
     */
    function initScatterChart() {
        const a1cData = labData.filter(d => d.test === 'HbA1c');
        const glucData = labData.filter(d => d.test === 'Glucose');
        
        const scatterPoints =;
        
        // Data Matching Logic: Find Glucose and A1c readings on same date
        a1cData.forEach(a => {
            const g = glucData.find(g => g.date === a.date);
            if(g) {
                scatterPoints.push({ x: a.value, y: g.value, date: a.date });
            }
        });

        const ctx2 = document.getElementById('scatterChart').getContext('2d');
        scatterChartInstance = new Chart(ctx2, {
            type: 'scatter',
            data: {
                datasets:
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: { 
                        title: { display: true, text: 'HbA1c (%)', font: { weight: 'bold' } },
                        min: 5.0, max: 8.0 
                    },
                    y: { 
                        title: { display: true, text: 'Glucose (mg/dL)', font: { weight: 'bold' } },
                        min: 50, max: 300
                    }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function(ctx) {
                                return `${ctx.raw.date}: A1c ${ctx.raw.x}% / Glucose ${ctx.raw.y}`;
                            }
                        }
                    }
                }
            }
        });
    }

    // Initialize Dashboard on Load
    document.addEventListener('DOMContentLoaded', () => {
        updateChart(); // Default view
        initScatterChart();
    });

</script>
</body>
</html>


5. Conclusions and Strategic Recommendations

The synthesis of longitudinal data for patient E.A.C. presents a clinical picture of a geriatric patient with robust cardiovascular defense mechanisms but emerging vulnerabilities in metabolic regulation and micronutrient homeostasis.

Immediate Metabolic Intervention: The regression in glycemic control (A1c 7.3%, Random Glucose 247 mg/dL) necessitates a review of the diabetic pharmacotherapy regimen. While the A1c is within the "safe" geriatric range (<7.5%), the volatility (swinging from 62 to 247 mg/dL) poses a fall risk.

Micronutrient Rationalization: The supra-therapeutic levels of Vitamin B12 (>1,500 pg/mL) and Vitamin D (>120 ng/mL) suggest supplement overuse. A "brown bag" medication review is recommended to discontinue unnecessary supplementation and prevent potential hypercalcemic toxicity.

Diastolic Dysfunction Management: With Grade 1 Diastolic Dysfunction, the patient is sensitive to volume status. The decline in eGFR (87 to 70 mL/min) serves as an early warning of hemodynamic shifting or dehydration, reinforcing the need for careful fluid management.

Digital Monitoring Strategy: The provided CSV schema and interactive dashboard offer a scalable framework for ongoing health tracking. This tool will allow the patient and caregivers to visualize trends instantly, moving from reactive "snapshot" medicine to proactive, trend-based management.

End of Report

Works cited

_medical_mom_labs Combined.pdf

Vitamin D Toxicity - PMC, accessed February 7, 2026, https://pmc.ncbi.nlm.nih.gov/articles/PMC7427646/

Association between Elevated Plasma Vitamin B12 and Short-Term Mortality in Elderly Patients Hospitalized in an Internal Medicine Unit - PMC, accessed February 7, 2026, https://pmc.ncbi.nlm.nih.gov/articles/PMC10749720/

Some Vitamins May Skew Lab Results - My Doctor Online, accessed February 7, 2026, https://mydoctor.kaiserpermanente.org/mas/news/some-vitamins-may-skew-lab-results-2816469

Age- and Gender-Specific Changes in the Left Ventricular Relaxation: A Doppler Echocardiographic Study in Healthy Individuals - American Heart Association Journals, accessed February 7, 2026, https://www.ahajournals.org/doi/10.1161/circimaging.108.809087

Diastolic Dysfunction: Causes, Symptoms and Treatment - Cleveland Clinic, accessed February 7, 2026, https://my.clevelandclinic.org/health/diseases/23434-diastolic-dysfunction

Is grade 1 diastolic dysfunction considered heart failure? - Dr.Oracle, accessed February 7, 2026, https://www.droracle.ai/articles/228269/is-grade-1-diastolic-dysfunction-considered-heart-failure

2023 ESC Guidelines for Managing CVD in Diabetes: Key Points—Part 1, accessed February 7, 2026, https://www.acc.org/Latest-in-Cardiology/ten-points-to-remember/2023/09/08/18/40/2023-esc-guidelines-cvd-diabetes-part-1-esc-2023

Chapter 37 Diabetes in Older People, accessed February 7, 2026, https://www.diabetes.ca/health-care-providers/clinical-practice-guidelines/chapter-37

Elderly HbA1c Goals and Complications - Juniper Publishers, accessed February 7, 2026, https://juniperpublishers.com/crdoj/pdf/CRDOJ.MS.ID.555931.pdf

Biotin Interference with Laboratory Assays - Quest Diagnostics, accessed February 7, 2026, https://www.questdiagnostics.com/healthcare-professionals/clinical-education-center/faq/faq202

High Vitamin B12 Levels: Causes, Symptoms, and What to Do Next - Rupa Health, accessed February 7, 2026, https://www.rupahealth.com/post/high-vitamin-b12-levels-causes-symptoms-and-what-to-do-next

What causes high Vitamin B12 without supplements? - SiPhox Health, accessed February 7, 2026, https://siphoxhealth.com/articles/what-causes-high-vitamin-b12-without-supplements

Vitamin D Toxicity: What It Is, Causes, Symptoms & Treatment - Cleveland Clinic, accessed February 7, 2026, https://my.clevelandclinic.org/health/diseases/24750-vitamin-d-toxicity-hypervitaminosis-d

Signs, Symptoms, and Side Effects of Too Much Vitamin D - Healthline, accessed February 7, 2026, https://www.healthline.com/nutrition/vitamin-d-side-effects

Presentation of clinical laboratory results: an experimental comparison of four visualization techniques - PMC, accessed February 7, 2026, https://pmc.ncbi.nlm.nih.gov/articles/PMC3638193/

Usage | chartjs-plugin-annotation, accessed February 7, 2026, https://www.chartjs.org/chartjs-plugin-annotation/latest/guide/usage.html

Visualization of Patient-Generated Health Data: A Scoping Review of Dashboard Designs, accessed February 7, 2026, https://pmc.ncbi.nlm.nih.gov/articles/PMC10665122/

Best practices for data visualization: creating and evaluating a report for an evidence-based fall prevention program - PMC, accessed February 7, 2026, https://pmc.ncbi.nlm.nih.gov/articles/PMC7647241/