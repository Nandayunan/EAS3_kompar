# flow control

## Tentang Aplikasi

`flow control` adalah aplikasi simulasi pengendalian lalu lintas cerdas yang saya kembangkan untuk menunjukkan konsep pemrosesan terdistribusi dan paralel pada simulasi empat jalur. Aplikasi ini memisahkan fungsi menjadi beberapa node (acquisition, analysis, controller, dashboard) yang berjalan sebagai proses terpisah dan saling bertukar pesan lewat multiprocessing queues.

## Pembuat

- Abdy Ananda Yunan — 152022100

## Ringkasan Singkat

Aplikasi menampilkan antarmuka dashboard yang menampilkan statistik per-lajur, grafik waktu-nyata, serta panel performa paralel/sekuensial. Terdapat dua mode operasi:
- Live pipeline: Node A–C berjalan sebagai proses terpisah dan mengirimkan hasil ke dashboard (Node D) melalui antrian IPC.
- Standalone simulation: Dashboard berjalan sendiri dan menghasilkan data simulasi untuk demonstrasi.

## Fitur Utama

- Arsitektur pipeline terdistribusi (Node A → Node B → Node C → Node D)
- Mode live (multiprocessing) dan mode simulasi lokal
- Dashboard profesional dengan kartu per-lajur dan grafik bar waktu-nyata
- Benchmark performa paralel vs sekuensial untuk demonstrasi speedup
- Logging asinkron ke `logs/traffic_log.csv`

## Persyaratan

- Python 3.10 atau lebih baru
- Paket Python: `PyQt5`, `matplotlib`

Instalasi dependensi:
```bash
pip install PyQt5 matplotlib
```

## Cara Menjalankan

- Jalankan pipeline penuh (processes + GUI):
```bash
python run_system.py
```

- Jalankan hanya GUI (mode simulasi lokal):
```bash
python dashboard_gui.py
```

Menutup jendela GUI akan menghentikan proses latar belakang ketika dijalankan dalam mode pipeline.

## Struktur Proyek (ringkas)

- `run_system.py` — peluncur pipeline multiprocess dan GUI
- `dashboard_gui.py` — antarmuka dashboard (PyQt5)
- `nodes/` — modul node: `acquisition_node`, `analysis_node`, `controller_node`, `dashboard_node`
- `benchmark/` — modul uji performa paralel vs sekuensial
- `simulator/` — generator data lalu lintas acak
- `logs/` — CSV log otomatis

---

Jika Anda ingin saya menambahkan `requirements.txt`, contoh screenshot dashboard, atau menyesuaikan teks README ini lebih lanjut (mis. bahasa Inggris atau format akademik), beri tahu saya — saya akan tambahkan.
