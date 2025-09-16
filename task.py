import pandas as pd
from fpdf import FPDF
import os

# --- Part 1: Data Reading and Analysis ---

def analyze_data(file_path):
    """Reads a CSV file, performs basic analysis, and returns a dictionary of results."""
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        return "Error: The file was not found. Please check the file path."

    # Basic data analysis
    total_sales = df['Sales'].sum()
    total_products = df['Product_ID'].nunique()
    avg_price = df['Price'].mean()
    most_popular_product = df['Product_ID'].mode()[0]
    
    # You can add more complex analysis here
    
    # Return analysis results as a dictionary
    analysis_results = {
        'Total Sales': f"${total_sales:,.2f}",
        'Total Products': total_products,
        'Average Price': f"${avg_price:.2f}",
        'Most Popular Product': most_popular_product
    }
    
    return analysis_results

# --- Part 2: PDF Report Generation ---

def generate_pdf_report(analysis_data, output_filename="sales_report.pdf"):
    """Generates a PDF report from the analysis data."""
    pdf = FPDF()
    pdf.add_page()
    
    # Set up fonts and add a title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Sales Performance Report", ln=True, align='C')
    pdf.ln(10) # Add a line break

    # Add a subtitle
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Summary Statistics", ln=True)
    pdf.ln(2)

    # Add the analysis results to the PDF
    pdf.set_font("Arial", '', 10)
    for key, value in analysis_data.items():
        # Using a cell for the label and another for the value
        pdf.cell(60, 10, key, border=1)
        pdf.cell(0, 10, str(value), border=1, ln=True)

    # Save the PDF file
    pdf.output(output_filename)
    
    print(f"Report generated successfully: {output_filename}")

# --- Part 3: Main Execution Block ---

if __name__ == "__main__":
    # Create a dummy CSV file for demonstration if it doesn't exist
    if not os.path.exists('sales_data.csv'):
        data = {
            'Product_ID': ['P101', 'P102', 'P101', 'P103', 'P102', 'P101'],
            'Sales': [150.50, 200.00, 150.50, 50.00, 200.00, 150.50],
            'Price': [10.00, 20.00, 10.00, 5.00, 20.00, 10.00]
        }
        df = pd.DataFrame(data)
        df.to_csv('sales_data.csv', index=False)
        print("Created dummy 'sales_data.csv' for demonstration.")
    
    # Main script logic
    data_file = 'sales_data.csv'
    
    # Step 1: Analyze the data
    analysis_results = analyze_data(data_file)
    
    if isinstance(analysis_results, str):
        print(analysis_results)
    else:
        # Step 2: Generate the report
        generate_pdf_report(analysis_results)
