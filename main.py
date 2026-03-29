import os
import re
import json
import requests
from PyPDF2 import PdfReader

# === CONFIGURATION ===
PDF_FOLDER = r'C:\Users\Jenson_Temp\Downloads\Internship Project API\references'
HUGGINGFACE_API_KEY = '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'
TOGETHER_API_KEY = 'tgp_v1_FByqD1xegXK3z7wK8-Ny-2sT9MgWBPboMwEwWmsI4Vo'

PDF_FILES = {
    'Titanium ref 1.pdf': 'Titanium Grade 2',
    'Titanium ref 2.pdf': 'Titanium Grade 2 (Annealed)',
    'Titanium ref 3.pdf': 'Titanium Grade 2 (Variant 1)',
    'Titanium ref 4.pdf': 'Titanium Grade 2 (CP Titanium Strip and Foil)',
    'Titanium ref 5.pdf': 'Titanium Grade 2 (Variant 2)',
    'Titanium ref 6.pdf': 'Titanium Grade 2 (Variant 3)',
    'Titanium ref 7.pdf': 'Titanium Grade 2 (UNS R50400)'
}

# Expected keys
PROPERTY_KEYS = [
    "yield_strength_mpa",
    "ultimate_strength_mpa",
    "youngs_modulus_gpa",
    "elongation_percent",
    "poissons_ratio",
    "density_gcm3",
    "thermal_conductivity_wmk",
    "thermal_expansion_coefficient"
]

# === EXTRACT TEXT FROM PDF ===
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

# === HUGGING FACE AI: EXTRACT RAW PROPERTIES ===
def extract_properties_with_huggingface(text):
    prompt = (
        "Extract the following material properties from the text below: "
        "Yield Strength (MPa), Ultimate Strength (MPa), Young's Modulus (GPa), "
        "Percentage Elongation (%), Poisson's Ratio, Density (g/cm3), "
        "Thermal Conductivity (W/mK), Coefficient of Thermal Expansion.\n\n"
        f"Text:\n{text}\n\n"
        "Return as JSON with these keys: yield_strength_mpa, ultimate_strength_mpa, "
        "youngs_modulus_gpa, elongation_percent, poissons_ratio, density_gcm3, "
        "thermal_conductivity_wmk, thermal_expansion_coefficient."
    )

    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(
        "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta",
        headers=headers,
        json={"inputs": prompt}
    )

    try:
        result = response.json()
        match = re.search(r'\{.*\}', str(result), re.DOTALL)
        if not match:
            raise ValueError("No JSON found in response")

        properties = json.loads(match.group())

        # Fill missing keys with "NA"
        for key in PROPERTY_KEYS:
            properties.setdefault(key, "NA")

        return properties

    except Exception as e:
        print(f"❌ Hugging Face AI extraction failed: {e}")
        return {key: "NA" for key in PROPERTY_KEYS}

# === TOGETHER AI: FORMAT INTO MEANINGFUL TABLE ===
def format_properties_with_together_ai(properties):
    prompt = (
        "Format the following material properties into a neat list with units:\n\n"
        f"{properties}\n\n"
        "Return in this format:\n"
        "- Density: 4.51 g/cm3\n"
        "- Yield Strength: 275 MPa\n"
        "- Ultimate Strength: 344 MPa\n"
        "- Elongation: 20%\n"
        "- Poisson's Ratio: 0.37\n"
        "- Young's Modulus: 105 GPa\n"
        "- Thermal Conductivity: 16.4 W/mK\n"
        "- Thermal Expansion Coefficient: 8.6 m/mC"
    )

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers=headers,
        json={
            "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3
        }
    )

    try:
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"❌ Together AI formatting failed: {e}")
        # fallback: raw dict
        return "\n".join(f"- {k}: {v}" for k, v in properties.items())

# === MAIN ===
def main():
    print("📁 Processing PDFs and formatting extracted material properties...\n")

    for filename, material_name in PDF_FILES.items():
        pdf_path = os.path.join(PDF_FOLDER, filename)
        if not os.path.exists(pdf_path):
            print(f"⚠ File not found: {filename}")
            continue

        print(f"\n📄 {filename} → {material_name}")
        text = extract_text_from_pdf(pdf_path)

        # Step 1: Extract with Hugging Face
        raw_properties = extract_properties_with_huggingface(text)

        # Step 2: Format with Together AI
        formatted_output = format_properties_with_together_ai(raw_properties)
        print("✅ Extracted Properties:\n")
        print(formatted_output)

if __name__ == "__main__":
    main()
