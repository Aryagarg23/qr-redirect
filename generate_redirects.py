import pandas as pd
import os

# Load the CSV file
csv_file = "Final_LIs_for_F24.csv"  # Replace with your CSV file
df = pd.read_csv(csv_file)

# Ensure the necessary columns exist
if 'url' not in df.columns or 'id' not in df.columns:
    raise ValueError("The CSV file must contain 'url' and 'id' columns.")

# Directory to store generated HTML files
output_dir = "redirect_files"
os.makedirs(output_dir, exist_ok=True)

# Google Analytics Measurement ID (replace with your actual Measurement ID)
google_measurement_id = "G-VSQZKE4MSS"  # Replace with your Google Analytics Measurement ID

# Generate redirect HTML files
for _, row in df.iterrows():
    # Extract necessary data
    article_id = str(row['id'])  # Ensure ID is a string
    target_url = row['url']      # The URL to redirect to

    # File name for the redirect HTML
    file_name = f"{article_id}.html"
    file_path = os.path.join(output_dir, file_name)

    # HTML content with redirection and Google Analytics (gtag.js)
    html_content = f"""
    <!DOCTYPE html>
    <html>
      <head>
        <!-- Redirect -->
        <meta http-equiv="refresh" content="1; URL='{target_url}'" />
        <!-- Google Analytics (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id={google_measurement_id}"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){{dataLayer.push(arguments);}}
          gtag('js', new Date());
          gtag('config', '{google_measurement_id}', {{
            'page_path': '/redirect_files/{file_name}'
          }});
        </script>
      </head>
      <body>
        <h1>Redirecting...</h1>
        <p>If you are not redirected automatically, click <a href="{target_url}">here</a>.</p>
      </body>
    </html>
    """

    # Write the HTML file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)

print(f"Redirect files generated in '{output_dir}' directory.")
