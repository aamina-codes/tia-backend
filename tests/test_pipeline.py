import glob

from pipeline.thyroid_pipeline import ThyroidPipeline

pipeline = ThyroidPipeline()

reports = glob.glob("uploaded_reports/*")

if not reports:

    print("No reports found.")

else:

    report = reports[0]

    print(f"Testing: {report}")

    result = pipeline.process(report)

    print(result)