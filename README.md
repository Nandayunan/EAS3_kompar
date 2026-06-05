# Urban Flow — FLow Control

## Contributors

- Abdy Ananda Yunan - 152022100

Versi yang telah dimodifikasi dari proyek "Distributed Smart Traffic Simulator" — ditata ulang untuk tampilan profesional dan kemudahan penggunaan.

## Ringkasan
`Urban Flow` adalah simulator kendali lalu lintas cerdas yang memisahkan tugas acquisition, analysis, controller, dan dashboard ke proses terpisah yang saling berkomunikasi menggunakan multiprocessing queues. GUI modern dibuat dengan PyQt5; visualisasi menggunakan Matplotlib.

## Fitur Utama
- Pipeline terdistribusi (Node A → Node B → Node C → Node D)
- Mode live pipeline (multiprocess) dan mode standalone (simulasi lokal)
- Visual dashboard profesional (tema terang), kartu per-lajur, dan grafik bar waktu-nyata
- Benchmark paralel vs sekuensial untuk demonstrasi speedup
- Logging asinkron ke `logs/traffic_log.csv`

## Perubahan penting pada versi ini
- Tampilan GUI dirombak menjadi tema terang dan layout profesional (`Urban Flow`).
- Grafik historial diganti menjadi chart bar per siklus untuk presentasi lebih jelas.
- Penambahan helper `detect_vehicle` pada `nodes/controller_node.py` agar modul benchmark dapat berjalan.

## Persyaratan
- Python 3.10+
- Paket: `PyQt5`, `matplotlib`

Instalasi paket:
```bash
pip install PyQt5 matplotlib
```

## Cara Menjalankan
- Jalankan full pipeline (Node A/B/C sebagai proses terpisah dan GUI):
```bash
python run_system.py
```
- Jalankan hanya GUI (mode simulasi lokal):
```bash
python dashboard_gui.py
```

## Struktur Proyek (ringkas)
- `run_system.py` — peluncur pipeline multiprocess dan GUI
- `dashboard_gui.py` — GUI PyQt5 (Urban Flow)
- `nodes/` — modul node (acquisition, analysis, controller, dashboard)
- `benchmark/` — tes performa paralel vs sekuensial
- `simulator/` — generator data lalu lintas acak
- `logs/` — CSV log otomatis

## Catatan
- Menutup GUI akan memicu shutdown bersih pada proses latar belakang ketika dijalankan via `run_system.py`.
- Jika Anda ingin saya commit perubahan README ini ke branch baru, beri tahu nama branch yang diinginkan.

---

Versi ini dirancang untuk presentasi dan demonstrasi; beri tahu saya jika Anda ingin bahasa lain, detail teknis tambahan, atau penyusunan ulang konten.
