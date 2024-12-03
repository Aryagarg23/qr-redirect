import pandas as pd
import os

# Load the CSV file
csv_file = "Final_LIs_for_F24.csv"
df = pd.read_csv(csv_file)

# Ensure the necessary columns exist
if 'url' not in df.columns or 'id' not in df.columns:
    raise ValueError("The CSV file must contain 'url' and 'id' columns.")

# Directory to store generated HTML files
output_dir = "redirect_files"
os.makedirs(output_dir, exist_ok=True)

# Google Analytics Tracking ID (replace with your actual ID)
google_analytics_id = "UA-XXXXXXXXX-X"

# Generate redirect HTML files
for _, row in df.iterrows():
    # Extract necessary data
    article_id = str(row['id'])  # Ensure ID is a string
    target_url = row['url']      # The URL to redirect to

    # File name for the redirect HTML
    file_name = f"{article_id}.html"
    file_path = os.path.join(output_dir, file_name)

    # HTML content with redirection and Google Analytics
    html_content = f"""
    <!DOCTYPE html>
    <html>
      <head>
        <meta http-equiv="refresh" content="0; URL='{target_url}'" />
        <script>
          (function(i,s,o,g,r,a,m){{i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){{
          (i[r].q=i[r].q||[]).push(arguments)}},i[r].l=1*new Date();a=s.createElement(o),
          m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
          }})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

          ga('create', '{google_analytics_id}', 'auto');  // Replace with your Google Analytics ID
          ga('send', 'pageview', '/{file_name}');
        </script>
      </head>
      <body>
        <p>Redirecting to <a href="{target_url}">{target_url}</a>...</p>
      </body>
    </html>
    """

    # Write the HTML file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)

print(f"Redirect files generated in '{output_dir}' directory.")
