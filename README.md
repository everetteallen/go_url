# go_url
Link Redirector using a Google Sheet

Google Cloud function that looks up last word on the end of a calling url in a Google Sheet, gets a new URL and returns a 302 redirect with that URL.

When setting up the Google Cloud Function must set the following as Runtime Variables:

searchCol = "A"
- This is the column in the GSheet to search for the keyword

dataCol = "B"
- This is the column in the GSheet with the target redirect URL

sheetID = "xxxxxxxxxxxxxxxxxxxxxxxxx"
- This is the Google Sheet identifier taken from a sheet readable by either the Service Account of the Google Cloud Function or by anyone with the url.

-EGA