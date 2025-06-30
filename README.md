# 🧩 Flask CRM + ERP System

A lightweight, customizable **CRM + ERP dashboard** built with **Flask** and **Bootstrap**, designed for small service-based teams and freelancers. This tool enables you to manage client retainers, tasks, and business summaries directly from an Excel file.

---

## 🔧 Features

- 📁 Upload Excel files (with multiple sheets: CRM, Retainers, Tasks)
- 📊 Filter and search client and task data directly in the browser
- 🔄 Refresh data from uploaded files on the fly
- 📤 Export dashboard summaries to CSV
- 🔒 No database required — works entirely on structured Excel files

---

## 🖥️ Live Demo (Optional)
> *(If deployed, paste your link here)*  
**http://127.0.0.1:5000/** — local development

---

## 📂 Excel File Structure

Your Excel should have the following **sheet names**:

- `CRM`: Contains client/company details
- `Retainers`: Active/inactive service contracts
- `Tasks`: Associated deliverables or milestones

You can generate mock data using the [Faker library](https://faker.readthedocs.io/).

---

## 🛠️ Tech Stack

- Python 3
- Flask
- Pandas
- Bootstrap (via HTML templates)
- OpenPyXL (Excel support)

---

## 🚀 Getting Started

1. **Clone the repo:**

```bash
g✍️ Author
Built by Aman Ali — focused on automating business workflows with Python, Pandas, dashboards, and web scraping.it clone https://github.com/doc727/flask_crm_erp_app.git
cd flask_crm_erp_app
