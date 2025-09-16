#CODTECH-TASK-2

COMPANY : CODTECH IT SOLUTIONS

NAME : AJAY NEGI

INTERN ID : CT08DY1001 

DOMAIN : PYTHON PROGRAMMING

DURATION : 8 WEEKS

MENTOR : NEELA SANTHOSH KUMAR

This project demonstrates how to perform basic sales data analysis in Python using pandas and how to automatically generate a professional-looking PDF report with the help of the fpdf library. It is designed as a beginner-friendly project that combines data analysis and simple reporting into one complete workflow.

The program starts by attempting to read sales data from a CSV file. If no such file exists, it creates a small dummy dataset containing product IDs, sales values, and prices to ensure that the script can run without requiring additional files. This approach makes the project self-contained and easy to test immediately. Once the dataset is loaded, the code uses pandas to calculate several key performance indicators. These include the total sales revenue, the number of unique products sold, the average product price, and the most popular product based on frequency. These simple metrics provide a quick overview of business performance and can be easily extended with additional calculations such as profit margins, regional sales breakdowns, or time-series trends.

After the analysis, the script automatically generates a PDF report using the fpdf library. The PDF starts with a centered title, followed by a subtitle for summary statistics. Each metric is displayed in a clean tabular style, with labels in one column and values in another, making the report easy to read and understand. The use of formatting such as bold fonts, spacing, and borders improves the professional appearance of the report. Finally, the PDF is saved to the local directory, allowing it to be shared or archived.

The project is structured into three main parts for clarity and reusability. The first part, analyze_data(), is responsible for reading the file and computing the required statistics. It includes basic error handling to notify users if the file is missing. The second part, generate_pdf_report(), handles the layout and creation of the PDF. This separation of concerns makes the code more modular and easier to maintain. The third part, the main execution block, ties everything together. It creates a CSV if none exists, calls the analysis function, and then passes the results to the PDF generator.

From a technical perspective, this project highlights how pandas simplifies data manipulation while fpdf provides flexible tools for report generation. Even though the analysis here is basic, the same workflow can be scaled to larger datasets and more advanced metrics. For example, sales data could be grouped by region or month, and charts created with matplotlib could be embedded into the PDF for visualization. Additional improvements could include dynamic filenames with timestamps, input validation for unexpected CSV formats, or interactive dashboards as a complement to static reports.

In conclusion, this project demonstrates the complete journey from raw data to polished report. It shows how Python can be used not only for analysis but also for presenting results in a professional format that non-technical stakeholders can understand. By combining automation, analysis, and reporting in a single script, this project offers a practical foundation for real-world business applications in sales reporting, finance, and beyond.

#OUTPUT

<img width="960" height="540" alt="Image" src="https://github.com/user-attachments/assets/2ec78f71-e26d-4703-8eac-49c79892f7e5" />

