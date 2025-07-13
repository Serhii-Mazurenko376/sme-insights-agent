# 📄 PDF Text Chunking – Demo Output

This is the log of a successful run of the `chunk_text.py` script inside the `pdf_tools/` folder.

---

## ✅ Terminal Output

```
👋 Hello World
🟢 Script started
✅ Loaded text (604 characters)
[DEBUG] Extracted raw text:
ACME Corp. - Income Statement (Q1 2025)
Revenue: $120,000
Cost of Goods Sold: $65,000
Gross Profit: $55,000
Operating Expenses:
- Salaries: $20,000
- Rent: $5,000
- Marketing: $8,000
Operating Profit: $22,000
Other Expenses:
- Interest: $3,000
- Depreciation: $2,000
Net Profit: $17,000
Notes:
- Revenue dropped 15% compared to Q4 2024.
- Marketing spend increased by 60%.
- Inventory turnover slowed.

📦 Chunks: ['ACME Corp. - Income Statement (Q1 2025)\nRevenue: $120,000\nCost of Goods Sold: $65,000', 
'Gross Profit: $55,000\nOperating Expenses:\n- Salaries: $20,000\n- Rent: $5,000\n- Marketing: $8,000', 
'Operating Profit: $22,000\nOther Expenses:\n- Interest: $3,000\n- Depreciation: $2,000', 
'Net Profit: $17,000\nNotes:\n- Revenue dropped 15% compared to Q4 2024.\n- Marketing spend increased by 60%.\n- Inventory turnover slowed.']
✂️ Total Chunks: 4

--- Chunk 1 ---
ACME Corp. - Income Statement (Q1 2025)
Revenue: $120,000
Cost of Goods Sold: $65,000

--- Chunk 2 ---
Gross Profit: $55,000
Operating Expenses:
- Salaries: $20,000
- Rent: $5,000
- Marketing: $8,000

--- Chunk 3 ---
Operating Profit: $22,000
Other Expenses:
- Interest: $3,000
- Depreciation: $2,000

--- Chunk 4 ---
Net Profit: $17,000
Notes:
- Revenue dropped 15% compared to Q4 2024.
- Marketing spend increased by 60%.
- Inventory turnover slowed.

✅ Chunks were also saved to output_chunks.txt
```

---

## 🧾 File Reference

- Script: `pdf_tools/chunk_text.py`
- PDF File: `data/income_statement_q1_2025.pdf`
- Output File: `output_chunks.txt`

---

## 🛠️ Tips

- Use `print(text)` and `print(chunks)` early to debug
- Adjust `max_chars` to control chunk size
- If `import` fails, ensure correct path + `__init__.py` exists

---

Made with 💻 by **PennyPilot Team**
