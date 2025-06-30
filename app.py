from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = "data"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # Max 10MB file

def load_data():
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], "crm_erp_filled.xlsx")
    crm = pd.read_excel(filepath, sheet_name="CRM")
    retainers = pd.read_excel(filepath, sheet_name="Retainers")
    tasks = pd.read_excel(filepath, sheet_name="Tasks")
    return crm.to_dict(orient="records"), retainers.to_dict(orient="records"), tasks.to_dict(orient="records")

@app.route("/", methods=["GET", "POST"])
def home():
    error_msg = None

    if request.method == "POST":
        file = request.files.get("file")

        if file and file.filename.endswith(".xlsx"):
            try:
                # Save the file temporarily
                temp_path = os.path.join(app.config["UPLOAD_FOLDER"], "temp_upload.xlsx")
                file.save(temp_path)

                # Test the required sheets
                pd.read_excel(temp_path, sheet_name="CRM")
                pd.read_excel(temp_path, sheet_name="Retainers")
                pd.read_excel(temp_path, sheet_name="Tasks")

                # All sheets are valid — save it as the main file
                os.replace(temp_path, os.path.join(app.config["UPLOAD_FOLDER"], "crm_erp_filled.xlsx"))
                return redirect(url_for("home"))

            except Exception as e:
                error_msg = f"❌ Upload failed: {str(e)}"

        else:
            error_msg = "❌ Only .xlsx files are allowed."

    try:
        crm, retainers, tasks = load_data()
    except Exception as e:
        crm, retainers, tasks = [], [], []
        error_msg = f"⚠️ Failed to load data: {str(e)}"

    return render_template("index.html", crm=crm, retainers=retainers, tasks=tasks, error=error_msg)
from flask import send_file
import io

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = "data"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # Max 10MB file

def load_data():
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], "crm_erp_filled.xlsx")
    crm = pd.read_excel(filepath, sheet_name="CRM")
    retainers = pd.read_excel(filepath, sheet_name="Retainers")
    tasks = pd.read_excel(filepath, sheet_name="Tasks")
    return crm.to_dict(orient="records"), retainers.to_dict(orient="records"), tasks.to_dict(orient="records")

@app.route("/", methods=["GET", "POST"])
def home():
    error_msg = None

    if request.method == "POST":
        file = request.files.get("file")

        if file and file.filename.endswith(".xlsx"):
            try:
                # Save the file temporarily
                temp_path = os.path.join(app.config["UPLOAD_FOLDER"], "temp_upload.xlsx")
                file.save(temp_path)

                # Test the required sheets
                pd.read_excel(temp_path, sheet_name="CRM")
                pd.read_excel(temp_path, sheet_name="Retainers")
                pd.read_excel(temp_path, sheet_name="Tasks")

                # All sheets are valid — save it as the main file
                os.replace(temp_path, os.path.join(app.config["UPLOAD_FOLDER"], "crm_erp_filled.xlsx"))
                return redirect(url_for("home"))

            except Exception as e:
                error_msg = f"❌ Upload failed: {str(e)}"

        else:
            error_msg = "❌ Only .xlsx files are allowed."

    try:
        crm, retainers, tasks = load_data()
    except Exception as e:
        crm, retainers, tasks = [], [], []
        error_msg = f"⚠️ Failed to load data: {str(e)}"

    return render_template("index.html", crm=crm, retainers=retainers, tasks=tasks, error=error_msg)
from flask import send_file
import io

@app.route("/export-summary")
def export_summary():
    crm, retainers, tasks = load_data()

    total_clients = len(crm)
    active_retainers = sum(1 for r in retainers if str(r.get("Status", "")).lower() == "active")
    total_tasks = len(tasks)
    completed_tasks = sum(1 for t in tasks if str(t.get("Status", "")).lower() == "completed")

    summary_data = {
        "Metric": ["Total Clients", "Active Retainers", "Total Tasks", "Completed Tasks"],
        "Value": [total_clients, active_retainers, total_tasks, completed_tasks]
    }

    summary_df = pd.DataFrame(summary_data)

    # Save to in-memory buffer
    buffer = io.StringIO()
    summary_df.to_csv(buffer, index=False)
    buffer.seek(0)

    return send_file(
        io.BytesIO(buffer.getvalue().encode()),
        mimetype="text/csv",
        download_name="dashboard_summary.csv",
        as_attachment=True
    )
if __name__ == "__main__":
    app.run(debug=True)