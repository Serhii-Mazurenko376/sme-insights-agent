import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pdf_tools.extract_text import extract_text_from_pdf

def chunk_text(text: str, max_chars: int = 100):
    """
    Splits long text into chunks of approximately `max_chars` characters.
    """
    chunks = []
    current = ""
    for line in text.splitlines():
        if len(current) + len(line) + 1 < max_chars:
            current += line + "\n"
        else:
            chunks.append(current.strip())
            current = line + "\n"
    if current:
        chunks.append(current.strip())
    return chunks

if __name__ == "__main__":
    print("🟢 Script started")
    pdf_path = "data/income_statement_q1_2025.pdf"  # or another file if testing
    try:
        text = extract_text_from_pdf(pdf_path)
        print(f"✅ Loaded text ({len(text)} characters)")
        print("[DEBUG] Extracted raw text:\n", text)

        chunks = chunk_text(text)
        print(f"📦 Chunks: {chunks}")
        print(f"✂️ Total Chunks: {len(chunks)}")

        for i, chunk in enumerate(chunks[:3], 1):  # print only first 3 chunks
            print(f"\n--- Chunk {i} ---\n{chunk}")

        # Save all chunks to a text file
        output_path = "output_chunks.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            for i, chunk in enumerate(chunks, 1):
                f.write(f"--- Chunk {i} ---\n{chunk}\n\n")

        print(f"📄 Chunks saved to {output_path}")

    except Exception as e:
        print(f"[ERROR] {e}")
